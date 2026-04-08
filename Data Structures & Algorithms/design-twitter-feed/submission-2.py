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
        users = self.follow_map[userId] | {userId}
        tweets = [tweet for u in users for tweet in self.tweets[u][-10:]]
        return [t for _, t in heapq.nsmallest(10, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)