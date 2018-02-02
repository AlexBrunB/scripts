#!/bin/bash
 
if cut -d ";" -f 3 | grep -c -i "$1"
then
	exit 0
else
	exit 84	
fi
