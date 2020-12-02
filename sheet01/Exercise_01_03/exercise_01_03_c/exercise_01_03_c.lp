% instance
nurse(heinz).
nurse(fritz).
nurse(udo).
nurse(frida).
nurse(ira).
nurse(nora).

shift(mor).
shift(aft).
shift(nig).

day(one).
day(two).

% Jede Person hat genau eine Schicht am Tag
{ assign(N,S,D) : shift(S) } == 1 :- day(D), nurse(N).

% Jede Schicht wird von zwei Personen übernommen
{ assign(N,S,D) : nurse(N) } == 2 :- day(D), shift(S).

% Frida und Fritz arbeiten niemals in der Nacht
:- assign(fritz,nig,D), day(D).
:- assign(frida,nig,D), day(D).

% Frida und Fritz arbeiten immer zusammen
assign(frida,S,D) :- assign(fritz,S,D), day(D), shift(S).
assign(fritz,S,D) :- assign(frida,S,D), day(D), shift(S).

% Nora arbeitet nur in der Nacht
:- not assign(nora,nig,D), day(D).

% Nora arbitet nur in der Nacht, also arbeitet Ira nie in der Nacht
:- assign(ira,nig,D), day(D).

% Wenn man am zweiten Tag am Morgen arbeiten muss, darf man die Nacht davor nicht gearbeitet haben
not assign(N,nig,one) :- assign(N,mor,two), nurse(N).

#show assign/3.
