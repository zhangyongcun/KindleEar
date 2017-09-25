#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return uspolitics

class uspolitics(BaseFeedBook):
    title                 = u'US Politics'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'US Politics', 'http://feedmaker.kindle4rss.com/feeds/us-politics.economist.com.xml', True)
           ]