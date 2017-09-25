#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return tomac

class tomac(BaseFeedBook):
    title                 = u'9to5Mac'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'9to5Mac', 'http://9to5mac.com/feed/', True)
           ]