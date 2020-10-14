#!/bin/bash

if [ -z "$1" ]
  then
    echo "No argument supplied (name of kami file)"
    exit 1
fi


create_prob=("src/create_pddl.py")
domain=("src/domain.pddl")

python3 $create_prob $1 > /tmp/prob.pddl

color=("\x1B[34m")
color_end=("\e[0m")

printf $color"Running fast-downward with FF heuristic and context-enhanced additive heuristic... \n\n"$color_end
./../downward-main/fast-downward.py $domain /tmp/prob.pddl --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])" > /tmp/output

cat sas_plan

printf $color"\n\nRunning fast-downward with blind heuristics, may take a while...\n\n"$color_end
./../downward-main/fast-downward.py $domain /tmp/prob.pddl --search "astar(blind())" > /tmp/output

cat sas_plan
rm -f sas_plan
rm -f /tmp/output
rm -f /tmp/prob.pddl