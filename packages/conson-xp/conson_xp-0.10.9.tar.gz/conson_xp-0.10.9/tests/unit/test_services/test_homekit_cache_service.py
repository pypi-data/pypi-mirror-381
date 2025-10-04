"""Unit tests for HomeKitCacheService."""

import tempfile
from datetime import datetime, timedelta
from pathlib import Path, PosixPath
from unittest.mock import Mock

from xp.models import ConbusDatapointResponse
from xp.models.cache import CacheEntry
from xp.models.response import Response
from xp.models.telegram.reply_telegram import ReplyTelegram
from xp.services.homekit.homekit_cache_service import HomeKitCacheService


class TestHomeKitCacheService:
    """Test cases for HomeKitCacheService"""

    def setup_method(self):
        """Setup test fixtures"""
        # Create temporary file for each test
        self.temp_cache_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.temp_cache_file.close()
        self.temp_cache_path = Path(self.temp_cache_file.name)

        # Create mock services
        self.mock_output_service = Mock()
        self.mock_lightlevel_service = Mock()
        self.mock_telegram_service = Mock()

    def teardown_method(self):
        """Cleanup test fixtures"""
        # Clean up temporary cache file
        self.temp_cache_path.unlink(missing_ok=True)

    def _create_service(self, cache_file=None):
        """Helper method to create HomeKitCacheService with mocked dependencies"""
        return HomeKitCacheService(
            cache_file=cache_file or str(self.temp_cache_path),
            conbus_output_service=self.mock_output_service,
            conbus_lightlevel_service=self.mock_lightlevel_service,
            telegram_service=self.mock_telegram_service,
        )

    def test_service_initialization_default_cache_file(self):
        """Test service initialization with default cache file"""
        service = self._create_service(cache_file=".homekit_cache.json")

        expected_cache_file = PosixPath(".homekit_cache.json")
        assert service.cache_file == expected_cache_file
        assert isinstance(service.cache, dict)

    def test_service_initialization_custom_cache_file(self):
        """Test service initialization with custom cache file"""
        service = self._create_service()

        assert service.cache_file == self.temp_cache_path
        assert isinstance(service.cache, dict)

    def test_cache_miss_queries_device(self):
        """Test cache miss triggers device query"""
        self.mock_output_service.get_output_state.return_value = (
            ConbusDatapointResponse(
                success=True,
                datapoint_telegram=ReplyTelegram(
                    checksum="CK", raw_telegram="device_response"
                ),
            )
        )

        service = self._create_service()
        response = service.get("test_device", "test_tag")

        # Should call device
        self.mock_output_service.get_output_state.assert_called_once_with("test_device")

        # Should return cache miss response
        assert response.hit is False
        assert response.data == "device_response"
        assert response.error is None

        # Should store in cache
        assert "test_device" in service.cache
        assert service.cache["test_device"].data == "device_response"

    def test_cache_hit_returns_cached_data(self):
        """Test cache hit returns cached data without device query"""
        service = self._create_service()

        # Manually add cache entry
        service.cache["test_device"] = CacheEntry(
            data="cached_data", tags=["test_tag"], ttl=300
        )

        response = service.get("test_device", "test_tag")

        # Should not call device
        self.mock_output_service.get_output_state.assert_not_called()

        # Should return cache hit response
        assert response.hit is True
        assert response.data == "cached_data"
        assert response.error is None

    def test_expired_cache_entry_triggers_device_query(self):
        """Test expired cache entry triggers new device query"""
        self.mock_output_service.get_output_state.return_value = (
            ConbusDatapointResponse(
                success=True,
                datapoint_telegram=ReplyTelegram(
                    checksum="CK", raw_telegram="fresh_data"
                ),
            )
        )

        service = self._create_service()

        # Add expired cache entry
        expired_entry = CacheEntry(data="old_data", tags=["test_tag"], ttl=1)
        expired_entry.timestamp = datetime.now() - timedelta(seconds=2)
        service.cache["test_device"] = expired_entry

        response = service.get("test_device", "test_tag")

        # Should call device for fresh data
        self.mock_output_service.get_output_state.assert_called_once_with("test_device")

        # Should return fresh data
        assert response.hit is False
        assert response.data == "fresh_data"

        # Old entry should be removed, new entry added
        assert service.cache["test_device"].data == "fresh_data"

    def test_device_query_failure(self):
        """Test handling of device query failure"""
        self.mock_output_service.get_output_state.return_value = Response(
            success=False, data=None, error="Device timeout"
        )

        response = self._create_service().get("test_device", "test_tag")

        # Should return error response
        assert response is not None
        assert response.hit is False
        assert response.data is None
        assert response.error is not None
        assert "Device timeout" in response.error

    def test_device_query_exception(self):
        """Test handling of device query exception"""
        self.mock_output_service.get_output_state.side_effect = Exception(
            "Connection error"
        )

        response = self._create_service().get("test_device", "test_tag")

        # Should return error response
        assert response is not None
        assert response.hit is False
        assert response.data is None
        assert response.error is not None
        assert "Connection error" in response.error

    def test_set_cache_entry(self):
        """Test manually setting cache entry"""
        service = self._create_service()
        service.set("test_device", "test_tag", "manual_data")

        # Should create cache entry
        assert "test_device" in service.cache
        entry = service.cache["test_device"]
        assert entry.data == "manual_data"
        assert "test_tag" in entry.tags

    def test_set_updates_existing_entry(self):
        """Test setting cache entry updates existing entry"""
        service = self._create_service()

        # Create initial entry
        service.cache["test_device"] = CacheEntry(
            data="old_data", tags=["old_tag"], ttl=300
        )
        old_timestamp = service.cache["test_device"].timestamp

        # Update entry
        service.set("test_device", "new_tag", "new_data")

        # Should update existing entry
        entry = service.cache["test_device"]
        assert entry.data == "new_data"
        assert "old_tag" in entry.tags
        assert "new_tag" in entry.tags
        assert entry.timestamp > old_timestamp

    def test_clear_specific_key(self):
        """Test clearing specific cache key"""
        service = self._create_service()

        # Add multiple entries
        service.set("device1", "tag1", "data1")
        service.set("device2", "tag2", "data2")

        # Clear specific key
        service.clear("device1")

        # Should remove only specified key
        assert "device1" not in service.cache
        assert "device2" in service.cache

    def test_clear_by_tag(self):
        """Test clearing cache entries by tag"""
        service = self._create_service()

        # Add entries with different tags
        service.set("device1", "output_state", "data1")
        service.set("device2", "output_state", "data2")
        service.set("device3", "module_info", "data3")

        # Clear by tag
        service.clear("output_state")

        # Should remove entries with specified tag
        assert "device1" not in service.cache
        assert "device2" not in service.cache
        assert "device3" in service.cache

    def test_clear_entire_cache(self):
        """Test clearing entire cache"""
        service = self._create_service()

        # Add multiple entries
        service.set("device1", "tag1", "data1")
        service.set("device2", "tag2", "data2")

        # Clear entire cache
        service.clear()

        # Should remove all entries
        assert len(service.cache) == 0

    def test_items_returns_active_entries(self):
        """Test items returns only active (non-expired) entries"""
        service = self._create_service()

        # Add active entry
        service.cache["active_device"] = CacheEntry(
            data="active_data", tags=["tag1"], ttl=300
        )

        # Add expired entry
        expired_entry = CacheEntry(data="expired_data", tags=["tag2"], ttl=1)
        expired_entry.timestamp = datetime.now() - timedelta(seconds=2)
        service.cache["expired_device"] = expired_entry

        items = service.items()

        # Should return only active entries
        assert "active_device" in items
        assert "expired_device" not in items
        assert items["active_device"] == "active_data"

    def test_received_event_invalidates_tagged_entries(self):
        """Test received_event invalidates cache entries with matching tag"""
        service = self._create_service()

        # Add entries with different tags
        service.set("device1", "output_state", "data1")
        service.set("device2", "output_state", "data2")
        service.set("device3", "module_info", "data3")

        # Invalidate by event
        service.received_event("output_state")

        # Should remove entries with matching tag
        assert "device1" not in service.cache
        assert "device2" not in service.cache
        assert "device3" in service.cache

    def test_received_update_creates_or_updates_entry(self):
        """Test received_update creates or updates cache entry"""
        service = self._create_service()

        # Update non-existing entry
        service.set("new_device", "status", "new_data")

        # Should create new entry
        assert "new_device" in service.cache
        entry = service.cache["new_device"]
        assert entry.data == "new_data"
        assert "status" in entry.tags

        # Update existing entry
        old_timestamp = entry.timestamp
        service.set("new_device", "other_status", "updated_data")

        # Should update existing entry
        entry = service.cache["new_device"]
        assert entry.data == "updated_data"
        assert "status" in entry.tags
        assert "other_status" in entry.tags
        assert entry.timestamp > old_timestamp

    def test_cache_persistence_save_and_load(self):
        """Test cache data persistence to file"""
        # Create service and add data
        service1 = self._create_service()
        service1.set("persistent_device", "test_tag", "persistent_data")

        # Create new service instance
        service2 = self._create_service()

        # Should load persisted data
        assert "persistent_device" in service2.cache
        assert service2.cache["persistent_device"].data == "persistent_data"

    def test_cache_persistence_handles_corrupted_file(self):
        """Test cache persistence handles corrupted cache file gracefully"""
        # Write invalid JSON to cache file
        self.temp_cache_path.write_text("invalid json content")

        # Should not raise exception
        service = self._create_service()

        # Should have empty cache
        assert len(service.cache) == 0

    def test_get_cache_stats(self):
        """Test cache statistics calculation"""
        service = self._create_service()

        # Add active entry
        service.cache["active_device"] = CacheEntry(
            data="active_data", tags=["tag1"], ttl=300
        )

        # Add expired entry
        expired_entry = CacheEntry(data="expired_data", tags=["tag2"], ttl=1)
        expired_entry.timestamp = datetime.now() - timedelta(seconds=2)
        service.cache["expired_device"] = expired_entry

        stats = service.get_cache_stats()

        assert stats["total_entries"] == 2
        assert stats["expired_entries"] == 1
        assert stats["active_entries"] == 1
