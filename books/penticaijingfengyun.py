#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return penticaijingfengyun

class penticaijingfengyun(BaseFeedBook):
    title                 = u'喷嚏网-财经风云'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'喷嚏网-财经风云', 'http://feedmaker.kindle4rss.com/feeds/caijing.dapenti.com.xml', True)
           ]