#!/bin/sh

f=$1
if [ -f "$f" ]; then
	echo "$f exists"
else
	eval "mkdir $f"
	eval "cd $f"
	eval "touch file0.txt"
	eval "touch file1.txt"
	eval "touch file2.txt"
	eval "touch file3.txt"
	eval "touch file4.txt"
	eval "tar cf files.tar *.txt*"
	eval "ls"
	eval "mkdir files"
	eval "mv files.tar files"
	eval "cd files"
	eval "tar xvf files.tar"
fi
exit 0
