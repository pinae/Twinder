#!/usr/bin/python
# -*- coding: utf-8 -*-

from readers.twitter import TwitterReader


reader = TwitterReader()
data = reader.read()
for item in data:
    print(item['text'])
