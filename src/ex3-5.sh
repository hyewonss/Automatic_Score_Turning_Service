#!/bin/sh

myFunction () {
echo "Got into function"
eval ls "$a"
return 
}
echo "Start the program"
a=$1
myFunction $a
echo "Quit the program"
exit 0
