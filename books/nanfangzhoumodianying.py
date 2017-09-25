#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return nanfangzhoumodianying

class nanfangzhoumodianying(BaseFeedBook):
    title                 = u'南方周末·电影'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'南方周末·电影', 'http://feedmaker.kindle4rss.com/feeds/dianying.infzm.com.xml', True)
           ]