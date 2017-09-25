#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return zerohedge

class zerohedge(BaseFeedBook):
    title                 = u'Zero Hedge'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Zero Hedge', 'http://feeds.feedburner.com/zerohedge/feed', True)
           ]