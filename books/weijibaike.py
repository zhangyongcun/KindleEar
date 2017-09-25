#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return weijibaike

class weijibaike(BaseFeedBook):
    title                 = u'维基百科优良条目供稿'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'维基百科优良条目供稿', 'http://zh.wikipedia.org/w/api.php?action=featuredfeed&feed=good&feedformat=atom', True)
           ]