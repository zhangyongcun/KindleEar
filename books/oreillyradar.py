#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return oreillyradar

class oreillyradar(BaseFeedBook):
    title                 = u'O'Reilly Radar'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'O'Reilly Radar', 'http://feeds.feedburner.com/oreilly/radar/atom', True)
           ]