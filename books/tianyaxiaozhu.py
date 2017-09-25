#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return tianyaxiaozhu

class tianyaxiaozhu(BaseFeedBook):
    title                 = u'天涯小筑'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'天涯小筑', 'http://tvfantasy.net/feed/', True)
           ]