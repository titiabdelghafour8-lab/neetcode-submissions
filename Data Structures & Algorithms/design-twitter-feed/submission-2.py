import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.usersFollows = defaultdict(set)
        self.globalTweets = []
        self.tweetDate = 100001 # incements by one at each new tweet, initialized by the max since heapq uses min heap and we want the most recent tweets so the ones with min tweetDate

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.globalTweets, (self.tweetDate, tweetId, userId))
        self.usersFollows[userId].add(userId)
        self.tweetDate -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tmp_deleted = []
        valid_feed = []
        valid_feed_count = 0
        if not self.globalTweets:
            return []
        while True:
            el = heapq.heappop(self.globalTweets)
            if el[2] in self.usersFollows[userId]:
                valid_feed.append(el[1])
                valid_feed_count += 1
            tmp_deleted.append(el)
            if not self.globalTweets or valid_feed_count == 10:
                while tmp_deleted:
                    heapq.heappush(self.globalTweets, tmp_deleted.pop())
                return valid_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.usersFollows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not self.usersFollows[followerId]:
            return
        self.usersFollows[followerId].remove(followeeId)
