#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return bbczhongguo

class bbczhongguo(BaseFeedBook):
    title                 = u'BBC 中国'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'BBC 中国', 'http://feedmaker.kindle4rss.com/feeds/cn-bbc.xml', True)
           ]