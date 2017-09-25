#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return newrepublic

class newrepublic(BaseFeedBook):
    title                 = u'New Republic'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'New Republic', 'http://www.newrepublic.com/rss.xml', True)
           ]