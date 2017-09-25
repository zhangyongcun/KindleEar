#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return lixiangshenghuoshiyanshi

class lixiangshenghuoshiyanshi(BaseFeedBook):
    title                 = u'理想生活实验室'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'理想生活实验室', 'http://www.toodaylab.com/feed', True)
           ]