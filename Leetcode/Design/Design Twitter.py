'''
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]
'''

思路： 题目要求输入用户ID，返回最近的他或者她关注的tweet用户发的10条tweets。
这题需要建立两个字典，一个{user_id, [(sent_tweets_time,  user_id, accumulative_tweets)].
另一个字典存用户和他follow哪些user的信息{user_id: set(followee_id...)}.
创建一个maxHeap list 和一个result list。从当前user对应的list中找出最后一条tweet放入maxHeap,
再遍历当前user follow的其他user，并把他们发的最后一条tweet放入maxHeap. 用while loop拿出最近的tweet ID，
拿出后在push进去当前拿出的user的最后一条tweet到axHeap直到拿出的tweets等于10或者maxHeap为空时退出。

import collections
import heapq
class Twitter:
    def __init__(self):
        self.time = 0
        # used for heap later. {'user_id':[(time, tweets_id)]}
        self.messages = collections.defaultdict(list)
        # following set
        self.following = collections.defaultdict(set)
        # Given by question
        self.__number_of_most_recent_tweets = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.messages[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # use heapq
        # maxHeap: (-1* most recent time, userId, # of tweers current userId had)
        maxHeap = []
        # save returned tweetsId
        result = []
        # 如果当前user发过tweets，则压入当前user最后一条发送的tweets时间, 最后的0记录当前读了多少条tweets，倒着读
        if self.messages[userId]:
            heapq.heappush(maxHeap, (-self.messages[userId][-1][0], userId, 0))
        # 找出当前user follow了哪些users
        for uid in self.following[userId]:
            # 如果当前userfollow的那些users也发了tweets
            if self.messages[uid]:
                heapq.heappush(maxHeap, (-self.messages[uid][-1][0], uid, 0))
        # 查找最近的10条tweets
        while maxHeap and len(result) < self.__number_of_most_recent_tweets:
            _time, _uid, _curr = heapq.heappop(maxHeap)
            _next = _curr + 1
            if _next < len(self.messages[_uid]):
                heapq.heappush(maxHeap, (-self.messages[_uid][-(_next+1)][0], _uid, _next))
            # append当前时间最近的user_id对应的tweets
            result.append(self.messages[_uid][-(_curr+1)][1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
