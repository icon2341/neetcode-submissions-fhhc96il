import heapq

class Twitter:

    def __init__(self):
        self.follow_map = {}
        self.tweet_map = {}
        self.tweet_counter = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if(userId in self.tweet_map):
            self.tweet_map[userId].add((-self.tweet_counter, tweetId))
            self.tweet_counter +=1
        else:
            self.tweet_map[userId] = set()
            self.tweet_map[userId].add((-self.tweet_counter, tweetId))
            self.tweet_counter +=1    
        if(userId not in self.follow_map):
              self.follow_map[userId] = set()

    def getNewsFeed(self, userId: int) -> List[int]:
        # loop through all followees of follower and get all their tweets in an array
        if userId in self.follow_map:
            tweets = []
            followed_users = self.follow_map[userId]
            followed_users.add(userId)
            for followed_user in followed_users:
                if(followed_user in self.tweet_map):
                    for tweet in self.tweet_map[followed_user]:
                        heapq.heappush(tweets, tweet)
                else: continue

            print("USER: ", userId)
            print("FOLLOWS: ", self.follow_map[userId])
            print("TWEET MAP: ", self.tweet_map)

            # pop 10 tweets
            k = 0 
            output =[]
            while k < 10 and tweets:
                output.append(heapq.heappop(tweets)[1])
                k+=1


            print("OUTPUT: ", output)
            return output
        else:
            return []
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if(followerId in self.follow_map):
            self.follow_map[followerId].add(followeeId)
        else:
            self.follow_map[followerId] = set()
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId in self.follow_map):
            if(followeeId in self.follow_map[followerId]):
                self.follow_map[followerId].remove(followeeId)
        else:
            pass
        
