## Kurze Anmerkung zu der Bearbeitung der Aufgabe Nr. 2:


### Vorwort und "dummer" Fehler meinerseits:
Ich habe die Aufgabe *Nr.2 b)* falsch verstanden, wodurch ich einen komplett  neuen Parser geschrieben hat, der nicht das gewünschte Format, sondern eines für mich ersichtlicheres Format eines Programms akzeptiert. Ich habe dachte, dass die Konjunktion von Implikationen das in Aufgabe *Nr. 2 a)* beschriebene ist und dann mit Kommas getrennt werden. Über den Syntax der akzeptierenden Programme komme ich gleich nochmal zurück.  
Falls dies dennoch ein fataler Fehler sein könnte, dann könnte ich mit wenigen Zeilen Code die Konjunktion von Implikationen in das benötigte Format umwandeln. Dies finde ich jedoch aber nicht wirklich von Sinnen, da das aktuelle Format für mich sinnvoller ist. Dennoch würde ich das natürlich sofort änder, um die Aufgabe zu bestehen.

### Syntax des nicht der Aufgabenstellung entsprechenden Programms:
Grammatik der Programme:
```
str  -> a | b | c | ...  
atom -> Not(str) | str  
body -> str | And(atom, atom) | And(... And(atom, atom), ...)
head -> str

Implication -> Impl(body, head)
Program     -> Implication | Implication, Implication, ...
```
Beispiele für die Programme:
```
1. "Impl(Not(b), a), Impl(Not(a), b)"
2. "Impl(Not(b), a), Impl(Not(a), b), Impl(Not(a), c), Impl(d, c), Impl(And(a, b), d)"
```

... letztendlich sind die Implikationen einfach nicht in den Konjunktionen mit drin, sondern jede Implikation ist mit einem Komma getrennt. 

### Skript zu get_models.sh:
Dieses Skript ist nicht teil der Aufgabe, wird aber von Skripten in anderen Aufgaben verwendet, um deren Richtigkeit zu beweisen. Somit wäre es gut, dieses nicht zu löschen, da ansonsten Exercise_01_04/proof_exerercise.sh nicht funktionieren würde.  
Ebenfalls kann dieses aber auch zum Kontrollieren verwendet werden, da man so direkt alle stabilen Modelle des gegeben Programms ausgeben kann.

### Hilfsdatei helping_stable.py:
Diese Datei wird einfach nur von dem Hauptskript **stable_models.py** verwendet, da sie einige wichtige Funktionen zum Parsen des Programmes hat.