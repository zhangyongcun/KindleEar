#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return xueqiu

class xueqiu(BaseFeedBook):
    title                 = u'今日话题 - 雪球'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'今日话题 - 雪球', 'http://feedmaker.kindle4rss.com/feeds/hot.xueqiu.com.xml', True)
           ]