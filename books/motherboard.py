#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return motherboard

class motherboard(BaseFeedBook):
    title                 = u'Motherboard'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Motherboard', 'http://motherboard.vice.com/en_us/rss', True)
           ]