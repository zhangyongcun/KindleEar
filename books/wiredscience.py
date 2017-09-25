#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wiredscience

class wiredscience(BaseFeedBook):
    title                 = u'WIRED / Science'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'WIRED / Science', 'http://feedmaker.kindle4rss.com/feeds/science.wired.xml', True)
           ]