#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return newyorkernews

class newyorkernews(BaseFeedBook):
    title                 = u'New Yorker: News'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'New Yorker: News', 'http://feedmaker.kindle4rss.com/feeds/news.newyorker.com.xml', True)
           ]