#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return newyorkersciencetech

class newyorkersciencetech(BaseFeedBook):
    title                 = u'New Yorker: Science & Tech'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'New Yorker: Science & Tech', 'http://feedmaker.kindle4rss.com/feeds/tech.newyorker.com.xml', True)
           ]