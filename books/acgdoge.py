#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return acgdoge

class acgdoge(BaseFeedBook):
    title                 = u'ACGdoge'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'ACGdoge', 'http://www.acgdoge.net/feed/atom', True)
           ]