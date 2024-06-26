#!/usr/bin/env python3
""" module doc """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """class doc"""

    def __init__(self):
        """function doc"""
        super().__init__()

    def put(self, key, item):
        """function"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """function doc"""
        return self.cache_data.get(key)
