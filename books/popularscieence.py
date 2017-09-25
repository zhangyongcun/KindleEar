#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return popularscieence

class popularscieence(BaseFeedBook):
    title                 = u'Popular Science'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Popular Science', 'http://www.popsci.com/rss.xml', True)
           ]