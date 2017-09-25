#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return tengxunxinwenguonei

class tengxunxinwenguonei(BaseFeedBook):
    title                 = u'腾讯新闻：国内'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'腾讯新闻：国内', 'http://feedmaker.kindle4rss.com/feeds/china.qq.com.xml', True)
           ]