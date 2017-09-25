#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return arstechnica

class arstechnica(BaseFeedBook):
    title                 = u'Ars Technica'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Ars Technica', 'http://feeds.arstechnica.com/arstechnica/index/', True)
           ]