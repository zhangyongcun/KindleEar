#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return jianbao

class jianbao(BaseFeedBook):
    title                 = u'简书'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'简书', 'http://feedmaker.kindle4rss.com/feeds/jianshu.com.xml', True)
           ]