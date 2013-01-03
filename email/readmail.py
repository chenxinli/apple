#!/usr/bin/python
# -*- coding: utf-8 -*-  
  
import sys,poplib,time 
from email import parser  
from email import header
  
host = 'pop.163.com'  

username = 'we72_83@163.com'
password = "8bnq2f"

def reademail(user, pwd) :
	pop_conn = poplib.POP3(host, timeout=5)
	pop_conn.user(user)  
	pop_conn.pass_(pwd)  
	 
	#Get messages from server:
	topn = 3 
	mailcount = len(pop_conn.list()[1])
	startindex = 1
	if mailcount > topn :
		startindex = mailcount - topn + 1
	messages = [pop_conn.top(i, 0) for i in range(startindex, mailcount+1)]  
	  
	# Concat message pieces:  
	messages = ["\n".join(mssg[1]) for mssg in messages]  
	  
	#Parse message intom an email object:  
	messages = [parser.Parser().parsestr(mssg) for mssg in messages]  
	for message in messages:  
		subject = header.decode_header(message['Subject'])[0][0];
		fromstr = header.decode_header(message['From']);
		date = header.decode_header(message['Date']);
		print "Subject:",subject, "From", fromstr, "Date", date, user+":"+pwd
		#print "From", fromstr, "Date", date, user+":"+pwd
		#if subject.find("預訂申請") >= 0 :
		#	print "GOTIT:", date, user+":"+pwd 

	'''
	# delete all emails
	for i in range(2, mailcount+1) :
		pop_conn.dele(i)
	'''

	pop_conn.quit()  

for line in sys.stdin.readlines() :
	line = line.strip()
	index = line.find(":")
	user = line[:index]
	pwd = line[index+1:]

	try:
		reademail(user, pwd)
		print time.ctime(), "checkmail:", user+":"+pwd
	except Exception, data:
		print "exception:", Exception, ":", data, "\tUser:", line
	sys.stdout.flush()

