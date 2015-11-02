#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from twitter import *

CONSUMER_KEY = "XUX6xQN0IK0V5kUNXEtllvKpb"
CONSUMER_SECRET = ""

MY_TWITTER_CREDS = os.path.expanduser('~/.twinder_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

twitter = Twitter(auth=OAuth(
    oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))