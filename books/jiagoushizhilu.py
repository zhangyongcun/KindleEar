#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return jiagoushizhilu

class jiagoushizhilu(BaseFeedBook):
    title                 = u'架构师之路'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'架构师之路', 'http://feedmaker.kindle4rss.com/feeds/gh_10a6b96351a9.weixin.xml', True)
           ]