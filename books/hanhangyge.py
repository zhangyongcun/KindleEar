#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return hanhangyge

class hanhangyge(BaseFeedBook):
    title                 = u'韩寒·一个'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'韩寒·一个', 'http://feedmaker.kindle4rss.com/feeds/wufazhuce.com.xml', True)
           ]