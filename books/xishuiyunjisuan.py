#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return xishuiyunjisuan

class xishuiyunjisuan(BaseFeedBook):
    title                 = u'细说云计算'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'细说云计算', 'http://feedmaker.kindle4rss.com/feeds/CloudNote.weixin.xml', True)
           ]