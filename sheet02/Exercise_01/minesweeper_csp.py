#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Bachelor-project - Foundations of Artificial Intelligence

Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Description:
    This file is for solving the given minesweeper board by creating
    the necessary constraints. It can't be perfect because of the
    probability of the mines, but there is more in the the exercise
    d) to read about.

Usage:
    This file is only imported and can't be use by itself, otherwise
    it wouldn't function.

"""

from constraint import *
import operator
from minesweeper_board import *

class Csp:
    
    def __init__(self, board):
        self.board = board
        self.fringe = board.get_fringe_cells()
        self.csp_to_grid = {}
        self.grid_to_csp = {}
        for i in range(len(self.fringe)):
            self.csp_to_grid[i] = self.fringe[i]
            self.grid_to_csp[self.fringe[i]] = i
            
        self.problem = Problem()
        self.add_variables()
        self.add_mines_constraint()
        for cell in self.board.get_fringe_neighbors():
            self.add_cell_constraints(cell[0], cell[1])
        
        # Gibt eine mögliche Lösung des CSP zurück
    def get_solution(self):
        return self.problem.getSolution()
    
    # Gibt alle möglichen Lösung des CSP zurück
    # Achtung: Dies kann dauern!
    def get_solutions(self):
        return self.problem.getSolutions()
    
    
    ############################ TODO #################################
    # Die folgenden Funktionen sind zu implementieren.
    ###################################################################
    
    # TODO: Füge für jede Zelle des Randgebiets eine neue Variable hinzu mit Wertebereich {0,1},
    # wobei 0 für keine Bombe und 1 für eine Bombe im dazugehörigen Feld
    # steht
    def add_variables(self):
        lst = [(cell[0], cell[1]) for cell in self.fringe]

        self.problem.addVariables(lst, [0, 1])


    # TODO: Füge eine Bedinung hinzu, welche fordert, dass für jedes aufgedeckte Feld, das an 
    # ein Randfeld angrenzt, die Zahl, die in diesem Feld angezeigt wird, die Summe der Minen in 
    # den angrenzenden verdeckten Feldern entspricht. Folgende funktionen können interessant sein
    # - self.board.get_cell_content(x,y): Zahl im Feld (x,y)
    # - self.board.get_neighbors(x,y): Nachbarzellen von (x,y)
    # - self.board.is_cell_at_fringe(x',y'): Ist (x',y') Teil des Randgebietes?
    # Hierfür kann der ExactSumConstraint verwendet werden
    def add_cell_constraints(self, x, y):
        # Get all the neighbours which are not expanded now
        acc_cells = []

        for n_cell in self.board.get_neighbors(x, y):
            if self.board.is_cell_at_fringe(n_cell[0], n_cell[1]):
                acc_cells.append((n_cell[0], n_cell[1]))

        value = self.board.get_cell_content(x, y)  # Get the value of the current cell

        self.problem.addConstraint(ExactSumConstraint(value), acc_cells)


    # TODO: Die Anzahl an Felder mit einer Bombe (Randgebiet) entspricht maximal der 
    # Bombenanzahl im Spiel 
    # Hierfür kann der MaxSumConstraint verwendet werden
    def add_mines_constraint(self):
        self.problem.addConstraint(MaxSumConstraint(self.board.num_bombs), self.fringe)

    
    # TODO: Berechne das Feld, welches als nächstes aufgedeckt werden soll
    # Hierbei sollen alle möglichen Lösungen berücksichtig werden, 
    # und das vielversprechendste Feld zurück gegeben werden.
    # In anderen Worten, es soll ein Feld gewählt werden, das in jeder/in den
    # meisten Lösungen keine Bombe enhält.
    # Mit self.get_solutions() bekommt man alle Lösungen des aktuellen CSP
    # Mit self.board.get_fringe_cells() erh#lt man alle Randzellen
    def next_cell(self):
        count_cell = {}

        for sol in self.problem.getSolutions():

            # A cell is in the Formation: Cell, value
            for cell in sol.items():

                # When the value is 0 at the cell there should be no bomb so increment the accumulator
                if cell[1] == 0:
                    count_cell[cell[0]] = count_cell.get(cell[0], 0) + 1

     
        # Return the cell wich the least bombs in all the solutions
        return max(count_cell, key=count_cell.get)
