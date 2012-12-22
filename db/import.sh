#!/bin/bash - 
#===============================================================================
#
#          FILE:  import.sh
# 
#         USAGE:  ./import.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR: zhenfang (taobao), zhenfang@taobao.com
#       COMPANY: www.taobao.com
#       CREATED: 12/08/2012 01:25:28 AM CST
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

dir=$1
table=$2

while [ 1 ];
do
	for file in `ls $dir/*.py`; 
	do
		echo "`date` import $file to $table"
		tmp="$dir/`date +%s`.py"
		mv $file $tmp
		./import.py $tmp $table
		mv $tmp $file.imported
		echo "`date` done!"
	done

	sleep 5
done

