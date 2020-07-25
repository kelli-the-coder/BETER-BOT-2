import tweepy
import os

test_acc_username = "Testacc81222228"
kelli_acc_id = "1049519637774458881"
trump_acc_id = "25073877"
beter_acc_id = "1284250618815754247"
test_acc_id = "1284999496011862017"
elon_musk_id = "44196397"
barack_obama_id = "813286"
joe_biden_id = "939091"
hillary_clinton_id = "1339835893"
caucasian_james_id = "272985460"
lil_nas_x_id = "754006735468261376"



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
  def __init__(self, api, limit=0):
    self.tweet_count = 0
    self.tweet_limit = limit
    self.reply_to_list = ["realDonaldTrump", "kawaiiouran", test_acc_username, "elonmusk", "JoeBiden", "HillaryClinton", "BarackObama", "CaucasianJames", "LilNasX"]
    super().__init__(api)

  def on_status(self, status):
    # this first part gets the tweet and sets the text to tweet_text, whether or not it was someone in the self.reply_to_list or not
    if hasattr(status, "retweeted_status"):#this checks if its a retweet
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
    if status.user.screen_name in self.reply_to_list or '@BETERBIFFIN2' in tweet_text:
      print(f"Username: {status.user.screen_name}")
      print(f"Tweet: {tweet_text}")
      print(f"Tweet_ID: {status.id_str}")

    if status.user.screen_name in self.reply_to_list:
      if status.user.screen_name == "kawaiiouran":
        api.update_status(status=f"@kawaiiouran Kelli you are so cool and also awesome {random.randint(1, 100000)}",in_reply_to_status_id=status.id_str)
        print("replied to kawaii ouran")
      elif status.user.screen_name == "realDonaldTrump":
        api.update_status(status=f"@realDonaldTrump pee pee poo poo {random.randint(1, 100000)}", in_reply_to_status_id=status.id_str)
        print("replied to realDonaldTrump")
      elif status.user.screen_name == test_acc_username:
        api.update_status(status=f"@Testacc81222228 Whats up my broski???? {random.randint(1, 100000)}", in_reply_to_status_id = status.id_str)
        print("Replied to test acc")
      elif status.user.screen_name == "elonmusk":
        api.update_status(status=f"@elonmusk Can I get a free Tesla? {random.randint(1, 100000)}", in_reply_to_status_id=status.id_str)
        print("replied to elon musk")
      elif status.user.screen_name == "BarackObama":
        api.update_status(status=f"@BarackObama Is your favorite vegetable barack-oli? {random.randint(1, 100000)}", in_reply_to_status_id=status.id_str)
        print("replied to Barack Obama")
      else:
        api.update_status(status=f"@{status.user.screen_name} pee pee poo poo {random.randint(1, 100000)}", in_reply_to_status_id=status.id_str)
        print(f"replied to {status.user.screen_name}")

    else:
      if '@BETERBIFFIN2' in tweet_text:
        print(f"@{status.user.screen_name} has @ed you /n their tweet says {tweet_text}")
        api.update_status(status=f"@{status.user.screen_name} WHO HAS SUMMONED ME {random.randint(1, 100000)}", in_reply_to_status_id=status.id_str)
        print(f"replied to @{status.user.screen_name}")

    return self.tweet_count != self.tweet_limit
    
#this checks if connection to Api was successfull so it will go first because it will go when the api is connected which is before on_status
  def on_connect(self):
    print("Connected to API successfully")


tweet_listener = TweetListener(api)
tweet_stream = tweepy.Stream(auth=api.auth, listener=tweet_listener)
tweet_stream.filter(track = ["@BETERBIFFIN2"], follow = [kelli_acc_id, trump_acc_id, test_acc_id, elon_musk_id, barack_obama_id, joe_biden_id, hillary_clinton_id, caucasian_james_id, lil_nas_x_id], is_async=True)
