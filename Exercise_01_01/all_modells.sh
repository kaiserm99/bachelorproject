#!/bin/sh
SOLUTIONS=0
cp $1 /tmp/tmpsat

while :; do

  minisat -verb=0 /tmp/tmpsat /tmp/tmpout

  if [ `head -1 /tmp/tmpout` = UNSAT ]; then
    break
  fi

  SOLUTIONS=$((SOLUTIONS + 1))

  tail -1 /tmp/tmpout |
    awk '{
      for(i=1;i<NF;++i) { $i = -$i }
      print
    }' >> /tmp/tmpsat

  perl -pe  's/(\d+)$/$1+1/e' /tmp/tmpsat

done

echo There are $SOLUTIONS solutions.

rm -f /tmp/tmpsat
rm -f /tmp/tmpout
