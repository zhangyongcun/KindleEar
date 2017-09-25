#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return duxier

class duxier(BaseFeedBook):
    title                 = u'读写人'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'读写人', 'http://www.duxieren.com/duxieren.xml', True)
           ]