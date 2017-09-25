#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return lincxtoy

class lincxtoy(BaseFeedBook):
    title                 = u'LinuxTOY'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'LinuxTOY', 'https://linuxtoy.org/feeds/all.atom.xml', True)
           ]