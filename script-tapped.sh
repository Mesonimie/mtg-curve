#!/bin/sh

for land in $(seq 24 25)
do
    echo  "# $land"
    for cost in C 1C CC 2C 1CC CCC 3C 2CC 1CCC CCCC 4C 3CC 2CCC 1CCCC 5C 4CC 3CCC 5CC 4CCC
    do
	echo -n "| $cost | "
	pypy3 main-tapped.py --land $land $cost 
	echo "|"
    done
    echo ""
done
