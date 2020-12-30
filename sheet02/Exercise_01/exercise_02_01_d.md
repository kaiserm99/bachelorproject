
## Aufgabe Nr.2 d)

### Verbesserung der Computing Time:
Jedes Mal, wenn eine weitere Zelle ausgewählt wird, erhält man logischerweise auch mehr Informationen über die jeweiligen Mienen. Im richtigen Spiel kann man dann Felder mit einer Flag bestücken, an denen zu 100 % eine Mine sein muss. Dies wird in unserer Implementation nicht gemacht. Somit bleiben Constraints in dem CSP, owohl man diese auch als Bomben markieren könnte. Könnte man das CSP ohne diese Constraints lösen, wäre die Computing Time nicht so hoch und man könnte die nächsten Zellen schneller auswählen.

### Verbesserung von bestimmten Situationen (Extremfälle):
In unserer Implementation startet man immer mit dem (0, 0)-Feld, was zunächst kein Problem darstellt, da das erste Feld immer irgendwie ausgewählt werden muss und sich direkt schon eine Mine darunter befindet. Nehmen wird nun aber an, dass folgendes vereinfachte Spielfeld vorliegt:
> _ _ _ x _  
> _ _ _ x _  
> x x x x _  
> _ _ _ _ \_  

Hier stellen zum einen die "_"-Symbole die Felder dar, welche keine Minen enthalten. Die Felder mit den "x"-Symbolen repräsentieren dabei die Felder mit den Minen untendrunter.  
Wenn man nun in mit dem bereis erwähnten (0, 0)-Feld beginnt, kommt man letztendlich zu einem "Deadlock". Nämlich dann würde das Feld wie folgt aussehen:
> 0 0 2 x _  
> 2 3 5 x _  
> x x x x _  
> _ _ _ _ \_ 

Und es gäbe mit unserer Implementation keine Lösung mehr. Man müsste nun zufällig ein weiteres Feld auswählen, da das CSP mit den aktuellen Constraints keine Lösung mehr erzielen kann. Dies wäre eine Idee unsere Implementierung zu verbessern.

**Achtung:**  
Dies funktioniert auch nicht bei eingeschlossenen Feldern, also würde folgendes Spielfeld ebenso nicht zu einem Ergebnis führen:
> _ _ _ _ \_  
> _ x x x \_  
> _ x _ x _  
> _ x x x _  
> _ _ _ _ \_  

Hier müsste man ebenfalls zufällig ein Wert im mittleren der Bomben auswählen. Diese Extremfälle müssten auf jeden Fall noch beachtet werden.


### Unmöglich zum Entschiedene Probleme:

Nehmen wir nun folgendes Beispiel-Spielfeld an:

> 0 1 2 3 2 1  
 0 2 X X X 2  
 1 3 X 5 X 2  
 2 X 5 5 3 2  
 2 X X X X 1  
 1 2 3 3 2 1  

Unsere Implementation scheitert bei diesem Feld, da nicht genügend Informationen vorliege. Bei der Auswahl, welche Zelle als nächstes ausgewählt werden soll, werden die Lösungen gezählt, in denen die jeweilige Zelle keine Mine enthält. Es kann jedoch sein, dass nicht nur eine Zelle die höchste Anzahl von keinen Minen in der Lösung hat, sondern mehrere. Hier wird z.B. die (4,3)-Zelle ausgewählt:

> 0  1  2  .  .  .   
 0  2  .  .  .  .   
 1  3  .  5  .  .   
 2  .  5  .  .  .   
 2  .  .  .  .  .   
 1  2  3  .  .  .   

... welche jedoch eine Mine enthält und so das Spiel verloren ist. Hätte man hier aber das (0,3)-Feld ausgewählt, dann hätte man mehr wertvolle Informationen bekommen und hätte letztendlich das Spiel gewinnen können.  
Leider kann man diese Entscheidung nie begründen und man kann sie nicht durch logische Fakten begründen, weshalb weitere Verbesserungen nicht möglich sind. Dieses Spiel basiert zum größten Teil einfach noch auf Wahrscheinlichkeiten und kann niemals perfekt gespielt werden.
