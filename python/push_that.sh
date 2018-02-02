#!/bin/bash

if git add --all ;
git commit -a;
git push ;
then
	exit 0
else
	exit 84
fi
