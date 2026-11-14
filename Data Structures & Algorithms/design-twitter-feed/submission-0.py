class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = collections.defaultdict(list)
        self.following = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        recent = []
        user = self.following[userId] | {userId}
        for u in user:
            recent.extend(self.tweet[u][-10:])
        recent.sort(reverse = True)
        res = []
        for t, tweetId in recent[:10]:
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
