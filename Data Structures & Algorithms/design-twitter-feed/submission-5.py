class Twitter:

    def __init__(self):
        self.feeds = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)
        #self.followee = collections.defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        #Add the tweetId into User's feed
        self.feeds[userId].append([tweetId, self.time])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feedsSeq = []
        for feed, time in self.feeds[userId]:
            heapq.heappush(feedsSeq, (-time, feed))
        for follower in self.followers[userId]:
            for feed, time in self.feeds[follower]:
                heapq.heappush(feedsSeq, (-time, feed))
        feeds = []
        while feedsSeq and len(feeds) < 10:
            _, tweetId = heapq.heappop(feedsSeq)
            feeds.append(tweetId)
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        #ex: User 1 follows User 2
        #Append User 2 into the User 1'follower list
        #Append User 1 into the User 2' followee list
        if followerId != followeeId:
            self.followers[followerId].add(followeeId) 
        #self.followee[followeeId].add(followerId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId) 
        #self.followee[followeeId].remove(followerId) 



