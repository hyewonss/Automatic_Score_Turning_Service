#!/bin/sh

read weight height
h=$(echo "scale=3; $height/100" | bc)
bmi=$(echo "scale=3; $weight/($h*$h)" | bc)
if [ "$(echo "$bmi >= 23" | bc)" -eq 1 ] 
then
	echo "overweight"
elif [ "$(echo "$bmi < 18.5" | bc)" -eq 1 ] 
then
	echo "underweight"
else
	echo "average"

fi
exit 0
