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
printf $green"Printing the shortest path from Frankfurt to München in the given transition system...\n"$color_end
printf $green"======================================================================================\n"$color_end
python3 exercise_02_02_b.py