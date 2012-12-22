#!/bin/bash - 
#===============================================================================
#
#          FILE:  ok.sh
# 
#         USAGE:  ./ok.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR: xinli.chen (taobao), xinli.chen@dianping.com
#       COMPANY: www.dianping.com
#       CREATED: 10/26/2012 03:33:14 PM CST
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

dir=`dirname $0`

file=$1
step=$2
total=$3
s=0

while [ $s -lt $total ]; 
do
	head -n `expr $s + $step` $file | tail -n $step | $dir/readmail.py > $dir/../logs/email.out.$s 2>&1 &
	s=`expr $s + $step`
done

wait
