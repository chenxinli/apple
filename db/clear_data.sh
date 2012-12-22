#!/bin/sh

user=root
password=24985zf
tables="ipad_pd ipad_nj ipad_hk ipad_cd ipad_sz ipad_xd ipad_slt ipad_cdtest"

for table in $tables; 
do
	echo "`date` updating: $table"
	SQL="update $table set status=0"
	echo $SQL | mysql -u$user -p$password apple
	echo "`date` done updating: $table"
done
