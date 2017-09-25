#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return bochengzai

class bochengzai(BaseFeedBook):
    title                 = u'喷嚏网-铂程斋'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'喷嚏网-铂程斋', 'http://feedmaker.kindle4rss.com/feeds/xilei.dapenti.com.xml', True)
           ]