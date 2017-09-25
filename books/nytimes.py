#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return nytimes

class nytimes(BaseFeedBook):
    title                 = u'NYTimes'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'NYTimes', 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', True)
           ]