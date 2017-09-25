#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return nanfzhoumo

class nanfzhoumo(BaseFeedBook):
    title                 = u'南方周末'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'南方周末', 'http://feedmaker.kindle4rss.com/feeds/hot.infzm.com.xml', True)
           ]