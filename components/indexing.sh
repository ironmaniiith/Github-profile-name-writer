alphabetLines=`cat alphabets | wc -l`
for i in `seq 1 8 $alphabetLines `;do
	for j in `seq 0 6`; do
			cat alphabets | awk NR==$(($i+$j))
	done | python parse.py
done > finalIndexing.txt

numberLines=`cat numbers | wc -l`

for i in `seq 1 8 $numberLines`; do
	for j in `seq 0 6`; do
		cat numbers | awk NR==$(($i+$j))
	done | python parse.py
done >> finalIndexing.txt