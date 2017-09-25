#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return theatlanticwire

class theatlanticwire(BaseFeedBook):
    title                 = u'The Atlantic Wire'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'The Atlantic Wire', 'http://feeds.feedburner.com/TheAtlanticWire', True)
           ]