#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return theatlantic

class theatlantic(BaseFeedBook):
    title                 = u'The Atlantic'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'The Atlantic', 'http://feeds.feedburner.com/TheAtlantic', True)
           ]