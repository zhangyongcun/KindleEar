#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return hexunjinrtoutiao

class hexunjinrtoutiao(BaseFeedBook):
    title                 = u'和讯-今日头条'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'和讯-今日头条', 'http://feedmaker.kindle4rss.com/feeds/hexun.com.xml', True)
           ]