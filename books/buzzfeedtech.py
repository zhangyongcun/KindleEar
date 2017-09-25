#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return buzzfeedtech

class buzzfeedtech(BaseFeedBook):
    title                 = u'BuzzFeed Tech'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'BuzzFeed Tech', 'http://www.buzzfeed.com/tech.xml', True)
           ]