#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return hypervocal

class hypervocal(BaseFeedBook):
    title                 = u'HyperVocal'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'HyperVocal', 'http://hypervocal.com/feed/', True)
           ]