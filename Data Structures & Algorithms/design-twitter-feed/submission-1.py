import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)      # userId -> [(timestamp, tweetId), ...] most recent last
        self.followees = defaultdict(set)    # userId -> set of userIds they follow

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        # seed with the most recent tweet from self + each followee
        watching = self.followees[userId] | {userId}
        for uid in watching:
            tweets = self.tweets.get(uid)
            if tweets:
                idx = len(tweets) - 1
                ts, tid = tweets[idx]
                heapq.heappush(heap, (-ts, uid, idx))

        res = []
        while heap and len(res) < 10:
            neg_ts, uid, idx = heapq.heappop(heap)
            res.append(self.tweets[uid][idx][1])
            if idx - 1 >= 0:
                ts, tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-ts, uid, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)