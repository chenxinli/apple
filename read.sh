#!/bin/bash


dir="logs/`date +%m%d`"
today=`date +"%d %b"`
today="30 Dec"
mkdir $dir

for i in `grep "GOTIT" ./logs/email.out.* | grep "$today" | awk '{print $NF}'`; 
do 
echo $i | ./email/readapple.py | ./email/readmeta.py  >> $dir/email.out
done

#awk '{printf("%s.*%s\n", $1, $NF)}' $dir/email.out | xargs -i grep -n {} ./generate/hk/userlist.txt ./generate/nj/userlist.txt >> $dir/id.out


#mail -s "apple `date +%m-%d`" "chen.daqi@yahoo.cn,chen.daqi@gmail.com" < $dir/email.out
