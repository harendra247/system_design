#!/usr/bin/env python3


from collections import OrderedDict

'''
Assumptions
We are caching the results of web queries.
Inputs are valid or no validation required.
This fits in memory.
'''

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        else:
            self.cache.pop(key)
        self.cache[key] = value

    def remove(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.pop(key)
            return key
