#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return uproxx

class uproxx(BaseFeedBook):
    title                 = u'UPROXX'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'UPROXX', 'http://feeds.feedburner.com/uproxx/features', True)
           ]