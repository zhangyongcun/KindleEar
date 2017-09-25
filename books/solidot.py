#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return solidot

class solidot(BaseFeedBook):
    title                 = u'Solidot'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Solidot', 'http://www.solidot.org/index.rss', True)
           ]