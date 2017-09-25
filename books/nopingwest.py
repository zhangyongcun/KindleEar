#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return nopingwest

class nopingwest(BaseFeedBook):
    title                 = u'NO Ping West (搞笑)'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'NO Ping West (搞笑)', 'http://feedmaker.kindle4rss.com/feeds/no-ping-west.xml', True)
           ]