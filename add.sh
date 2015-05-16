#!/bin/bash
while read line
	do
		echo "'http://www.romzj.com"${line:1:(-1)}\'\, >> moto.link
	done < $1
