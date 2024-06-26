#!/usr/bin/env python3
""" LIFOCache: Cache with Last In First Out algorithm
"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """ A LIFO caching system
    """

    def __init__(self):
        """Initialize the caching system
        """
        super().__init__()
        self.last_in_keys = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            # If the cache is full, Remove last item first
            # if we are not updating an existent key
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                key_to_remove = self.last_in_keys.popleft()
                self.cache_data.pop(key_to_remove)
                print('DISCARD:', key_to_remove)

            # Update cache
            self.cache_data[key] = item

            # If the key is already in last_in_keys, remove it first
            if key in self.last_in_keys:
                self.last_in_keys.remove(key)

            # Enqueue the key to last_in_keys queue
            self.last_in_keys.appendleft(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
