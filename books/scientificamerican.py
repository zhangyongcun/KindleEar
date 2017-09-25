#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return scientificamerican

class scientificamerican(BaseFeedBook):
    title                 = u'Scientific American'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Scientific American', 'http://rss.sciam.com/ScientificAmerican-Global', True)
           ]