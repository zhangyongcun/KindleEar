#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return topstories

class topstories(BaseFeedBook):
    title                 = u'Top Stories'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Top Stories', 'http://feeds2.feedburner.com/time/topstories', True)
           ]