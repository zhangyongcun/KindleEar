#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ifuckinglovescience

class ifuckinglovescience(BaseFeedBook):
    title                 = u'I Fucking Love Science'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'I Fucking Love Science', 'http://www.iflscience.com/rss.xml', True)
           ]