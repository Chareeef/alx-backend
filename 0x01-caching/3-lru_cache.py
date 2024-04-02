#!/usr/bin/env python3
""" LRUCache: Cache with Least Recently Used implementation
"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """ A LRU caching system
    """

    def __init__(self):
        """Initialize the caching system
        """
        super().__init__()
        self.lru_keys = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            # If the cache is full, firstly remove
            # the least recently used item if we are
            # not updating an existent key
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                key_to_remove = self.lru_keys.pop()
                self.cache_data.pop(key_to_remove)
                print('DISCARD:', key_to_remove)

            # Update cache
            self.cache_data[key] = item

            # If the key was already in lru_keys, remove it first
            if key in self.lru_keys:
                self.lru_keys.remove(key)

            # Add the key to lru_keys queue
            self.lru_keys.appendleft(key)

    def get(self, key):
        """ Get an item by key
        """
        # Try to retrieve the item
        item = self.cache_data.get(key)

        if item:
            # Remove old mark in self.lru_keys if it exists
            if key in self.lru_keys:
                self.lru_keys.remove(key)

            # Mark it as recently used
            self.lru_keys.appendleft(key)

        # Return the item or None
        return item
