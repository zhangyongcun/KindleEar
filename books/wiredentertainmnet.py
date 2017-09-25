#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wiredentertainmnet

class wiredentertainmnet(BaseFeedBook):
    title                 = u'WIRED / Entertainment'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'WIRED / Entertainment', 'http://feedmaker.kindle4rss.com/feeds/underwire.wired.xml', True)
           ]