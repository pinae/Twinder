#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from twitter import *
from secret import CONSUMER_KEY, CONSUMER_SECRET

MY_TWITTER_CREDENTIALS = os.path.expanduser('~/.twinder_credentials')
if not os.path.exists(MY_TWITTER_CREDENTIALS):
    oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDENTIALS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDENTIALS)

twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

timeline = twitter.statuses.home_timeline()
for tweet in timeline:
    print(tweet['text'])
