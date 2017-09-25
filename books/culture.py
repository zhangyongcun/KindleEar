#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return culture

class culture(BaseFeedBook):
    title                 = u'Culture'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Culture', 'http://feedmaker.kindle4rss.com/feeds/culture.economist.com.xml', True)
           ]