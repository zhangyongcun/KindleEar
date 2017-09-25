#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return dailydot

class dailydot(BaseFeedBook):
    title                 = u'Daily Dot'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Daily Dot', 'http://www.dailydot.com/feed/summary/latest/', True)
           ]