#!/bin/bash
while read line 
do 
wget ${line:1:(-1)}
done < $1
