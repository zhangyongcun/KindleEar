#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return lianhezaobaoguonei

class lianhezaobaoguonei(BaseFeedBook):
    title                 = u'联合早报国内'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'联合早报国内', 'zaobao.feedsportal.com/c/34003/f/616930/index.rss', True)
           ]