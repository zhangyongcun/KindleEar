#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return extremetech

class extremetech(BaseFeedBook):
    title                 = u'ExtremeTech'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'ExtremeTech', 'http://www.extremetech.com/feed', True)
           ]