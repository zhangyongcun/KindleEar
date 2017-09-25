#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return shaoshupai

class shaoshupai(BaseFeedBook):
    title                 = u'少数派'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'少数派', 'http://sspai.com/feed', True)
           ]