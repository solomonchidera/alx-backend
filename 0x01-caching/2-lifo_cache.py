#!/usr/bin/env python3
""" Module doc """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Class doc"""

    def __init__(self):
        """Function doc"""
        super().__init__()

    def put(self, key, item):
        """Function docs"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """ Function doc """
        return self.cache_data.get(key)
