#!/usr/bin/env python3
""" LFUCache: Cache with Least Frequently Used algorithm
"""
from base_caching import BaseCaching
from collections import deque


class LFUCache(BaseCaching):
    """ An LFU caching system
    """

    def __init__(self):
        """Initialize the caching system
        """
        super().__init__()

        # LFU Dictionary: { key: number of uses, ... }
        self.lfu_keys = {}

        # Keep track of least recently used keys
        self.lru_keys = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            # If the cache is full, firstly remove
            # the least frequently used item if we are
            # not updating an existent key
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                # Find the least number of uses
                min_uses = min(self.lfu_keys.values())

                # Find keys with corresponding min_uses
                least_fu_keys = [key for key, n_uses in self.lfu_keys.items()
                                 if n_uses == min_uses]

                # Find the LRU key among least_fu_keys
                for idx in range(len(self.lru_keys) - 1, -1, -1):
                    if self.lru_keys[idx] in least_fu_keys:
                        # Remove the key completely
                        key_to_remove = self.lru_keys[idx]
                        self.lru_keys.remove(key_to_remove)
                        self.lfu_keys.pop(key_to_remove)
                        self.cache_data.pop(key_to_remove)
                        print('DISCARD:', key_to_remove)
                        break

            # Update cache
            self.cache_data[key] = item
            self.lfu_keys[key] = self.lfu_keys.get(key, 0) + 1

            # For LRU tracking:

            # If the key is already in lru_keys, remove it first
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

            # Update number of uses in self.lfu_keys
            self.lfu_keys[key] = self.lfu_keys.get(key, 0) + 1

            # For LRU tracking:

            # Remove old mark in self.lru_keys if it exists
            if key in self.lru_keys:
                self.lru_keys.remove(key)

            # Mark it as recently used
            self.lru_keys.appendleft(key)

        # Return the item or None
        return item
