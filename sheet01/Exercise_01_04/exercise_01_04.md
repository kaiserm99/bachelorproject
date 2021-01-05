## Aufgabe Nr. 4:

### a)

Mit *.pinguin*:

> Answer: 1  
-fliegt vogel pinguin  
SATISFIABLE

Ohne *.pinguin*:

> Answer: 1  
vogel fliegt  
SATISFIABLE

### b)
Im folgenden wird nun ein weiterer Constraint dem Programm hinzugefügt. Dieses sieht dann in Clingo-Syntax folgendermaßen aus:

```
fliegt :- vogel, not nfliegt. nfliegt :- pinguin. vogel. pinguin. :- fliegt, nfliegt.
```
Bzw. der Syntax des Programmes in der Programm-Sprache, welche in Nr.2) akzeptiert wird:

```
Impl(And(vogel, Not(nfliegt)), fliegt), Impl(pinguin, nfliegt), Impl(TOP, vogel),
Impl(TOP, pinguin), Impl(And(fliegt, nfliegt), BOT)
```

### c)

#### Eigener ASP-Solver:
Mit dem folgenden Aufruf erhalten wir gerade dasselbe Verhalten wie in Clingo, obwohl wir mein eigenes MiniSat-basiertes Programm verwenden (mit *.pinguin*):
```
./get_models.sh "Impl(And(vogel, Not(nfliegt)), fliegt), Impl(pinguin, nfliegt), Impl(TOP, vogel), Impl(TOP, pinguin), Impl(And(fliegt, nfliegt), BOT)"
```
Output:
```
All Atoms: 
['fliegt', 'nfliegt', 'pinguin', 'vogel']

All stable models out of Minisat:
-1 2 3 4 0

All stable models mapped to the right atom:
nfliegt pinguin vogel
```

<ins> Ohne den Fakt *.pinguin*: </ins>
```
./get_models.sh "Impl(And(vogel, Not(nfliegt)), fliegt), Impl(pinguin, nfliegt), Impl(TOP, vogel), Impl(And(fliegt, nfliegt), BOT)"
```
Output:
```
All Atoms: 
['fliegt', 'nfliegt', 'pinguin', 'vogel']

All stable models out of Minisat:
1 -2 -3 4 0

All stable models mapped to the right atom:
fliegt vogel 
```

--> Hier kann man erkennen, dass genau die gleichen stabilen Modelle wie in *a)* herausgekommen sind. Somit wurde gerade das Verhalten von Clingo simuliert. 

#### Eigener SAT-Solver und ohne CC und Loop-Formeln:
<ins> Alle Modelle mit dem Fakt *.pinguin*:</ins>

Mit dem folgenden Aufruf erhalten wir das gewünschte DIMACS-Format. Mit dem Skript *all_models.sh* können wir dann alle Modelle des Programmes ausgeben lassen.
```
python3 stable_models.py -d "And(Impl(And(vogel, Not(nfliegt)), fliegt), And(Impl(pinguin, nfliegt), And(Impl(TOP, vogel), And(Impl(TOP, pinguin), Impl(And(fliegt, nfliegt), BOT)))))"
```
Somit erhalten wir alle Modelle:
```
['fliegt', 'nfliegt', 'pinguin', 'vogel']  
-1 2 3 4 0
```
Bzw. zur besseren Leserlichkeit:
```
nfliegt pinguin vogel
```  
--> Hier erhalten wir wieder das gleiche Ergebnis wie mit Clingo.  
<br/>  
<ins> Alle Modelle ohne den Fakt *.pinguin*: </ins>
Hier wird ebenso wieder folgender Aufruf benutzt um das gewünschte DIMACS-Format zu erhalten:
```
python3 stable_models.py -d "And(Impl(And(vogel, Not(nfliegt)), fliegt), And(Impl(pinguin, nfliegt), And(Impl(TOP, vogel), Impl(And(fliegt, nfliegt), BOT))))"
```
Somit erhalten wir alle Modelle:
```
['fliegt', 'nfliegt', 'pinguin', 'vogel']  
1 -2 -3 4 0  
-1 2 -3 4 0  
-1 2 3 4 0 
```
Bzw. zur besseren Leserlichkeit:
```
fliegt vogel  
nfliegt vogel  
nfliegt pinguin vogel
```
--> Sobald man jedoch den Fakt *.pinguin* weglässt, kommen auch nicht stabile Modelle als Ergebnis heraus. In den letzten beiden Modellen gibt es nämlich Atome, welche nicht unterstürzt sind. Diese Modelle würden durch die Anwendung der Clark’s Completion jedoch herausfallen, da keine Loops in dem vorliegenden Programm existieren.  
Letztendlich erhält man hier nicht das gleiche Verhalten wie mit Clingo. 