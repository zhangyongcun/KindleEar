#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return baiduyule

class baiduyule(BaseFeedBook):
    title                 = u'百度百家:娱乐'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'百度百家:娱乐', 'http://feedmaker.kindle4rss.com/feeds/entertainment.baijia.baidu.com.xml', True)
           ]