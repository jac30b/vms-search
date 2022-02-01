from common.hashmap import Hash
from common.ddl import DLList


class Cache:
<<<<<<< Updated upstream
    pass
=======
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = Hash(capacity)
        self.dlist = DLList()
        self.size = 0

    def put(self, key, value):
        lookup = self.hash.get(key)
        if not lookup:
            # cache miss
            if self.size < self.capacity:
                self.hash.insert(key, self.dlist.push_back(key, value))
                self.size += 1
            else:
                todelete = self.dlist.pop_front()
                self.hash.remove(todelete.key)
                self.hash.insert(key, self.dlist.push_back(key, value))
        else:
            # cache hit
            self.dlist.pop_node(lookup)
            self.hash.insert(key, self.dlist.push_back(key, value))

    def get(self, key):
        lookup = self.hash.get(key)
        if not lookup:
            return -1
        else:
            self.dlist.pop_node(lookup)
            self.dlist.push_back(lookup.key, lookup.value)
            return lookup.value
>>>>>>> Stashed changes
