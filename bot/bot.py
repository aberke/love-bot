import os
import random
import time

import tweepy

from bot import twitter_util
from bot.celeb_data import CELEB_DATA


TWITTER_API_CONSUMER_KEY = os.environ["TWITTER_API_CONSUMER_KEY"]
TWITTER_API_CONSUMER_SECRET = os.environ["TWITTER_API_CONSUMER_SECRET"]
TWITTER_API_ACCESS_TOKEN = os.environ["TWITTER_API_ACCESS_TOKEN"]
TWITTER_API_ACCESS_TOKEN_SECRET = os.environ["TWITTER_API_ACCESS_TOKEN_SECRET"]

MAX_LOVE_TWEETS_PER_TWEET = 10
SECONDS_DELAY_BETWEEN_TWEETS = 5*60
# Filter out tweets that are older than this
HOURS_RECENT = 24

TWEET_TEMPLATES_KEY = "tweet_templates"


class LoveBot:

    def __init__(self):
        self.api = self.get_api_connection()


    def get_api_connection(self):
        auth = tweepy.OAuthHandler(TWITTER_API_CONSUMER_KEY, TWITTER_API_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_API_ACCESS_TOKEN, TWITTER_API_ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)


    def handle_celebrity(self, celeb_username, hours_recent=HOURS_RECENT):
        """ Handle celeb tweets made in the last 'hours_recent' hours """
        if not (celeb_username in CELEB_DATA and
                (TWEET_TEMPLATES_KEY in CELEB_DATA[celeb_username])):
                print("Error: No user data for {}".format(celeb_username))
                return

        tweet_templates = CELEB_DATA[celeb_username][TWEET_TEMPLATES_KEY]

        tweets = self.get_filtered_tweets(celeb_username, hours_recent)
        print("@{}: handling {} tweets".format(celeb_username, len(tweets)))

        for tweet_index, tweet in enumerate(tweets):
            tweet_url = twitter_util.get_tweet_url(celeb_username, tweet)
            # Get list of tuples of screen names to tweet at
            lover_pairs = self.get_retweet_lover_pairs(tweet)
            # shorten the list of lover_pairs to avoid overtweeting
            lover_pairs = lover_pairs[:MAX_LOVE_TWEETS_PER_TWEET]
            print("@{}, {}: handling {} lover pairs for tweet: {}".format(
                  celeb_username, tweet_index, len(lover_pairs), tweet.text))

            for (lover_username1, lover_username2) in lover_pairs:
                # Tweet @ them
                tweet_template = random.choice(tweet_templates)
                tweet_text = tweet_template.format(
                    lover_username1=lover_username1,
                    lover_username2=lover_username2,
                    tweet_url=tweet_url,
                )
                # TODO: catch errors
                print("@{}, {}: tweeting @ lovers {} & {}".format(
                      celeb_username, tweet_index, lover_username1,
                      lover_username2))
                self.api.update_status(tweet_text)
                # Space out tweets
                print("@{}, {}: successfully tweeted. Sleeping {}s".format(
                      celeb_username, tweet_index,
                      SECONDS_DELAY_BETWEEN_TWEETS))
                time.sleep(SECONDS_DELAY_BETWEEN_TWEETS)


    def get_retweet_lover_pairs(self, tweet):
        # Get as many retweets as we can (max count=100)
        retweets = self.api.retweets(tweet.id, count=100)
        # Get list of tuples of screen names to tweet at
        return self.pair_retweeters(retweets)


    def pair_retweeters(self, retweets):
        """
        Returns [(string: lover1, string: lover2)] list of screen_name pairs.
        """
        # Map {timezone: [User.screen_name, ...]}
        screen_names_by_time_zone = {}
        for r in retweets:
            user = r.user
            screen_name = user.screen_name
            time_zone = user.time_zone
            if time_zone in screen_names_by_time_zone:
                screen_names_by_time_zone[time_zone].append(screen_name)
            else:
                screen_names_by_time_zone[time_zone] = [screen_name]

        # Attempt to pair people by timezones
        lover_pairs = []  # List of 2-tuples
        for time_zone, screen_name_list in screen_names_by_time_zone.items():
            i = 0
            while i < len(screen_name_list):
                lover1 = screen_name_list[i]
                if (i + 1) < len(screen_name_list):
                    lover2 = screen_name_list[i + 1]
                    lover_pair = (lover1, lover2)
                    lover_pairs.append(lover_pair)
                i += 2
        return lover_pairs


    def get_filtered_tweets(self, celeb_username, hours_recent):
        """
        Returns [Tweet] filtered list of celeb tweets.

        Filters out retweets & tweets made more than 'recent_hours' ago.
        """
        tweets = self.api.user_timeline(celeb_username, count=50)
        # Filter out old tweets
        tweets = [t for t in tweets if twitter_util.is_recent_tweet(t, hours_recent)]
        # Filter out retweets -- only use originals
        tweets = [t for t in tweets if not twitter_util.is_retweet(t)]
        return tweets
