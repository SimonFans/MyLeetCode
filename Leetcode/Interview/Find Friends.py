# output = ["steven", "simon", "sam", "avery"]
def findFriendDFS(start, end, connect, temp):
    def dfs(start, end, connect, temp):
        if temp and temp[-1] == end:
            res.append(list(temp))
        if start not in connect:
            return
        for other in connect[start]:
            if other in temp:
                continue
            dfs(other, end, connect, temp + [other])
    res = []
    dfs(start, end, connect, temp)
    return res

start = "steven"
end = "avery"
connect = {"steven":["simon", "jerry"],
           "simon":["sam", "steven"],
           "jerry": ["steven"],
           "sam":['tom', 'avery']}

print('result:', findFriendDFS(start, end, connect, [start]))
