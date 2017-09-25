#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return grantiand

class grantiand(BaseFeedBook):
    title                 = u'Grantland'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Grantland', 'http://www.grantland.com/feed', True)
           ]