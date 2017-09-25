#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return baidudianshang

class baidudianshang(BaseFeedBook):
    title                 = u'百度百家:电商'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'百度百家:电商', 'http://feedmaker.kindle4rss.com/feeds/dianshang.baijia.baidu.com.xml', True)
           ]