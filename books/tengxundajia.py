#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return tengxundajia

class tengxundajia(BaseFeedBook):
    title                 = u'腾讯·大家'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'腾讯·大家', 'http://feedmaker.kindle4rss.com/feeds/dajia.qq.com.xml', True)
           ]