#!/bin/bash
COMM=$1
if [ ${COMM}x == x ];then
    COMM=`date`
else
    COMM=$1 `date`
fi
git add .
git commit -m"${COMM}"
git push origin master

