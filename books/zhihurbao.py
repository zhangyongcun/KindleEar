#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return zhihurbao

class zhihurbao(BaseFeedBook):
    title                 = u'知乎日报'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'知乎日报', 'http://feedmaker.kindle4rss.com/feeds/zhihu-daily.xml', True)
           ]