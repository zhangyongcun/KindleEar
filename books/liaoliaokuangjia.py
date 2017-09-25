#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return liaoliaokuangjia

class liaoliaokuangjia(BaseFeedBook):
    title                 = u'聊聊架构'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'聊聊架构', 'http://feedmaker.kindle4rss.com/feeds/archtime.weixin.xml', True)
           ]