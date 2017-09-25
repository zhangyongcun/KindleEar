#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wireddesign

class wireddesign(BaseFeedBook):
    title                 = u'WIRED / Design'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'WIRED / Design', 'http://feedmaker.kindle4rss.com/feeds/design.wired.xml', True)
           ]