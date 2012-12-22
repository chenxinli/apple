#!/bin/env python

import sys,string;
import MySQLdb;

filepath=sys.argv[1]
table=sys.argv[2]

split=filepath.rfind("/")
dot=filepath.find(".")

if split == -1 :
	path = "."
	module = filepath[:dot]
else :
	path = filepath[:split]
	module = filepath[split+1:dot]

sys.path.append(path)
M=__import__(module)
keys = M.keys

conn=MySQLdb.connect(host="42.121.56.68",user="ipad",passwd="ipadpwd",db="apple")
conn.autocommit(1)
cursor = conn.cursor ()

SPLIT="#121#"
keyperline=200
size=len(keys)
lines=size/keyperline

for i in range(0, lines) :
	tmp = keys[i*keyperline:(i+1)*keyperline]
	data = string.join(tmp, SPLIT)
	
	try :
		cursor.execute("insert into "+table+"(data,status,updatetime) values ('%s', 0, NOW())" % (data))
	except Exception, ex :
		print "exception when insert", ex

cursor.execute("select count(*) from "+table)
print cursor.fetchone()

cursor.close ()
conn.close ()
