#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return newyorkerhumor

class newyorkerhumor(BaseFeedBook):
    title                 = u'New Yorker: Humor'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'New Yorker: Humor', 'http://feedmaker.kindle4rss.com/feeds/humor.newyorker.com.xml', True)
           ]