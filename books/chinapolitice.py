#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return chinapolitice

class chinapolitice(BaseFeedBook):
    title                 = u'China Politics'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'China Politics', 'http://feedmaker.kindle4rss.com/feeds/china-politics.economist.com.xml', True)
           ]