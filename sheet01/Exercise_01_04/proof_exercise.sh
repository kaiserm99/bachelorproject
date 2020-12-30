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

get_mod=$(find ../../ -name "get_models.sh")
if [ -z $get_mod ];
then
	echo "WARNING! Couldn't find get_models.sh in the two upper parent folders!"
	exit -1
fi


printf $green"Pirnting my own script with the given program (with pinguin):\n"$color_end
printf $green"=============================================================\n"$color_end
./$get_mod "Impl(And(vogel, Not(nfliegt)), fliegt), Impl(pinguin, nfliegt), Impl(TOP, vogel), Impl(TOP, pinguin)"
printf $green"\nClingo:\n=======\n"$color_end
clingo 0 pinguin_prog.lp


printf $green"\n\nPirnting my own script with the given program (WITHOUT pinguin):\n"$color_end
printf $green"================================================================\n"$color_end
./$get_mod "Impl(And(vogel, Not(nfliegt)), fliegt), Impl(pinguin, nfliegt), Impl(TOP, vogel)"
printf $green"\nClingo:\n=======\n"$color_end
clingo 0 no_pinguin_prog.lp