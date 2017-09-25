#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return businessinsider

class businessinsider(BaseFeedBook):
    title                 = u'Business Insider'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Business Insider', 'http://feeds2.feedburner.com/businessinsider', True)
           ]