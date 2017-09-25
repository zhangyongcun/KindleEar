#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return sciencenordic

class sciencenordic(BaseFeedBook):
    title                 = u'ScienceNordic'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'ScienceNordic', 'http://sciencenordic.com/rss.xml', True)
           ]