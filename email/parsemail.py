#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,re
from email import parser
from email import header


timept='''提取日期：
\d+月\d+日(.*)'''
namept="亲爱的(.*),"
colorpt=".*[黑白]色"
addrpt='''提取地点：
(.*)Apple Store'''

def readmeta(content) :
	msg=parser.Parser().parsestr(content)

	buffer=""
	for part in msg.walk() :
		key = part.get_payload(decode=True)
		buffer += str(key)

	print buffer

print readmeta(sys.stdin.read())
