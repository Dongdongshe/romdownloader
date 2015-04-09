#!/bin/bash
while read line 
do
echo $(cut -d ';' -f1 <<< "$line") >> miui.out.c 
echo $(cut -d ';' -f2 <<< "$line") >> miui.out.c 
echo $(cut -d ';' -f3 <<< "$line") >> miui.out.c 
echo $(cut -d ';' -f4 <<< "$line") >> miui.out.c 
echo $(cut -d ';' -f5 <<< "$line") >> miui.out.c 
done < $1
