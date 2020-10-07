## Aufgabe 1.2.a) Zusammenfassung:

### Programme:

Eine Menge von Implikationen.

### Regel / Kopf / Körper:

Jede einzelne Implikationen in einem Programm, welche aus einem Kopf und Körper besteht.

### Fakt:

Körper der Regel ist leer.

### Constraint:

Kopf der Regel ist leer.

### Modelle von Programmen:

Sollen aus jenen Atomen bestehen, die durch das Programm **unterstützt** (supported) und
**begründet** (founded) sind.

### Unterstützt:

Ein Atom in einem Programm heißt so, wenn es im **Kopf** einer **bezüglich M anwendbaren**
Regel steht.

### Anwendbar:

Eine Regel ist **bezüglich M anwendbar**, wenn jedes positive Atom im Körper der Regel in M
ist und keines der negativen Atome im Körper positiv in M ist, dann ist der Kopf in M.

### Begründet:

Ein **Atom** heißt so, falls es sich aus dem bezüglich M reduzierten Programm P^M aus den verbleibenden Fakten und einer Sequenz von Regelanwendungen (per Modus Ponens) ableiten lässt.

### Reduktion P^M:

Jede Regel in P, die ¬b im Körper hat, so dass b ∈ M, wird gelöscht. Aus allen verbleibenden Regeln werdenalle negativen Konjunkte gelöscht.

### Stabiles Modell:

Wenn alle Atome in M unterstützt und begründet sind.