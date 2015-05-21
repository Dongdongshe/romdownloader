#!/bin/bash
files="/home/sherman/miui/*"
for f in $files
do 
echo $f >> "/home/sherman/error.txt"
unzip $f -d . >/dev/null
model=$(cat system/build.prop | grep "ro.product.model" | cut -d '=' -f2)
target=1
split_boot boot.img
repack-zImage.sh -u boot/boot.img-kernel
buildno=$(strings boot/boot.img-kernel_unpacked/piggy |grep "[23]\.[0-9]*\.[0-9]*"|tail -1)
if [ "$buildno" == "" ]
then 
buildno=$(strings boot/boot.img-kernel_unpacked/piggy.gz+piggy_trailer|grep "[23]\.[0-9]*\.[0-9]*"|tail -1)
fi
if [ "$buildno" == "" ]
then
echo "null" >> /home/sherman/error.txt
else echo "$buildno" >> /home/sherman/error.txt 
fi
version=$(cat system/build.prop | grep "ro.build.version.release" | cut -d '=' -f2)
platform=$(cat system/build.prop| grep "ro.board.platform" | cut -d '=' -f2)
echo "$model;$target;$buildno;$version;$platform" >> /home/sherman/parser.out
rm -rf system/ data/ META-INF/ boot.img boot/ 
done  
