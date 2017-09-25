#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return cnbeta

class cnbeta(BaseFeedBook):
    title                 = u'cnBeta'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'cnBeta', 'http://feedmaker.kindle4rss.com/feeds/cnbeta.xml', True)
           ]