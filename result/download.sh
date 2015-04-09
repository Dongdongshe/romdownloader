#!/bin/bash
while read line 
do 
wget $line
done < $1
