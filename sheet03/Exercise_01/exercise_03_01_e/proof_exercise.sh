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

printf $green"**********************  Exercise 1 **********************\n"$color_end
printf $green"Solving the given Kami problem. See for console for more infos...\n"$color_end
printf $green"==================================================================\n\n\n"$color_end
./../kami_solver.sh kami.txt 