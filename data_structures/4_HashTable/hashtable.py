class HashTable:
    def __init__(self):
        self.capacity = 8  # initial capacity
        self.size = 0  # number of key-value pairs
        self.buckets = [[] for _ in range(self.capacity)]

    def hashing(self, key):
        """Basic hashing function"""
        unicode_points = 0
        for char in key:
            unicode_points += ord(char)
        return unicode_points % self.capacity

    def resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0  # reset size, will be updated in insert
        # rehashing & copy the old array into new array
        for bucket in old_buckets:
            for k, _ in bucket:
                self.insert(k, _)

    def insert(self, key, value):
        """Insert a key-value pair into hash table"""
        if self.size / self.capacity >= 0.8:  # resize when 80% full
            self.resize()

        hash_code = self.hashing(key)
        retrieved_bucket = self.buckets[hash_code]  # might be a linked list
        for i, (k, _) in enumerate(retrieved_bucket):
            # enumerate is to look thru each key_value pair with its corr. index
            if k == key:
                retrieved_bucket[i] = (key, value)
                break
        else:
            retrieved_bucket.append((key, value))
            self.size += 1  # bucket array size += 1 as a new hashCode is inserted into the bucket

    def get(self, key):
        hash_code = self.hashing(key)
        retrieved_bucket = self.buckets[hash_code]
        for k, v in retrieved_bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_code = self.hashing(key)
        retrieved_bucket = self.buckets[hash_code]
        for i, (k, _) in enumerate(retrieved_bucket):
            if k == key:
                del retrieved_bucket[i]
                self.size -= 1
                return

    def print_hash(self):
        hashTable = "{"
        for i, bucket in enumerate(self.buckets):
            # if bucket:  # only add non-empty buckets
            hashTable += f" {i}: {bucket}, "
        hashTable = hashTable.rstrip(", ") + " }"  # remove last comma
        return hashTable


if __name__ == '__main__':
    h = HashTable()
    with open("stock_prices.csv", "r") as f:
        for line in f:
            tokens = line.split(',')
            key = tokens[0]
            value = float(tokens[1])
            h.insert(key, value)

    print(h.capacity)
    print(h.size)
    h.insert('march 9', float(999))
    h.delete('march 9')
    print(h.capacity)
    print(h.size)
    h.insert('march 1', float(111))
    h.insert('march 2', float(222))
    h.insert('march 3', float(333))
    print(h.capacity)
    print(h.size)
    print(h.print_hash())
