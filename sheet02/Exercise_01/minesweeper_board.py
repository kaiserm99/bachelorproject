import random

BOMB = "X"
COVERED = "."

class Board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_bombs = 0
        self.board = [[0 for i in range(self.width)] for j in range(self.height)]
        self.covered_board = [[COVERED for i in range(self.width)] for j in range(self.height)]
        self.fringe = []
    
    # Sind alle Felder ohne Bombe aufgedeckt? Falls ja, ist das Spiel
    # gewonnen
    def is_solved(self):
        for x in range(self.width):
            for y in range(self.height):
                if not self.is_cell_uncovered(x,y) and self.board[x][y] != BOMB:
                    return False
        return True
    
    def random_board(self, num_bombs):
        fields = []
        for x in range(self.width):
            for y in range(self.height):
                fields += [(x,y)]
        fields = fields[1:]
        mine_fields = random.sample(fields, num_bombs)
        for mine in mine_fields:
            self.insert_bomb(mine[0], mine[1])
        
        
    def insert_bomb(self, x, y):
        if self.board[x][y] == BOMB:
            return
        self.board[x][y] = BOMB
        self.num_bombs += 1
        
        self.increase_bomb_counter(x-1,y-1)
        self.increase_bomb_counter(x,y-1)
        self.increase_bomb_counter(x+1,y-1)
        self.increase_bomb_counter(x-1,y)
        self.increase_bomb_counter(x+1,y)
        self.increase_bomb_counter(x-1,y+1)
        self.increase_bomb_counter(x,y+1)
        self.increase_bomb_counter(x+1,y+1)
        
    def increase_bomb_counter(self, x, y):
        if x < 0 or x >= self.width:
            return
        if y < 0 or y >= self.height:
            return
        if self.board[x][y] != BOMB:
            self.board[x][y] += 1
            
    # Deckt die aktuelle Zelle auf und updated alle anderen
    def uncover_cell(self, x, y):
        if self.board[x][y] == BOMB:
            return False
        
        queue = set([(x,y)])
        closed = set()
        while len(queue) > 0:            
            cur = list(queue)[0]
            queue.discard(cur)
            if cur in closed:
                continue
            closed.add(cur)
            
            cur_x = cur[0]
            cur_y = cur[1]
            self.covered_board[cur_x][cur_y] = self.board[cur_x][cur_y]
                        
            if self.board[cur_x][cur_y] == 0:
                cur_neighbors = set(self.get_neighbors(cur_x,cur_y))
                cur_neighbors = cur_neighbors - closed

                queue = queue | cur_neighbors
        return True
            
    def dump(self, uncovered=False):
        cur_board = self.covered_board
        if uncovered:
            cur_board = self.board
            
        for row in cur_board:
            for cell in row:
                if cell == BOMB:
                    print(" X", end = " ")
                elif cell == COVERED:
                    print(" .", end = " ")
                else:
                    print("%2d" % cell, end = " ")
            print()
    

    ###################### Helper Functions ###########################
    # Diese Funktionen können genutzt werden um hilfreiche und "legale"
    # Information über das Board zu erhalten.
    ###################################################################
        
    # Gibt den sichtbaren Feldinhalt/Feldlabel zurück
    def get_cell_content(self, x, y):
        return self.covered_board[x][y]
    
    # Ist diese Zelle aufgedeckt?
    def is_cell_uncovered(self, x, y):
        return self.covered_board[x][y] != COVERED
    
    # Is diese Zelle teil des Randgebiets?
    def is_cell_at_fringe(self, x, y):
        if self.is_cell_uncovered(x,y):
            return False
        for n in self.get_neighbors(x,y):
            if self.is_cell_uncovered(n[0],n[1]):
                return True
        return False
    
    # Gibt eine Liste von allen Zellen des Randgebiets zurück
    def get_fringe_cells(self):
        result = []
        for x in range(self.width):
            for y in range(self.height):
                if self.is_cell_at_fringe(x,y):
                    result += [(x,y)]
        return result
    
    def get_fringe_neighbors(self):
        result = []
        for x in range(self.width):
            for y in range(self.height):
                if self.is_cell_uncovered(x,y):
                    neighbors = self.get_neighbors(x,y)
                    for n in neighbors:
                        if self.is_cell_at_fringe(n[0],n[1]):
                            result += [(x,y)]
                            break
        return result
    
    # Gibt eine Liste von Nachbarzellen zurück
    def get_neighbors(self, x, y):
        neighbors = []
        neighbors += [(x-1,y-1)]
        neighbors += [(x,y-1)]
        neighbors += [(x+1,y-1)]
        neighbors += [(x-1,y)]
        neighbors += [(x+1,y)]
        neighbors += [(x-1,y+1)]
        neighbors += [(x,y+1)]
        neighbors += [(x+1,y+1)]
        valid_neighbors = []
        for n in neighbors:
            if n[0] < 0 or n[0] >= self.width:
                continue
            if n[1] < 0 or n[1] >= self.height:
                continue
            valid_neighbors += [n]
        return valid_neighbors    
