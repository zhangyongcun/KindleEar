#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return reuters

class reuters(BaseFeedBook):
    title                 = u'Reuters'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Reuters', 'http://feeds.reuters.com/reuters/topNews', True)
           ]