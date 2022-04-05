'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
'''

import random
class RandomizedSet:

    def __init__(self):
        # define a list to store values
        self.lst = []
        # define a hashMap {num : list index}
        self.hashMap = collections.defaultdict(int)

    def insert(self, val: int) -> bool:
        # If the value was in the list, then just return False
        if val in self.lst:
            return False
        # 因为list下标从0开始，所以先hashMap再append val to the list
        # list = [1,2,3], hashMap = {1 : 0, 2: 1, 3: 2 }
        self.hashMap[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        # If lst contains the val, then replace tbe value with the last element in the list
        # Because later you can just do list.pop() to remove the val from the list
        # Update the last element index by using the deleted element index
        last_element = self.lst[-1]
        remove_idx = self.hashMap[val]
        self.lst[remove_idx] = last_element
        self.hashMap[last_element] = remove_idx
        self.lst.pop()
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        '''
        The choice() method returns a randomly selected element from the specified sequence.
        '''
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
