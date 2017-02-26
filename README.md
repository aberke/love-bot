



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
