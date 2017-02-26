l0V3 Bot
--

https://twitter.com/lovebot_2000

People use technology to find love.  With Grindr, Tinder, Bumble, people relentlessly swiping away the days.  These apps connect people in a common geographic location, all desperately looking for love.  As technologists it is duty to make this more efficient.

Love Bot 2000 automates the creation of lifelong connections via the twittersphere for users.  
It connects people who are near eachother and like Neil Degrasse Tyson ...(or other celebrities) by crawling their tweets and relentless tweeting intros @ potential soul males who have retweeted the same tweet and are geographically close.  This bot instigates love for people, regardless of whether they're searching for it, separated in age by 50 years, or are in commited relationships.

This is love in the digital age.

Running Locally
---

* Create a virutual environment so that the following installations do not cause conflicts.  Make sure to reactivate this virtual environment each time you want to run the server locally.  All the following installations will be isolated in this environment.
```
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
```
* Install python dependencies ```$ pip install -r requirements.txt```

export twitter API keys into environment:
```
export TWITTER_API_CONSUMER_KEY=""
export TWITTER_API_CONSUMER_SECRET=""

export TWITTER_API_ACCESS_TOKEN=""
export TWITTER_API_ACCESS_TOKEN_SECRET=""
```

```
$ python runner.py
```
