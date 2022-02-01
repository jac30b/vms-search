import math


class Key:
    def __init__(self, key):
        self.key = key

    def getHash(self, maxSize):
        hash = 0
        R = 64
        for i, char in enumerate(self.key):
            hash = (R * hash + i) % maxSize
        return hash

    def get(self):
        return self.key


class Value:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


class Hash:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.keys = [None] * maxSize
        self.values = [None] * maxSize

    def __hash(self, key):
        return (key.getHash(self.maxSize) & 0x7FFFFFFF) % self.maxSize

    def __resize(self, size):
        tmp = Hash(size)
        for i in range(0, self.maxSize):
            if self.keys[i]:
                tmp.insert(self.keys[i].get(), self.values[i].get())
        self.keys = tmp.keys
        self.values = tmp.values
        self.maxSize = tmp.maxSize

    def insert(self, key, value):
        key = Key(key)
        value = Value(value)
        if self.size >= self.maxSize / 2:
            self.__resize(2 * self.maxSize)

        index = self.__hash(key)
        while True:
            if not self.keys[index]:
                break
            if self.keys[index].get() == key.get():
                self.values[index] = value
                return False
            index = (index + 1) % self.maxSize

        self.keys[index] = key
        self.values[index] = value
        self.size += 1
        return True

    def get(self, key):
        key = Key(key)
        index = self.__hash(key)
        while True:
            if not self.keys[index]:
                return False
            if self.keys[index].get() == key.get():
                return self.values[index].get()
            index = (index + 1) % self.maxSize

    def __exists(self, key):
        for v in self.keys:
            if v and v.get() == key.get():
                return True
        return False

    def remove(self, key):
        key = Key(key)
        if not self.__exists(key):
            return True
        index = self.__hash(key)
        while not key.get() == self.keys[index].get():
            index = (index + 1) % self.maxSize

        self.keys[index] = None
        self.values[index] = None

        index = (index + 1) % self.maxSize
        while self.keys[index]:
            keyToRestore = self.keys[index]
            valueToRestore = self.values[index]
            self.keys[index] = None
            self.values[index] = None
            self.size -= 1
            self.insert(keyToRestore.get(), valueToRestore.get())
            index = (index + 1) % self.maxSize

        self.size -= 1
        if self.size > 0 and self.size == self.maxSize / 8:
            self.__resize(math.floor(self.maxSize / 2))

        return True
