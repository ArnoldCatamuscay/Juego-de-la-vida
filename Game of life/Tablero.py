from Celdas import Celda
import numpy as np
import random

class Tablero:
    def __init__(self, cell_colors, cell_dimensions, board_dimensions):
        self.cell_colors = cell_colors
        self.board_dimensions = board_dimensions
        self.cell_dimensions = cell_dimensions
        self.board = [[Celda(cell_dimensions[0], cell_dimensions[1], x, y, cell_colors[0]) for x in range(board_dimensions[0])] for y in range(board_dimensions[1])]

    def inicializar_patron(self, pattern):
        # Inicializar el tablero con un patrón específico
        pass


    # Create a "seed" board of given dimensions at random
    def make_random_board(self, board_dimensions, occupancy):
        # Instantiate the board as a dictionary with a fraction occupied
        # 0 indicates an empty cell; 1 indicates an occupied cell
        for x in range(board_dimensions[0]):
            for y in range(board_dimensions[1]):
                if random.random() < occupancy:
                    self.board[x][y].esta_viva
                else:
                    self.board[x][y].esta_muerta
        # Return the board
        return self.board


    # Update the board according to the rules of the game
    def update_board(self):
        # For every cell in the board...
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # How many occupied neighbors does this cell have?
                neighbors = self.count_neighbors(self.board[i][j], self.board)
                val = self.board[i][j]
                # If the cell is empty and has 3 neighbors, mark it for occupation
                if self.board[i][j].estado == 0 and neighbors == 3:
                    self.board[i][j].estado = 2
                # On the other hand, if the cell is occupied and doesn't have 2 or 3
                # neighbors, mark it for death
                elif self.board[i][j].estado == 1 and not neighbors in [2, 3]:
                    self.board[i][j].estado = -1
        # Now, go through it again, making all the approved changes
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].estado == 2: self.board[i][j].esta_viva 
                if self.board[i][j].estado == -1: self.board[i][j].esta_muerta


    # Return the number of occupied neighbors this cell has
    def count_neighbors(self, cell, board):
        # Figure out the potential neighboring cells (need to watch the edges)
        #            ( i-1       ,   j    ), (     i-1   ,       j-1  ), Estan en desorden
        neighbors = [(cell[0] - 1, cell[1]), (cell[0] - 1, cell[1] - 1),
                    (cell[0], cell[1] - 1), (cell[0] + 1, cell[1] - 1),
                    (cell[0] + 1, cell[1]), (cell[0] + 1, cell[1] + 1),
                    (cell[0], cell[1] + 1), (cell[0] - 1, cell[1] + 1)]
        # For each potential neighbor, if the cell is occupied add one to the score
        score = 0
        for neighbor in neighbors:
            # Is this a real neighbor, or is it out-of-bounds? FRONTERA
            if neighbor in board.keys():
                # Remember that neighbors which are marked for death count, too!
                if board[neighbor] in [1, -1]: score += 1
        # Return the score
        return score


    # Draw the board on the background
    def draw_board(self, board, bg):
        # Draw every cell in the board as a rectangle on the screen
        for cell in board:
            rectangle = (cell[0] * self.cell_dimensions[0], cell[1] * self.cell_dimensions[1],
                            self.cell_dimensions[0], self.cell_dimensions[1])
            pygame.draw.rect(bg, self.colors[board[cell]], rectangle)