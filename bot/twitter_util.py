""" Utility functions for working with Twitter API """

from datetime import datetime, timedelta


def get_tweet_url(username, tweet):
    """ Returns (str) full URL for tweet """
    return "https://twitter.com/{username}/status/{id}".format(
            username=username,
            id=tweet.id
        )


def is_retweet(tweet):
    """ Returns True if this tweet should be considered a direct retweet """
    try:
        # Only retweets have this attribute
        tweet.retweeted_status.text
        return True
    except AttributeError:
        return False


def is_recent_tweet(tweet, hours_recent):
    """ Returns True if tweet was created within 'hours_recent' hours """
    time_difference = datetime.utcnow() - tweet.created_at
    return time_difference < timedelta(hours=hours_recent)
