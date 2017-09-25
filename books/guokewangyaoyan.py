#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return guokewangyaoyan

class guokewangyaoyan(BaseFeedBook):
    title                 = u'果壳网:谣言粉碎机'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'果壳网:谣言粉碎机', 'http://feedmaker.kindle4rss.com/feeds/fact.guokr.com.xml', True)
           ]