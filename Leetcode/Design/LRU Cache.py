'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
            return self.hashMap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, then update so have to move to the end first
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
        # new key:value or update existing key with new value
        self.hashMap[key] = value
        if len(self.hashMap) > self.capacity:
            # Remove the first item
            # By default, LIFO h.popitem(last=True), you can change: FIFO h.popitem(last=False)
            self.hashMap.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
