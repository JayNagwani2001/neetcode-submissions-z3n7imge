import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1   # decreasing so recent = smaller

    def getNewsFeed(self, userId: int):
        heap = []

        # include self + followees
        users = self.follow_map[userId] | {userId}

        for u in users:
            for tweet in self.tweets[u][-10:]:  # last 10 only
                heapq.heappush(heap, tweet)

        return [tweetId for _, tweetId in heapq.nsmallest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)