'''
Design two methods
    bool createPath(string path, int value)
Creates a new path and associates a value to it if possible and returns true.
Returns false if the path already exists or its parent path doesn't exist.

    int get(string path)
Returns the value associated with path or returns -1 if the path doesn't exist.

Input:
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]

Output:
[null,true,1]

Explanation:
FileSystem fileSystem = new FileSystem();
fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1

Input:
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output:
[null,true,true,2,false,-1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
'''

class FileSystem:

    def __init__(self):
        self.paths = defaultdict(int)

    def createPath(self, path: str, value: int) -> bool:
        if path == '/' or not path or path in self.paths:
            return False
        # given the current input path, get its parent path
        # it may not have parent path, such as '/c' => ''
        # otherwise parent path such as '/c/a' => '/c'
        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.paths:
            return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths[path] if path in self.paths else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# Time: O(M) where M is the length of path. We spend O(M) on finding the last '/'
# of the path then O(M) to obtain the parent string
# Space: O(K) where k is the number of unique paths we add
