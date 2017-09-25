#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return thedailybeast

class thedailybeast(BaseFeedBook):
    title                 = u'The Daily Beast'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'The Daily Beast', 'http://feeds.feedburner.com/thedailybeast/articles', True)
           ]