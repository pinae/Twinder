#!/usr/bin/python
# -*- coding: utf-8 -*-

from readers.basic import BasicReader
import os
from twitter import *
from secret import CONSUMER_KEY, CONSUMER_SECRET

MY_TWITTER_CREDENTIALS = os.path.expanduser('~/.twinder/twitter_credentials')


class TwitterReader(BasicReader):
    def __init__(self):
        if not os.path.exists(MY_TWITTER_CREDENTIALS):
            oauth_dance("Twinder Tweetsorter", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDENTIALS)
        oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDENTIALS)
        self.twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))
        self.last_known_tweet = None

    def read(self):
        timeline = self.twitter.statuses.home_timeline()
        text_list = []
        for tweet in timeline:
            if self.last_known_tweet and tweet['id'] == self.last_known_tweet:
                break
            text_list.append({
                'id': tweet['id'],
                'text': tweet['text']
            })
        if len(text_list) > 0:
            self.last_known_tweet = text_list[0]['id']
        return text_list
