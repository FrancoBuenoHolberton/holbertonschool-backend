#!/usr/bin/python3
""" asdaspdsapap asdasdasdal"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ caching system sadsadas"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if item is None or key is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ get a key by item asdasdasdsa"""
        return self.cache_data.get(key)
