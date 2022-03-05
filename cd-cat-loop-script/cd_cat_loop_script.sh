#!/bin/bash

if [ $# -eq 0 ]

then
	echo 
	
	echo "<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>"

	echo
	
	echo "Invalid Argument"
	
	echo "Usages: ./script <path/to/file>"
	
	echo

	echo "<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>"

	echo

else

	mkdir -p /tmp/dump

	find $1 -type f -exec ls {} \; | grep readme| while read line; do cp $line /tmp/dump;done

	ls /tmp/dump | for i in {0..1000};do cat /tmp/dump/readme_$i.txt;done 2>/dev/null | tr -d '\n'

fi
