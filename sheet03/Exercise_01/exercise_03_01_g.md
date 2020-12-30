
## Aufgabe Nr.1 g)  

### Was haben Sie in dieser Aufgabe gelernt?  
In der Aufgabe hab ich den Umgang mit pddl gelernt. Im Internet gab es dabei nicht so gute und hilfreiche Tutorials wie bei sonstigen Sprachen. Dennoch konnte ich mithilfe von dem [Planning Wiki](https://planning.wiki/) und auch der [AI-Planning Vorlesung](http://gki.informatik.uni-freiburg.de/teaching/ws2021/aip/) das nötige Wissen erlangen.

### Welche weiteren Optimierungen wären denkbar?  
Die meisten Optimierungen die mir bisher eingefallen sind, habe ich schon direkt schon eingebaut, somit ist es schwer noch mit neuen Optimierungsideen aufzukommen.  

Ich verwende in meiner Domain das Prinzip des [Floodfills](https://de.wikipedia.org/wiki/Floodfill), welche aus einer startend Funktion, dem eigentlichen Floodfill und einer abschließenden Funktion besteht. Dieses System hätte man auch mit *derived predicates* austauschen können. Dann hätte man immer eine komplette Gruppe von aneinanderlegenden, gleichfarbigen Tiles. Diese hätten dann beim eigentlichen planning sehr viel schneller verarbeitet werden können, jedoch dauert es auch seine Zeit, biss alle Axiome erstellt wurden.  

Ebenso besteht wie in [Aufgabe Nr.1 d)](exercise_03_01_d.md) bereits erwähnt noch das Problem mit den bedingten Effekten, also den *when-Ausdrücken*. Durch diese kann man entweder die langsame blinde Heuristik auf den A* (Stern) Algorithmus anwenden oder man verwendet eine nicht konsistente Heuristik, welche dann einen nicht optimalen Plan zurückgibt.  
Somit hat man also das Problem, dass die Suche entweder viel Computing Time benötigt oder der gegebene Plan nicht optimal ist.

### Welche Optimierungen könnten in PDDL durchgeführt werden?  
Die *derived predicates* könnte man auf jeden Fall noch in das pddl einbauen. Die andere Optimierungsidde ist leider nicht möglich bzw. ich kann mir nicht vorstellen, wie man das implementieren sollte.


### Welche wären eher in einem spezialisierten Kami-Löser umsetzbar?  
Der Knackpunkt sind die Gruppe von nebeneinander liegenden und gleichfarbigen Tiles, welche man durch *forall* und *when-Ausdrücken* immer neu erstellen muss, basierend auf dem aktuellen Zustand. Hätte man einen Rechner, welcher nur die Gruppen betrachtet und man alles nicht auf die einzelnen Tiles runterbrechen müsste, wäre dies viel effektiver. Dies ist aber bei der Verwendung von pddl nicht möglich.