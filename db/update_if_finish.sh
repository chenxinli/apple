#!/bin/sh

updatestamp="/tmp/.updating"
user=root
password=24985zf
tables="ipad_pd ipad_nj ipad_hk ipad_cd ipad_sz ipad_xd ipad_slt ipad_cdtest"

if [ -e $updatestamp ];
then
	echo "`date` update in progress, just exit"
	exit 0
fi

touch $updatestamp

echo `date`
for table in $tables; 
do
	SQL="select count(*) from $table where status=0"
	count=`echo $SQL | mysql -u$user -p$password apple | grep -v count`
	echo "`date` : $table status=0 count: $count"
	if [[ $count -lt 50 ]]; then
		echo "`date` Bang! $table $count"
		echo "update $table set status=0" | mysql -u$user -p$password apple
		echo "`date` finished! $count"
	fi
done
rm $updatestamp
