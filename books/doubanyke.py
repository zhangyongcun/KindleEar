#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return doubanyke

class doubanyke(BaseFeedBook):
    title                 = u'豆瓣一刻'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'豆瓣一刻', 'http://feedmaker.kindle4rss.com/feeds/douban_yike.xml', True)
           ]