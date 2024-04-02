#!/usr/bin/env python3
""" BaseCache module : Cache with no limit
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ An unlimited Cache
    """
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
