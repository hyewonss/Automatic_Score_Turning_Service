#!/bin/sh

f=$1

eval "mkdir $f"
eval "cd $f"
eval "mkdir file0"
eval "mkdir file1"
eval "mkdir file2"
eval "mkdir file3"
eval "mkdir file4"
eval "touch file0.txt"
eval "touch file1.txt"
eval "touch file2.txt"
eval "touch file3.txt"
eval "touch file4.txt"
eval "ln -s file0.txt file0"
eval "ln -s file1.txt file1"
eval "ln -s file2.txt file2"
eval "ln -s file3.txt file3"
eval "ln -s file4.txt file4"
exit 0
