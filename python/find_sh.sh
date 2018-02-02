#!/bin/bash

if find . -type f \( -name "*.sh" \)
then
	exit 0
else
	exit 84
fi

