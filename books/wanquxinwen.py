#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wanquxinwen

class wanquxinwen(BaseFeedBook):
    title                 = u'湾区日报'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'湾区日报', 'http://wanqu.co/feed/', True)
           ]