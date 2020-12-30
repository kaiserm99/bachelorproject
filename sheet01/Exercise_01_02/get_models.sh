#!/bin/bash

# Copyright 2020, University of Freiburg
# Bachelor-project - Foundations of Artificial Intelligence

# Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

# Usage:

# Please make sure you are using the given file ordering, otherwise problems
# can occur.

# If you want to get the models of the current Program in the
# script stable_models.py then just use:

# 	./get_models.sh

# If you want to provide a functional Program to the script, then use:

# 	./get_models.sh "PROGRAM" --> ./get_models.sh "Impl(Not(a), b), Impl(Not(b), a)"


# File names
tmp_file=("/tmp/tmp_cnf")
tmp_cnf=("/tmp/tmp_full_cnf.cnf")
tmp_models=("/tmp/tmp_models.model")
tmp_atoms=("/tmp/atoms.txt")

# Color values                                                                  
color=("\x1B[34m")
color_end=("\e[0m")

# Make sure to get the right file path, which depends on where you execute the file
pyfile=$(find ../../ -name "stable_models.py")

# Check if stable_models.py was found
if [ -z $pyfile ];
then
	echo "WARNING! Couldn't find stable_models.py in the two upper parent folders!"
	exit -1
fi


if [ -n "$1" ];
	then python3 $pyfile --minimal -p "$1" > $tmp_file;

	else python3 $pyfile --minimal > $tmp_file;
fi



tail -n +2 $tmp_file > $tmp_cnf

# Make sure to get the right file path, which depends on where you execute the file
all_mod=$(find ../../ -name "all_models.sh")

if [ -z $all_mod ];
then
	echo "WARNING! Couldn't find all_models.sh in the two upper parent folders!"
	exit -1
fi



$all_mod $tmp_cnf $tmp_models > $tmp_atoms  # This is just used so there is no ugly output


printf $color"\nAll Atoms: \n"$color_end
head $tmp_file -n +1 | tee $tmp_atoms

printf $color"\nAll stable models out of Minisat:\n"$color_end

tail -n +2 $tmp_models


printf $color"\nAll stable models mapped to the right atom:\n"$color_end


# The following part maps the corresponding atoms to the 
NAMES=()
for elem in $(cat $tmp_atoms | sed "s/,//g; s/[][]//g; s/'//g")
do
	NAMES+=($elem)
done

for number in $(tail -n +2 $tmp_models)
do
	if [ "$number" -eq "0" ]; then
		echo 
   		continue
	fi

	if [[ ${number:0:1} != "-" ]] ; 
		
		then
			number=$((number-1))
			echo -n ${NAMES[${number}]}" ";
	fi
done

rm -f $tmp_file
rm -f $tmp_cnf
rm -f $tmp_models
rm -f $tmp_atoms
