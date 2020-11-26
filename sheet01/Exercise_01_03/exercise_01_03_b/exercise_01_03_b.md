
## Aufgabe Nr.3 b)

Mit dem Befehl *clingo 0 exercise_01_03_b.lp* erhält man folgende Ausgabe:
> clingo version 5.2.2  
Reading from exercise_01_03_b.lp  
Solving...  
Answer: 1  
a  
Answer: 2  
b  
SATISFIABLE  

-->  Somit erhalten wir die beiden Modelle des Programms, welche gerade gerade {{a}, {b}} sind. 

Mit dem Befehl *./get_modells.sh* "Impl(Not(a), b), Impl(Not(b), a)" in dem Unterordner Exercise_01_02 erhält man folgendes:
> All Atoms:  
['a', 'b']  
All stable models out of Minisat:  
1 -2 0  
-1 2 0  
All stable models mapped to the right atom:  
a  
b 

--> Somit erhalten wir das gleiche Ergebnis wie mit *clingo*.