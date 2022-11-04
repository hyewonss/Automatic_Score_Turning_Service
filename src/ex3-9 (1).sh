#!/bin/sh

f=$1
eval grep $f DB.txt
exit 0
