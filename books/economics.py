#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return economics

class economics(BaseFeedBook):
    title                 = u'Economics'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Economics', 'http://feedmaker.kindle4rss.com/feeds/economics.economist.com.xml', True)
           ]