#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wenyixincufang

class wenyixincufang(BaseFeedBook):
    title                 = u'文怡心厨房'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'文怡心厨房', 'http://blog.sina.com.cn/rss/wenyi.xml', True)
           ]