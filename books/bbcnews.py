#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return bbcnews

class bbcnews(BaseFeedBook):
    title                 = u'BBC News'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'BBC News', 'http://feeds.bbci.co.uk/news/rss.xml', True)
           ]