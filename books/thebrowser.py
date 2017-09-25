#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return thebrowser

class thebrowser(BaseFeedBook):
    title                 = u'The Browser'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'The Browser', 'http://thebrowser.com/feed/', True)
           ]