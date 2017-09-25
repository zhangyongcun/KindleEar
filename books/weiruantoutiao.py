#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return weiruantoutiao

class weiruantoutiao(BaseFeedBook):
    title                 = u'微软研究院AI头条'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'微软研究院AI头条', 'http://feedmaker.kindle4rss.com/feeds/MSRAsia.weixin.xml', True)
           ]