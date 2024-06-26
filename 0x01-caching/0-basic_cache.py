#!/usr/bin/env python3
""" Module doc """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Class doc"""

    def put(self, key, item):
        """Function doc"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Function doc"""
        return self.cache_data.get(key)
