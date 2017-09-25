#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return aifanger

class aifanger(BaseFeedBook):
    title                 = u'爱范儿 · Beats of Bits'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'爱范儿 · Beats of Bits', 'http://www.ifanr.com/feed', True)
           ]