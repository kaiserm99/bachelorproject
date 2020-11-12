# Exercise 01 d), Nurse-Scheduling-Problem (NSP)

## Zuerst werden die Variablen der jeweiligen Arbeitsschichten und den jeweiligen Krankenpfleger(innen) zugewiesen:
Dabei wird direkt schon beachtet:

 - Fritz arbeitet niemals Nachts, also arbeit Frida auch niemals Nachts, da sie immer zusammen arbeiten  
 - Nora arbeitet nur Nachts, also arbeitet Ira niemals Nachts, da sie niemals zusammen arbeiten  

#### Alle Arbeitsschichten für den ersten Tag:  

fritzfo, fritzso, fridafo, fridaso, udofo, udoso, udono, irafo, iraso, heinzfo, heinzso, heinzno, norano

#### Alle Arbeitsschichten für den zweiten Tag:  

fritzft, fritzst, fridaft, fridast, udoft, udost, udont, iraft, irast, heinzft, heinzst, heinznt, norant  

## Nun werden die ganzen Bedingungen aufgestellt.  

### Es gibt sechs zu besetzende Arbeitsschichten an einem Arbeitstag und es gibt nur sechs Krankenpfleger(innen). Also muss jeder mindestes einmal am Tag arbeiten:  

- Or(fritzfo, fritzso)
- Or(fritzft, fritzst)
- Or(fridafo, fridaso)
- Or(fridaft, fridast)
- Or(udofo, Or(udoso, udono))
- Or(udoft, Or(udost, udont))
- Or(irafo, iraso)
- Or(iraft, irast)
- Or(heinzfo, Or(heinzso, heinzno))
- Or(heinzft, Or(heinzst, heinznt))
- norano
- norant

### Frida und Fritz arbeiten immer zusammen:   

 - BiImpl(fritzfo, fridafo)
 - BiImpl(fritzso, fridaso)
 - BiImpl(fritzft, fridaft)
 - BiImpl(fritzst, fridast)

### Jeder arbeitet höchstens einmal am Tag:

BiImpl(heinzfo, Not(Or(heinzso, heinzno))) 
BiImpl(heinzso, Not(Or(heinzfo, heinzno))) 
BiImpl(heinzno, Not(Or(heinzfo, heinzno))) 
BiImpl(fridafo, Not(Or(fridaso, fritzso))) 
BiImpl(fridaso, Not(Or(fridafo, fritzfo))) 
BiImpl(udofo, Not(Or(udoso, udono))) 
BiImpl(udoso, Not(Or(udofo, udono))) 
BiImpl(udono, Not(Or(udofo, udoso))) 
BiImpl(irafo, Not(iraso)) 
BiImpl(iraso, Not(irafo))


BiImpl(heinzft, Not(Or(heinzst, heinznt))) 
BiImpl(heinzst, Not(Or(heinzft, heinznt))) 
BiImpl(heinznt, Not(Or(heinzft, heinzst))) 
BiImpl(fridaft, Not(Or(fridast, heinzft))) 
BiImpl(fridast, Not(Or(fridaft, fritzft))) 
BiImpl(udoft, Not(Or(udost, udont))) 
BiImpl(udost, Not(Or(udoft, udont))) 
BiImpl(udont, Not(Or(udost, udoft))) 
BiImpl(iraft, Not(irast)) 
BiImpl(irast, Not(iraft))

**Fritz:**  
 - BiImpl(fritzfo, Not(fritzso))
 - BiImpl(fritzso, Not(fritzfo))
 - BiImpl(fritzft, Not(fritzst))
 - BiImpl(fritzst, Not(fritzft))  

**Frida:**  
 - BiImpl(fridafo, Not(fridaso))
 - BiImpl(fridaso, Not(fridafo))
 - BiImpl(fridaft, Not(fridast))
 - BiImpl(fridast, Not(fridaft))   

**Heinz:**
- BiImpl(heinzfo, Not(Or(heinzso, heinzno)))
- BiImpl(heinzso, Not(Or(heinzfo, heinzno)))
- BiImpl(heinzno, Not(Or(heinzfo, heinzso)))
- BiImpl(heinzft, Not(Or(heinzst, heinznt)))
- BiImpl(heinzst, Not(Or(heinzft, heinznt)))
- BiImpl(heinznt, Not(Or(heinzft, heinzst))) 

**Udo:**  
- BiImpl(udofo, Not(Or(udoso, udono)))
- BiImpl(udoso, Not(Or(udofo, udono)))
- BiImpl(udono, Not(Or(udofo, udoso)))
- BiImpl(udoft, Not(Or(udost, udont)))
- BiImpl(udost, Not(Or(udoft, udont)))
- BiImpl(udont, Not(Or(udoft, udost)))

**Ira:**
- BiImpl(irafo, Not(iraso))
- BiImpl(iraso, Not(irafo))
- BiImpl(iraft, Not(irast))
- BiImpl(irast, Not(iraft))

### In jeder Schicht arbeiten nur zwei Personen zur gleichen Zeit:  

#### Entweder arbeitet Heinz und Nora oder Udo und Nora (Nachts):
- BiImpl(heinzno, Not(udono))
- BiImpl(udono, Not(heinzno))
- BiImpl(heinznt, Not(udont))
- BiImpl(udont, Not(heinznt))

#### Wenn Frida und Fritz Frühschicht/Spätschicht haben, können die Anderen keine Frühschicht/Spätschicht mehr haben:
- Impl(fridafo, Not(Or(heinzfo, Or(udofo, irafo))))
- Impl(fridaso, Not(Or(heinzso, Or(udoso, iraso))))
- Impl(fridaft, Not(Or(heinzft, Or(udoft, iraft))))
- Impl(fridast, Not(Or(heinzst, Or(udost, irast))))

### Wenn jemand Nachtschicht hatte, darf er am darauffolgenden Tag keine Frühschicht haben. Davon sind Heinz und Udo betroffen:

- Impl(heinzno, Not(heinzft))
- Impl(udono, Not(udoft))

### Letztendlich resultiert folgende große Formel aus den oben genannten Annahmen:  

And(Or(fritzfo, fritzso), And(Or(fritzft, fritzst), And(Or(fridafo, fridaso), And(Or(fridaft, fridast), And(Or(udofo, Or(udoso, udono)), And(Or(udoft, Or(udost, udont)), And(Or(irafo, iraso), And(Or(iraft, irast), And(Or(heinzfo, Or(heinzso, heinzno)), And(Or(heinzft, Or(heinzst, heinznt)), And(norano, And(norant, And(BiImpl(fritzfo, fridafo), And(BiImpl(fritzso, fridaso), And(BiImpl(fritzft, fridaft), And(BiImpl(fritzst, fridast), And(BiImpl(heinzfo, Not(Or(heinzso, heinzno))), And(BiImpl(heinzso, Not(Or(heinzfo, heinzno))), And(BiImpl(heinzno, Not(Or(heinzfo, heinzno))), And(BiImpl(fridafo, Not(Or(fridaso, fritzso))), And(BiImpl(fridaso, Not(Or(fridafo, fritzfo))), And(BiImpl(udofo, Not(Or(udoso, udono))), And(BiImpl(udoso, Not(Or(udofo, udono))), And(BiImpl(udono, Not(Or(udofo, udoso))), And(BiImpl(irafo, Not(iraso)), And(BiImpl(iraso, Not(irafo)), And(BiImpl(heinzft, Not(Or(heinzst, heinznt))), And(BiImpl(heinzst, Not(Or(heinzft, heinznt))), And(BiImpl(heinznt, Not(Or(heinzft, heinzst))), And(BiImpl(fridaft, Not(Or(fridast, heinzft))), And(BiImpl(fridast, Not(Or(fridaft, fritzft))), And(BiImpl(udoft, Not(Or(udost, udont))), And(BiImpl(udost, Not(Or(udoft, udont))), And(BiImpl(udont, Not(Or(udost, udoft))), And(BiImpl(iraft, Not(irast)), And(BiImpl(irast, Not(iraft)), And(BiImpl(heinzno, Not(udono)), And(BiImpl(udono, Not(heinzno)), And(BiImpl(heinznt, Not(udont)), And(BiImpl(udont, Not(heinznt)), And(Impl(fridafo, Not(Or(heinzfo, Or(udofo, irafo)))), And(Impl(fridaso, Not(Or(heinzso, Or(udoso, iraso)))), And(Impl(fridaft, Not(Or(heinzft, Or(udoft, iraft)))), And(Impl(fridast, Not(Or(heinzst, Or(udost, irast)))), And(Impl(heinzno, Not(heinzft)), Impl(udono, Not(udoft)))))))))))))))))))))))))))))))))))))))))))))))


# ACHTUNG!!! Passt noch nicht!!!