#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return fenghuangwang

class fenghuangwang(BaseFeedBook):
    title                 = u'凤凰网'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'凤凰网', 'http://feed43.com/1726484643045386.xml', True)
           ]