#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return economistbusinessfinance

class economistbusinessfinance(BaseFeedBook):
    title                 = u'Economist/Business & Finance'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Economist/Business & Finance', 'http://feedmaker.kindle4rss.com/feeds/business-finance.economist.com.xml', True)
           ]