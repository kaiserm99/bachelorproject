#!/usr/bin/env python3

"""
	The following function tj() was nearly fully coppied by me. There are only few changes I did
	myselfe. I couldn't code a better implementation of this Algorithm by myself, so I copied it
	from Wikipedia. Here is the link:

	https://de.wikipedia.org/wiki/Algorithmus_von_Tarjan_zur_Bestimmung_starker_Zusammenhangskomponenten

	This Code was originally written by the Wikipedia User:

		Username: Heronils
		Name: Nils-Hero Lindemann
		E-Mail: nilsherolindemann@tutanota.com

	
	Authors: 
	
		Nils-Hero Lindemann <nilsherolindemann@tutanota.com>
		Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

"""
# tarjan.py, written on: Dienstag,  17 Oktober 2020.


class Knoten:
    
    def __init__(self, name, edges):
        self.name = name
        self.edges = []

        self.add_edges(edges)

        self.index = 0
        self.szkindex = 0
        self.besucht = False

    def add_edges(self, edges):
        for e in edges:

            if self.name != e and e not in self.edges:
                self.edges.append(e)


    def __repr__(self):
        return str(self.edges)


def tj(graph):
    if not graph:
        return

    knotenzähler = 0
    pfad, schnellzugriff = [], set()
    besucht = not next(iter(graph.values())).besucht


    def besuche(knotenname):
        nonlocal knotenzähler

        # Diesen Knoten besuchen
        knoten = graph[knotenname]
        knoten.index = knotenzähler
        knoten.szkindex = knotenzähler
        knotenzähler += 1
        pfad.append(knotenname); schnellzugriff.add(knotenname)
        knoten.besucht = besucht

        # Nachbarknoten besuchen
        for kante in knoten.edges:
            nächster = graph[kante]
            if nächster.besucht != besucht:
                besuche(kante)
                knoten.szkindex = min(knoten.szkindex, nächster.szkindex)
            elif kante in schnellzugriff:
                knoten.szkindex = min(knoten.szkindex, nächster.index)

        # SZKs ausgeben
        if knoten.szkindex == knoten.index:
            szk = []
            while True:
                pfadknotenname = pfad.pop(); schnellzugriff.remove(pfadknotenname)
                szk.append(pfadknotenname)
                if pfadknotenname == knotenname:
                    break
            if len(szk) > 1:  # Wir sind hier nur an SZKs interessiert die mehr als einen Knoten enthalten
                szk.reverse()
                print(f'starke Zusammenhangskomponente: {szk}')

    for knotenname in graph:
        besuche(knotenname)
