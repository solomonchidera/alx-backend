#!/usr/bin/env python3
""" Module docs """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Class docs """
    def put(self, key, item):
        """ Function docs """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get function docs """
        return self.cache_data.get(key, None)
