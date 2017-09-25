#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return bolezaixian

class bolezaixian(BaseFeedBook):
    title                 = u'博客 - 伯乐在线'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'博客 - 伯乐在线', 'http://blog.jobbole.com/feed/', True)
           ]