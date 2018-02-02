#!/bin/bash

#Script to create new repository and add ACL


if blih -u alexandre.brun@epitech.eu repository create "$1"

blih -u alexandre.brun@epitech.eu repository setacl "$1" ramassage-tek r

blih -u alexandre.brun@epitech.eu repository getacl "$1"
then
	exit 0
else
	exit 84
fi


