#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return betabeat

class betabeat(BaseFeedBook):
    title                 = u'Betabeat'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Betabeat', 'http://betabeat.com/feed/', True)
           ]