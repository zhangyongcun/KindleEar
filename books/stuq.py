#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return stuq

class stuq(BaseFeedBook):
    title                 = u'StuQ'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'StuQ', 'http://feedmaker.kindle4rss.com/feeds/stuq2015.weixin.xml', True)
           ]