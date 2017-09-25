#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return haoqixinrbao

class haoqixinrbao(BaseFeedBook):
    title                 = u'好奇心日报'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'好奇心日报', 'http://www.qdaily.com/feed', True)
           ]