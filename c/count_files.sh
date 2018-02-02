#!/bin/bash

if find . -type f  | wc -l
then
	exit 0
else
	exit 84
fi

