
## Aufgabe Nr.2 c)

### 1. Ist jeder, der in Freiburg wählen darf EU-Bürger?
Diese Frage kann mit HermiT beantwortet werden, indem man einfach alle Instanzen von Personen in Freiburg wählen dürfen, also alle Instanzen in der Klasse *CanVoteInFreiburg* geschnitten mit allen Instanzen der Klasse *Not-EU-Citizen*.  
Würde in diesem Schnitt ein Ergebnis herauskommen, dann würde es eine in Freiburg wahlberechtigte Person geben, welche kein EU-Bürger wäre. Mit der folgenden DL-Querry:
```
CanVoteInFreiburg and (isCitizenOf some Not-EU-Country)
```
... wird jedoch klar, dass keine Personeninstanz herauskommt und die äquivalente Klasse gerade *owl:Nothing*  ist.  
Somit muss also jede wahlberechtigte Person in Freiburg auch ein EU-Bürger sein.

### 2. Ist jeder, der in Freiburg wählen darf auch Deutscher?
In Freiburg wählen darf letztendlich jeder EU-Bürger, welcher in einem Stadtteil von Freiburg lebt und mindestens schon 16 Jahre alt ist. Würde man nun nur die Beispiel Personeninstanzen betrachten, könnte man diese Frage nicht unbedingt beantworten, da diese Personeninstanz durch *isCitizenOf Germany* ihre EU-Mitgliedschaft erhalten hätte. Somit würde die folgende DL-Querry:
```
CanVoteInFreiburg and (isCitizenOf value Germany)
```
... genau die gleichen Instanzen enthalten, als hätte man alle in Freiburg wahlberechtigten Personen ausgegeben. 

Wenn man jedoch eine weitere Person hinzufügt, welche durch *isCitizenOf France* ihre EU-Mitgliedschaft erhält, in einem Stadtteil von Freiburg lebt und über dem geforderten Mindestalter von 16 Jahren ist, kann man mit der folgenden DL-Querry:
```
CanVoteInFreiburg and (isCitizenOf value France)
```
... eine Personeninstanz erhalten. Somit ist also nicht jede in Freiburg wahlberechtigte Person automatisch ein Deutscher Staatsbürger.


### 3. Ist jeder, der in Freiburg wählen darf auch Freiburger?
Um dies zu zeigen, müsste man die Klasse aller in Freiburg wahlberechtigten Personen mit allen Personen die in keinem Stadtteil von Freiburg leben schneiden. HermiT kann leider nicht bei nicht-existenz weiterhelfen, somit funktioniert folgende DL-Querry nicht:
```
CanVoteInFreiburg and not (isLinvingIn some DistrictOfFreiburg)
```
Man kann jedoch einen anderen Weg gehen und alle in Freiburg wahlberechtigten Personen mit allen Personen, welche auch in einem Stadtteil von Freiburg wohnen, schneiden. Also folgende DL-Querry:
```
CanVoteInFreiburg and (isLinvingIn some DistrictOfFreiburg)
```
Diese Anfrage ist äquivalent zu *CanVoteInFreiburg* nach HermiT, womit man also erkennen kann, dass jede in Freiburg wahlberechtigte Person auch in einem Stadtteil von Freiburg lebt.

### 4. Ist jeder, der in Freiburg wählen darf auch Wiehremer?
HermiT kann leider nicht bei nicht-existenz von Werten weiterhelfen, sondern man brauch explizite Klassen.  Somit ist folgende DL-Querry:
```
CanVoteInFreiburg and not (isLinvingIn value Wiehre)
```
... nicht zulässig, da explizierte Klassen erforderlich sind. Diese habe ich aber nicht in meine Ontologie mit eingebaut. Somit müssen wir einen Umweg gehen und eine Personeninstanz erstellen, welche in Freiburg wahlberechtigt ist und dabei z.B. in Betzenhausen lebt. Somit könnte man dann mit der DL-Querry:
```
CanVoteInFreiburg and (isLinvingIn value Betzenhausen)
```
... eine Personeninstanz erhalten. Somit erhalten wir eine in Freiburg wahlberechtigte Person, welche nicht in Wiehre lebt. Also ist somit nicht jeder, der in Freiburg wählen darf auch Wiehremer.

### 5. Besteht Frauenwahlrecht?
Nun gilt es die Klasse der in Freiburg wahlberechtigten Personen mit dem Geschlecht Attribut zu schneiden. Falls dieser Schnitt nicht leer ist, dann darf man in Freiburg auch als Frau wählen. Mit der folgenden DL-Querry:
```
CanVoteInFreiburg and (genderOfPerson value "Female")
```
... erhalten wir eine weibliche Personeninstanz. Somit dürfen auch diese Personen in Freiburg wählen und damit ist auch gegeben, dass Frauenwahlrecht besteht.

### 6. Dürfen Schweizer wählen?
Um zu überprüfen, ob ein Schweizer auch in Freiburg wählen darf, muss im folgenden den Schnitt zwischen allen in Freiburg wahlberechtigten Personen und allen Personen mit der Schweizer Staatsbürgerschaft machen. Mit der folgenden DL-Querry:
```
CanVoteInFreiburg and (isCitizenOf value Switzerland)
```
... erhalten wir jedoch keine Personeninstanz. Jedoch löst HermiT diese Querry zu der äquivalenten Klasse *owl:Nothing* auf. Somit kann es also keine Person mit Schweizer Staatsbürgerschaft geben, welche in Freiburg wählen dürfte.