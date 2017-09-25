#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return yidongkaifaqianxian

class yidongkaifaqianxian(BaseFeedBook):
    title                 = u'移动开发前线'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'移动开发前线', 'http://feedmaker.kindle4rss.com/feeds/bornmobile.weixin.xml', True)
           ]