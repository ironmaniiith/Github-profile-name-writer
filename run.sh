#!/bin/bash
printf "\033c"
rm -rf runThis.sh
if  ls components/main.py >/dev/null 2>/dev/null ; then
	python components/main.py
	echo 'Now just run the file runThis.sh in your test repository and enjoy..!!'
else
	echo 'Make sure you have all the files at correct places'
fi