#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wiredtopstories

class wiredtopstories(BaseFeedBook):
    title                 = u'WIRED / Top Stories'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'WIRED / Top Stories', 'http://feedmaker.kindle4rss.com/feeds/top-stories.wired.xml', True)
           ]