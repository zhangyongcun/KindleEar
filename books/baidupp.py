#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return baidupp

class baidupp(BaseFeedBook):
    title                 = u'百度百家:P2P'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'百度百家:P2P', 'http://feedmaker.kindle4rss.com/feeds/p2p.baijia.baidu.com.xml', True)
           ]