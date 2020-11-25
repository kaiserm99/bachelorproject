% instance


% encoding
a :- not b.
c :- a.
d :- b, c.
e :- b, not a.
b :- not a.
c :- b, d.
d :- e.
e :- c, d.