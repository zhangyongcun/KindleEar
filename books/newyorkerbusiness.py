#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return newyorkerbusiness

class newyorkerbusiness(BaseFeedBook):
    title                 = u'New Yorker: Business'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'New Yorker: Business', 'http://feedmaker.kindle4rss.com/feeds/business.newyorker.com.xml', True)
           ]