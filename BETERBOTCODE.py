import tweepy
import os

test_acc_username = "Testacc81222228"

kelli_acc_id = "1049519637774458881"
trump_acc_id = "25073877"
beter_acc_id = "1284250618815754247"
test_acc_id = "1284999496011862017"
# status means tweet

auth = tweepy.OAuthHandler(os.environ["ApiKey"], os.environ["ApiSecretKey"])

auth.set_access_token(os.environ["AccessToken"], os.environ["AccessTokenSecret"])

api = tweepy.API(auth)

"""
#followers are ppl who follow that acc, "friends" is ppl who that acc follows
Kelli = api.get_user("kawaiiouran")
print(Kelli.screen_name)
print(Kelli.followers_count)
for follower in Kelli.followers():
  print(follower.screen_name)

#this gets all the tweets on trump's profile and prints them

Trump = api.get_user("realDonaldTrump")
for status in tweepy.Cursor(api.user_timeline, id="realDonaldTrump").items(5):
  print(status.text)
  print("\n")


#this gets the latest tweet from the Kelli account
#KellisTweet = Kelli.status.text

#print(KellisTweet)

"""


class TweetListener(tweepy.StreamListener):
    def __init__(self, api, limit=5):
        self.tweet_count = 0
        self.tweet_limit = limit
        self.reply_to_list = ["realDonaldTrump", "kawaiiouran", test_acc_username, "elonmusk", "JoeBiden",
                              "HillaryClinton", "BarackObama", "CaucasianJames", "LilNasX"]
        super().__init__(api)

    def on_status(self, status):
        if status.user.screen_name in self.reply_to_list:
            if hasattr(status, "retweeted_status"):  # this checks if its a retweet
                try:
                    tweet_text = status.retweeted_status.extended_tweet["full_text"]
                    self.tweet_count += 1
                except AttributeError:
                    tweet_text = status.retweeted_status.text
                    self.tweet_count += 1
            else:
                try:
                    tweet_text = status.extended_tweet["full_text"]
                    self.tweet_count += 1
                except AttributeError:
                    tweet_text = status.text
                    self.tweet_count += 1

            print(f"Username: {status.user.screen_name}")
            print(f"Tweet: {tweet_text}")
            print(f"Tweet_ID: {status.id_str}")

            if status.user.screen_name == "kawaiiouran":
                api.update_status(status="@kawaiiouran Kelli you are so cool and also awesome",
                                  in_reply_to_status_id=status.id_str)
                print("replied to kawaii ouran")
            elif status.user.screen_name == "realDonaldTrump":
                api.update_status(status="@realDonaldTrump pee pee poo poo", in_reply_to_status_id=status.id_str)
                print("replied to realDonaldTrump")
            elif status.user.screen_name == test_acc_username:
                api.update_status(status="@Testacc81222228 Whats up my broski????", in_reply_to_status_id=status.id_str)
                print("Replied to test acc")
            elif status.user.screen_name == "elonmusk":
                api.update_status(status="@elonmusk Can I get a free Tesla?", in_reply_to_status_id=status.id_str)
                print("replied to elon musk")
            elif status.user.screen_name == "BarackObama":
                api.update_status(status="@BarackObama Is your favorite vegetable barack-oli?",
                                  in_reply_to_status_id=status.id_str)
                print("replied to Barack Obama")
            else:
                api.update_status(status=f"@{status.user.screen_name} pee pee poo poo",
                                  in_reply_to_status_id=status.id_str)
                print(f"replied to {status.user.screen_name}")

        return self.tweet_count != self.tweet_limit

    # this checks if connection to Api was successfull so it will go first because it will go when the api is connected which is before on_status
    def on_connect(self):
        print("Connected to API successfully")


tweet_listener = TweetListener(api)
tweet_stream = tweepy.Stream(auth=api.auth, listener=tweet_listener)
tweet_stream.filter(follow=[kelli_acc_id, trump_acc_id, test_acc_id], is_async=True)
