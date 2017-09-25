#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return gawker

class gawker(BaseFeedBook):
    title                 = u'Gawker'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Gawker', 'http://feeds.gawker.com/gawker/full', True)
           ]