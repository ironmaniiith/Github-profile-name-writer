#!/bin/bash
echo 'Enter the name of the file in which your set of alphabets are stored'
read alphabets
echo 'Now enter the name of the file in which you set of numbers are stored'
read numbers

# Alphabets
alphabetLines=`cat $alphabets | wc -l`
for i in `seq 1 8 $alphabetLines `;do
	for j in `seq 0 6`; do
			cat $alphabets | awk NR==$(($i+$j))
	done | python parse.py
done > finalIndexing.py


# Numbers
numberLines=`cat $numbers | wc -l`
for i in `seq 1 8 $numberLines`; do
	for j in `seq 0 6`; do
		cat $numbers | awk NR==$(($i+$j))
	done | python parse.py
done >> finalIndexing.py

# The final output looks something similar to what is stored in testIndexing.py
echo 'Cool, now you have your final indexing in the file finalIndexing.py which will automatically be used'