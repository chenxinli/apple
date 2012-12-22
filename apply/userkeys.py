#!/usr/bin/python   
#-*-coding:utf-8-*-   
 
import time,sys,threading;
import socket;
import MySQLdb;

SPLIT="#121#"
starthour="0850"
stophour="1710"

thresh=200

host="42.121.56.68"
user="ipad"
passwd="ipadpwd"
db="apple"

table="ipad_hk"

loglock=threading.Lock()
def log(*args) :
	loglock.acquire()
	print time.ctime(), args
	loglock.release()


keys = []
keyslock = threading.Lock()
def retrieve() :
	global keys
	global keyslock

	key = None
	keyslock.acquire()
	if len(keys) > 0 :
		key = keys.pop()
	keyslock.release()
	return key

def pull() :
	global keys
	global keyslock

	while True :
		#if time.localtime().tm_hour >= stophour :
		if time.strftime("%H%M", time.localtime()) >= stophour :
			break
		time.sleep(1)

		if len(keys) > thresh :
			continue

		try :
			log("start pull new one")
			buffer = readmysql()
			
			if len(buffer) > 0 :
				keyslock.acquire()
				keys.extend(buffer)
				keyslock.release()
			log("end pull, size:", len(buffer))
		except Exception, ex:
			log("exception when read from mysql", ex)

def readmysql() :
	buffer = []
	conn=MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
	conn.autocommit(1)
	cursor = conn.cursor()

	comment = socket.gethostname()+"#"+socket.gethostbyname(socket.gethostname())
	cursor.execute("update " + table + " set id=(@tempid:=id), status=1, updatetime=NOW(), comment='"+comment
		+"' where status=0 limit 1 ")
	cursor.execute("select id, data from " + table + " where id = @tempid")
	row = cursor.fetchone() 
	if row != None :
		log("fetch id:", row[0])
		tmp = row[1].split(SPLIT)
		buffer.extend(tmp)
	cursor.close()
	conn.close()
	return buffer

while True :
	#if time.localtime().tm_hour >= starthour :
	if time.strftime("%H%M", time.localtime()) >= starthour :
		break

	log("wait until :", starthour)
	time.sleep(10)

pullthread = threading.Thread(target=pull)
pullthread.start()
