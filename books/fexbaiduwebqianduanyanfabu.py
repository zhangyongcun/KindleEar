#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return fexbaiduwebqianduanyanfabu

class fexbaiduwebqianduanyanfabu(BaseFeedBook):
    title                 = u'FEX 百度 Web 前端研发部'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'FEX 百度 Web 前端研发部', 'http://fex.baidu.com/feed.xml', True)
           ]