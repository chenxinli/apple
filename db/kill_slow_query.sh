#!/bin/sh

user=root
password=24985zf

SQL="show processlist;"

echo `date`
echo $SQL | mysql -u$user -p$password apple | grep Sleep | grep -v localhost | awk '{if($6>50) print $0}'

slow_ids=`echo $SQL | mysql -u$user -p$password apple | grep Sleep | grep -v localhost | awk '{if($6>50) print $1}'`
for id in $slow_ids; 
do
	echo "kill $id"
	echo "kill $id" | mysql -u$user -p$password apple
done
