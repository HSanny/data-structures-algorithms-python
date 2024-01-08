class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class HashTable:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def hashing(self, key):
        char_count = 0
        for char in key:
            char_count += ord(char)
        return char_count & self.capacity

    def resizing(self):
        old_bucket = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_bucket:
            for k, _ in bucket:
                self.insert(k, _)

    def insert(self, key, value):
        if self.size / self.capacity >= 0.7:
            self.resizing()

        hash_code = self.hashing(key)
        retrieved_bucket = self.buckets[hash_code]
        for i, (k, _) in enumerate(retrieved_bucket):
            if k == key:
                retrieved_bucket[i] = (key, value)
                break
        else:
            retrieved_bucket.append((key, value))
            self.size += 1
            return

    def delete(self, key):
        if self.size == 0:
            raise Exception("The hash table is empty!")

        hash_code = self.hashing(key)
        retrieved_bucket = self.buckets[hash_code]
        for i, (k, _) in retrieved_bucket:
            if k == key:
                del retrieved_bucket[i]
                self.size -= 1
                return

    def get(self, key):
        hash_code = self.hashing(key)
        retrieved_bucket = self.buckets[hash_code]
        for k, _ in retrieved_bucket:
            if k == key:
                return _
        return None

    def print_hash(self):
        return
