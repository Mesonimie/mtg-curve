#!/bin/sh

for land in $(seq 20 30)
do
    echo -n "$land |"
    for cost in C 1C CC 2C 1CC CCC 3C 2CC 1CCC CCCC 4C 3CC 2CCC 1CCCC 5C 4CC 3CCC 5CC 4CCC
    do
	pypy3 main.py --land $land $cost 
	echo -n "|"
    done
    echo ""
done
