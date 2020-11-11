#!/bin/bash

if [ -z "$1" ]
  then
    echo "No argument supplied (name of kami encoded file)"
    exit 1
fi

if ! [ -f "$1" ]; then
    echo "The supplied kami file ($1) does not exist. Please provide a other file!"
    exit 1
fi


function cleanup() {
    rm -f sas_plan
	rm -f $tmp_prob
	rm -f $tmp_out
}

function print_plan() {
	if ! [ -f sas_plan ]; 
	then
		echo "No plan with this kami encoded file!"
		exit 1
	fi

	cat sas_plan
}


# File names
create_prob=("src/create_pddl.py")
domain=("src/domain.pddl")
tmp_prob=("/tmp/prob.pddl")
tmp_out=("/tmp/out.txt")

# Color values
color=("\x1B[34m")
color_end=("\e[0m")


# Make sure when there is no excetion
if ! (python3 $create_prob $1 > $tmp_prob); then
	echo "Exception while creating the problem pddl file!"
	cleanup
	exit 1
fi


printf $color"Running fast-downward with FF heuristic and context-enhanced additive heuristic... \n\n"$color_end

if ./../downward-main/fast-downward.py $domain $tmp_prob --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])" > $tmp_out; then
	print_plan
else
	cleanup
	exit 1
fi


printf $color"\n\nRunning fast-downward with blind heuristics, may take a while...\n\n"$color_end

if ./../downward-main/fast-downward.py $domain $tmp_prob --search "astar(blind())" > $tmp_out; then
	print_plan
else
	cleanup
	exit 1
fi

cleanup


trap cleanup SIGINT
