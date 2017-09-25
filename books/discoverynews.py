#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return discoverynews

class discoverynews(BaseFeedBook):
    title                 = u'Discovery News'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Discovery News', 'http://feeds.feedburner.com/DiscoveryNews-Top-Stories', True)
           ]