#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return buzzfeed

class buzzfeed(BaseFeedBook):
    title                 = u'BuzzFeed'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'BuzzFeed', 'http://www.buzzfeed.com/index.xml', True)
           ]