#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return heikeyujike

class heikeyujike(BaseFeedBook):
    title                 = u'FreeBuf.COM | 关注黑客与极客'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'FreeBuf.COM | 关注黑客与极客', 'http://www.freebuf.com/feed', True)
           ]