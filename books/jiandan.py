#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return jiandan

class jiandan(BaseFeedBook):
    title                 = u'煎蛋'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'煎蛋', 'http://feedmaker.kindle4rss.com/feeds/jiandan.net.xml', True)
           ]