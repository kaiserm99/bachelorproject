
## Aufgabe Nr.3c)

Die Gemeinsamkeiten vom *ASP-Sovler* zum *SAT-Solver* sind z.B., dass beide Implikationen und logische Formeln verwenden um das vorliegende Problem zu beschreiben. 
Man kann ein Programm eines *ASP-Sovler*, welches nur aus "normalen" Regeln besteht, auch in einem  *SAT-Solver* lösen. Die *ASP-Solver* sind jedoch mächtiger. In solchen wird einem viel Schreibaufwand gespart, indem man bestimmte Variablen nicht mal deklarieren muss:

```
name(heinz).
name(fritz).
name(franz).
name(seppl).
verheiratet(fritz).

hat_frau(N) :- name(N), verheiratet(N).
```
In diesem Beispiel kann man erkennen, dass Atom *hat_frau()* nur bei *fritz* erfüllt ist und das *N* hierbei der Platzhalter ist. So muss man nicht jede Implikation aufschreiben. Dies könnte ein *SAT-Solver* aber theoretisch auch, da beim *ASP-Solver* die jeweiligen Atome zuerst *gegrindet* werden und dann wird erst alles gelöst.  

Der für mich wichtigste Unterschied ist, dass man direkt eine Anzahl angeben kann, von denen bestimmte Atome existieren sollen. So haben ich auch das NSP-Problem gelöst. So kann man mit der folgenden Deklaration jeden Krankenpfleger/in genau einer Schicht an dem jeweiligen Tag zuweisen:
```
{ assign(N,S,D) : shift(S) } == 1 :- day(D), nurse(N).
```
Wenn man nun noch jeder Schicht an einem bestimmten Tag noch exakt zwei Krankenpfleger/innen zuweisen möchte, dann kann man folgenden Deklaration verwenden:
```
{ assign(N,S,D) : nurse(N) } == 2 :- day(D), shift(S).
```
  
**Zusammengefasst:** Ein *SAT-Solver* ist die Unterklasse von einem *ASP-Solver*. Der *ASP-Solver* glänzt vor allem mit der Zuweisung von bestimmten Anzahle von Atomen.