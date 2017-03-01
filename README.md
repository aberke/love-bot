l0V3 Bot
--

https://twitter.com/lovebot_2000

People use technology to find love.  With Grindr, Tinder, Bumble, people are relentlessly swiping away the days.  These apps connect people in a common geographic location, all desperately looking for love.  As technologists it is duty to make this more efficient.

Love Bot 2000 is disrupting dating and automating the creation of lifelong connections via the twittersphere.  It crawls the tweets of celebrities like Neil Degrasse Tyson, finds people that retweeted their same tweet and are geographically near each other, and then relentlessly tweets intros @ these potential soul mates.  This bot instigates love for people, regardless of whether they're searching for it, separated in age by 50 years, or are in commited relationships.

This is love in the digital age.


Success Story
---

<img width="600px" src="https://raw.githubusercontent.com/aberke/love-bot/master/static/love-connection-screenshot.png" />


User Testimonials
----


```
"It was love at first follow"
```  
   -- Neil deGrasse Tyson fan and retweeter


```
"She followed me, then I followed her, we tweeted @ each other and then DMed...
it was history from there..."
```
   -- Science enthuiast and Bill Nye retweeter




Do you have an ideas for great intro lines or celebs whose tweets can inspire love?
-------

Let us know!

* Email an idea to alex@aberke.com
OR
* Make a PR [here](https://github.com/aberke/love-bot/blob/master/bot/celeb_data.py)



Are other pull requests welcome?
-----

Yes Please


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




Made with <3 @ the 2017 Stupid Hackathon in NYC.
