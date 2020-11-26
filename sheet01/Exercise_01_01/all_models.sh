#!/bin/sh

SOLUTIONS=0
cp $1 /tmp/tmpsat
rm -f $2  # If there is already a Output file, just remove it to update it

while :; do

	minisat -verb=0 /tmp/tmpsat /tmp/tmpout

	if [ `head -1 /tmp/tmpout` = UNSAT ]; then  # Check if the calculated output contains UNSAT
		
		if [ $SOLUTIONS -eq 0 ]; then  # If there was no solution yet, then the file should contain UNSAT
	    	echo "UNSAT" > $2  
		fi
		
		break
	fi

	if [ $SOLUTIONS -eq 0 ]; then  # If there is minimum one solution, then write SAT on top of the Output file
		echo "SAT" > $2
		echo "" >> /tmp/tmpsat
	fi

	SOLUTIONS=$((SOLUTIONS + 1))

	tail -1 /tmp/tmpout >> $2  # Write the calculated solution into the Output file

	tail -1 /tmp/tmpout |
		awk '{
	    	for(i=1;i<NF;++i) { $i = -$i }
	    	print
	   	}' >> /tmp/tmpsat  # Negate the whole output and append it to the file, which is minisat'ed next

	perl -pe 's/(\d+)$/$1+1/e if $. == 1' /tmp/tmpsat > /tmp/tmpfile  # Increase the variable count

	cp /tmp/tmpfile /tmp/tmpsat

done

echo There are $SOLUTIONS solutions.

rm -f /tmp/tmpsat
rm -f /tmp/tmpout
rm -f /tmp/tmpfile
