#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return huaerjieyingwen

class huaerjieyingwen(BaseFeedBook):
    title                 = u'华尔街英语'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'华尔街英语', 'http://feedmaker.kindle4rss.com/feeds/WSE_China.weixin.xml', True)
           ]