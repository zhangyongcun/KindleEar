#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return quarlz

class quarlz(BaseFeedBook):
    title                 = u'Quartz'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Quartz', 'http://qz.com/feed/', True)
           ]