class Twitter:

    def __init__(self):
        self.feeds = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)
        #self.followee = collections.defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        #Add the tweetId into User's feed
        self.feeds[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId]
        followers.add(userId)
        feedsHeap = []
        for follower in followers:
            if follower in self.feeds:
                index = len(self.feeds[follower]) - 1
                time, tweetId = self.feeds[follower][index]
                heapq.heappush(feedsHeap, (time, tweetId, follower, index - 1))
            
        feeds = []
        while feedsHeap and len(feeds) < 10:
            time, tweetId, follower, index = heapq.heappop(feedsHeap)
            feeds.append(tweetId)
            if index >= 0:
                time, tweetId = self.feeds[follower][index]
                heapq.heappush(feedsHeap, (time, tweetId, follower, index - 1))
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        #ex: User 1 follows User 2
        #Append User 2 into the User 1'follower list
        #Append User 1 into the User 2' followee list
        self.followers[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId) 



