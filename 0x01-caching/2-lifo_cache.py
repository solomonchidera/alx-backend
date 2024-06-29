#!/usr/bin/env python3
"""define a LIFO caching class"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """a class for a lifo cache"""
    def __init__(self):
        """initiation method"""
        super().__init__()

    def put(self, key, item):
        """Assign the item value for the key key."""
        if key is None or item is None:  # Correct handling of None values.
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:  # Correct condition.
                last_in = self.cache_data.popitem()  # Correct LIFO removal.
                print(f"DISCARD: {last_in[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
