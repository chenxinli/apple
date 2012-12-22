#!/usr/bin/python   
#-*-coding:utf-8-*-   
 
import httplib,urllib,time,sys;
import random,threading;

import userkeys;

maxretrytimes=3
numberthreads=10

def reserve(conn, key) :
	headers = {
			"Host": "reserve-cn.appleonline.net",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20100101 Firefox/16.0",
			"Accept": "*/*",
			"Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
			"Accept-Encoding": "gzip, deflate",
			"Connection": "keep-alive",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			"Referer": "https://reserve.apple.com/CN/zh_CN/reserve/iPad",
			"Content-Length": len(key),
			"Origin": "https://reserve.apple.com",
			"Pragma": "no-cache",
			"Cache-Control": "no-cache",
			};
	
	for i in range(0, maxretrytimes) :
		conn.request(method="POST", url="/reservation/create", body=key, headers=headers);   
		response = conn.getresponse();   
		data = response.read()
		if data == 'Success':
			break

	if count % 10 == 0:
		userkeys.log("reserve create:", response.status, response.reason, "Response:", data)


count = 0
countlock=threading.Lock()
def apply(name) :
	global count
	global countlock

	userkeys.log("thread started:", name)
	conn = httplib.HTTPSConnection(host="reserve-cn.appleonline.net", port=443, timeout=10)

	while True :
		#if time.localtime().tm_hour >= userkeys.stophour :
		if time.strftime("%H%M", time.localtime()) >= userkeys.stophour :
			break

		key = userkeys.retrieve()
		if key == None :
			userkeys.log("retrieve nothing, sleep 1 second")
			time.sleep(1)
			continue

		try :
			reserve(conn, key)
			countlock.acquire()
			count += 1
			if count % 100 == 0 :
				userkeys.log("thread:", name, "progress:", count)
			countlock.release()
		except Exception, ex :
			userkeys.log("exception when reserve:", ex)
			time.sleep(1)
			conn.close()
			conn = httplib.HTTPSConnection(host="reserve-cn.appleonline.net", port=443, timeout=10)

		sys.stdout.flush();

	conn.close();
	userkeys.log("thread finished:", name)

threads = []
for i in range(0, numberthreads) :
	th = threading.Thread(target=apply, args = (str(i)))
	th.start()
	threads.append(th)
	time.sleep(2)

for th in threads :
	th.join()

print "Done!"

