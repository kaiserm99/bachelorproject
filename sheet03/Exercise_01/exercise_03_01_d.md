# Aufgabe Nr.1 d)

## Welchen Plan findet Fast Downward?

> start_action tile02 yellow blue (1)
--> tile03 yellow blue (0)
--> tile04 yellow blue (0)
--> tile05 yellow blue (0)
--> tile06 yellow blue (0)
--> tile07 yellow blue (0)
--> tile17 yellow blue (0)
--> tile12 yellow blue (0)
--> tile22 yellow blue (0)
--> tile27 yellow blue (0)
--> tile37 yellow blue (0)
--> tile32 yellow blue (0)
--> tile42 yellow blue (0)
--> tile47 yellow blue (0)
--> tile57 yellow blue (0)
--> tile56 yellow blue (0)
--> tile55 yellow blue (0)
--> tile54 yellow blue (0)
--> tile52 yellow blue (0)
--> tile53 yellow blue (0)
end_action  (0)
start_action tile24 yellow blue (1)
--> tile25 yellow blue (0)
--> tile35 yellow blue (0)
--> tile34 yellow blue (0)
end_action  (0)

**Note:** Des weiteren werden nun Pläne ohne die Aktionen *-->* und *end_action* aufgeschrieben, um die Leserlichkeit zu behalten.

## Ist der Plan korrekt? Ist er optimal?

Ja, dieser Plan ist korrekt und sogar auch optimal. Zuerst wird nämlich der äußere Kreis zu blau gefärbt und daraufhin werden auch die inneren vier Tiles umgefärbt.

## Können Sie das Problem mit anderen Konfigurationen von Fast Downward schneller lösen?

In meiner *domail.pddl* verwende ich conditional effects, weshalb Aufrufe von A* (Stern) mit:
```
$ ./fast-downward.py domain.pddl problem.pddl --search "astar(ipdb())"
$ ./fast-downward.py domain.pddl problem.pddl --search "astar(lmcut())"
```
Nicht möglich sind. Dies wird auch [hier](http://www.fast-downward.org/Doc/Evaluator) bestätigt.

Wenn man jedoch eine Heuristik verwendet und nicht nur den *blinden* A* (Stern) Algorithmus, dann kommt man sehr viel schneller zu einem Ergebnis, jedoch ist dieses dann nicht das Optimale. Dies würde man mit folgenden Aufrufen erreichen:

```
$ ./fast-downward.py domain.pddl problem.pddl --evaluator "hff=ff()" --evaluator \
  "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"
  
$ ./fast-downward.py domain.pddl problem.pddl --evaluator "hcea=cea()" \
  --search "lazy_greedy([hcea], preferred=[hcea])"
```

Wie man aber sehen sehen kann, ist der Plan von folgendem *Kami-Spiel* aber nicht optimal. 

*Spielfeld:*
> GGGGBB
YYYYBB
RRRRBR
BBBBBB
RRRRBR

*Plan nach dem ersten Aufruf:*
> start_action tile50 red blue (1)
start_action tile04 green blue (1)
start_action tile00 red blue (1)
start_action tile02 red blue (1)
start_action tile03 yellow blue (1)
start_action tile52 red blue (1)

*Ein Optimaler Plan:*
> start_action tile40 blue red (1)
> start_action tile04 green red (1)
> start_action tile03 yellow red (1)

**Zusammengefasst:** Ja, man kann das Problem mit einer anderen Konfiguration schneller lösen, wie man aber sehen kann, leidet die Optimalität des Plans aber darunter.

## Können Sie durch Änderungen der Modellierung in PDDL die Planung beschleunigen?

Mit der Einführung der Aktionen-Kosten wurde die Lösung des im ÜB vorgegebenen Problems enorm gesteigert.
Mir fällt nun leider keine Optimierungsmöglichkeit mehr ein, ansonsten hätte ich diese auch direkt einfließen lassen. Wenn dann müsste man die Sprache an sich abändern, damit mehr Möglichkeiten vorhanden wären.