#!/bin/bash


# File names
tmp_file=("/tmp/tmp_cnf")
tmp_cnf=("/tmp/tmp_full_cnf.cnf")
tmp_modells=("/tmp/tmp_modells.modell")

# Color values                                                                  
color=("\x1B[34m")
color_end=("\e[0m")


python3 stable_modells.py > $tmp_file

tail -n +2 $tmp_file > $tmp_cnf

./../Exercise_01_01/all_modells.sh $tmp_cnf $tmp_modells


printf $color"\n\nHere you can see all the used atoms. The first Element corresponds to the Number 1 and so on...\n\n"$color_end
printf "All Atoms: "
head $tmp_file -n +1

printf $color"\nAll stable modells of the given Program:\n\n"$color_end
cat $tmp_modells


rm -f $tmp_file
rm -f $tmp_cnf
rm -f $tmp_modells