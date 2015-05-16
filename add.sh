#!/bin/bash
while read line
	do
		echo "'http://www.romzj.com"${line:1:(-1)}\'\, >> lg.link
	done < $1
