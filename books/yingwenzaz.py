#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return yingwenzaz

class yingwenzaz(BaseFeedBook):
    title                 = u'英文杂志'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'英文杂志', 'http://feedmaker.kindle4rss.com/feeds/englishmags.weixin.xml', True)
           ]