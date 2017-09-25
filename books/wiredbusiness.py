#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wiredbusiness

class wiredbusiness(BaseFeedBook):
    title                 = u'WIRED / Business'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'WIRED / Business', 'http://feedmaker.kindle4rss.com/feeds/business.wired.xml', True)
           ]