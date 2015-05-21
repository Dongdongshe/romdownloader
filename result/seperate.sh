#!/bin/bash
while read line 
do
echo $(cut -d ';' -f1 <<< "$line") >> $2 
echo $(cut -d ';' -f2 <<< "$line") >> $2
echo $(cut -d ';' -f3 <<< "$line") >> $2
echo $(cut -d ';' -f4 <<< "$line") >> $2
echo $(cut -d ';' -f5 <<< "$line") >> $2 
done < $1
