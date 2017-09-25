#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return newyorkerculture

class newyorkerculture(BaseFeedBook):
    title                 = u'New Yorker: Culture'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'New Yorker: Culture', 'http://feedmaker.kindle4rss.com/feeds/culture.newyorker.com.xml', True)
           ]