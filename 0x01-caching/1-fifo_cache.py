#!/usr/bin/env python3
""" FIFOCache: Cache with First In First Out implementation
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """ A FIFO caching system
    """

    def __init__(self):
        """Initialize the caching system
        """
        super().__init__()
        self.first_in_keys = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            # If the cache is full, Remove the first in element
            if len(self.cache_data) == self.MAX_ITEMS:
                key_to_remove = self.first_in_keys.pop()
                self.cache_data.pop(key_to_remove)
                print('DISCARD:', key_to_remove)

            # Update cache
            self.cache_data[key] = item

            # If the key was already in first_in_keys, remove it first
            if key in self.first_in_keys:
                self.first_in_keys.remove(key)

            # Push the key to the stack
            self.first_in_keys.appendleft(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
