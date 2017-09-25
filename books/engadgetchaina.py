#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return engadgetchaina

class engadgetchaina(BaseFeedBook):
    title                 = u'Engadget 中国版'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Engadget 中国版', 'http://feedmaker.kindle4rss.com/feeds/cn.engadget.com.xml', True)
           ]