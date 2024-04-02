#!/usr/bin/env python3
""" MRUCache: Cache with Most Recently Used algorithm
"""
from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    """ An MRU caching system
    """

    def __init__(self):
        """Initialize the caching system
        """
        super().__init__()
        self.mru_keys = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            # If the cache is full, start by removing
            # the most recently used key if we
            # are not updating an existent key
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                key_to_remove = self.mru_keys.popleft()
                self.cache_data.pop(key_to_remove)
                print('DISCARD:', key_to_remove)

            # Update cache
            self.cache_data[key] = item

            # If the key is already in mru_keys, remove it first
            if key in self.mru_keys:
                self.mru_keys.remove(key)

            # Enqueue the key to mru_keys queue
            self.mru_keys.appendleft(key)

    def get(self, key):
        """ Get an item by key
        """
        # Try to retrieve the item
        item = self.cache_data.get(key)

        if item:
            # Remove the key's old log in self.mru_keys if it exists
            if key in self.mru_keys:
                self.mru_keys.remove(key)

            # Mark the key as MRU
            self.mru_keys.appendleft(key)

        # Return the item or None
        return item
