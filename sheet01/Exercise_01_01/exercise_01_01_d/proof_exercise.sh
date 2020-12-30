#!/bin/bash

# Copyright 2020, University of Freiburg
# Bachelor-project - Foundations of Artificial Intelligence

# Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

# Usage:

# Just execute this script and you can see the proof that the Exercise was worked on.

#	./proof_exercise.sh

# Color values                                                                  
red=("\x1B[31m")
green=("\x1B[32m")
blue=("\x1B[34m")
color_end=("\e[0m")

# File names
tmp_cnf=("/tmp/tmp.cnf")
tmp_cnf_real=("/tmp/tmp2.cnf")
tmp_model=("/tmp/tmp.model")
tmp_out=("/tmp/out")


parser=$(find ../../ -name "parser.py")
if [ -z $parser ];
then
	echo "WARNING! Couldn't find parser.py in the two upper parent folders!"
	exit -1
fi

all_mod=$(find ../../ -name "all_models.sh")
if [ -z $all_mod ];
then
	echo "WARNING! Couldn't find all_models.sh in the two upper parent folders!"
	exit -1
fi



printf $green"Printing the CNF of the given NSP-Problem...\n"$color_end
printf $green"=============================================\n"$color_end



python3 $parser > $tmp_cnf

tail -n +2 $tmp_cnf > $tmp_cnf_real
cat $tmp_cnf


printf $green"\n\nPrinting the all the Models of the given NSP-Problem...\n"$color_end
printf $green"===========================================================\n"$color_end
./$all_mod $tmp_cnf_real $tmp_model > $tmp_out

tail -n 12 $tmp_model | tee $tmp_model


printf $green"\n\nPrinting the all the written table Models of the given NSP-Problem...\n"$color_end
printf $green"===========================================================================\n"$color_end
python3 nsp_tester.py $tmp_model

rm -f $tmp_cnf
rm -f $tmp_cnf_real
rm -f $tmp_model
rm -f $tmp_out