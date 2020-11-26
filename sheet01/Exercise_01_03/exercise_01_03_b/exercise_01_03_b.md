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

Mit dem Befehl *./get_modells.sh* in dem Unterordner Exercise_01_02 erhält man folgendes Ergebnis. Dabei muss in der in der Datei *stable_modells.py* auch das jeweilige Programm ausgewählt werden:
> Here you can see all the used atoms. The first Element corresponds to the Number 1 and so on...  
All Atoms: ['a', 'b']  
All stable modells of the given Program:  
SAT  
1 -2 0  
-1 2 0  

--> Somit erhalten wir das gleiche Ergebnis wie mit *clingo*.
