#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return zhongguorbaozixun

class zhongguorbaozixun(BaseFeedBook):
    title                 = u'中国日报: 资讯'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'中国日报: 资讯', 'http://feedmaker.kindle4rss.com/feeds/world.chinadaily.xml', True)
           ]