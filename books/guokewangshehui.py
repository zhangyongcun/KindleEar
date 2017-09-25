#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return guokewangshehui

class guokewangshehui(BaseFeedBook):
    title                 = u'果壳网:社会'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'果壳网:社会', 'http://feedmaker.kindle4rss.com/feeds/subject-society.guokr.com.xml', True)
           ]