from Celdas import Celda
import numpy as np
import random, pygame

class Tablero:
    def __init__(self, cell_colors, cell_dimensions, board_dimensions, occupancy):
        self.cell_colors = cell_colors
        self.board_dimensions = board_dimensions
        self.cell_dimensions = cell_dimensions
        self.occupancy = occupancy
        self.board = [[Celda(cell_dimensions[0], cell_dimensions[1], x, y, cell_colors[0]) for x in range(board_dimensions[0])] for y in range(board_dimensions[1])]

    def inicializar_patron(self, pattern):
        if pattern == "random":
            print("Patron: " + pattern)
            self.make_random_board()


    # Create a "seed" board of given dimensions at random
    def make_random_board(self):
        # Instantiate the board as a dictionary with a fraction occupied
        # 0 indicates an empty cell; 1 indicates an occupied cell
        for x in range(self.board_dimensions[0]):
            # print("\n")
            for y in range(self.board_dimensions[1]):
                if random.random() < self.occupancy:
                    self.board[x][y].esta_viva()
                else:
                    self.board[x][y].esta_muerta()
                # print("Tablero: " + str(self.board[x][y].estado) + ", ", end='')
        # Return the board
        return self.board


    # Update the board according to the rules of the game
    def update_board(self):
        # For every cell in the board...
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # How many occupied neighbors does this cell have?
                neighbors = self.count_neighbors(self.board[i][j])
                estado = self.board[i][j].estado
                # If the cell is empty and has 3 neighbors, mark it for occupation
                if estado == 0 and neighbors == 3:
                    estado = 2
                # On the other hand, if the cell is occupied and doesn't have 2 or 3
                # neighbors, mark it for death
                elif estado == 1 and not neighbors in [2, 3]:
                    estado = -1
        # Now, go through it again, making all the approved changes
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].estado == 2: self.board[i][j].esta_viva()
                if self.board[i][j].estado == -1: self.board[i][j].esta_muerta()


    # Return the number of occupied neighbors this cell has
    def count_neighbors(self, cell):
        # Figure out the potential neighboring cells (need to watch the edges)
        # cell es self.board[i][j]
        #            (     i-1   ,   j-1      ),(     i-1   ,     j  ), (  i-1    ,   j+1   )
        neighbors = [(cell.pos_x - 1, cell.pos_y - 1),(cell.pos_x - 1, cell.pos_y), (cell.pos_x - 1, cell.pos_y + 1),
                    (cell.pos_x, cell.pos_y - 1),(cell.pos_x, cell.pos_y + 1),
                    (cell.pos_x + 1, cell.pos_y - 1),(cell.pos_x + 1, cell.pos_y), (cell.pos_x + 1, cell.pos_y + 1)]
        # For each potential neighbor, if the cell is occupied add one to the score
        score = 0
        for neighbor in neighbors:
            # Is this a real neighbor, or is it out-of-bounds? FRONTERA
            if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < self.board_dimensions[0] and neighbor[1] < self.board_dimensions[1]:
                # Remember that neighbors which are marked for death count, too!
                if self.board[neighbor[0]][neighbor[1]].estado in [1, -1]: score += 1
        # Return the score
        return score


    # Draw the board on the background
    def draw_board(self, bg):
        # Draw every cell in the board as a rectangle on the screen
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # rectangle = (self.board[0] * self.cell_dimensions[0], self.board[1] * self.cell_dimensions[1],
                #                 self.cell_dimensions[0], self.cell_dimensions[1])
                rectangle = (self.board[i][j].pos_x * self.cell_dimensions[0], self.board[i][j].pos_y * self.cell_dimensions[1], self.cell_dimensions[0], self.cell_dimensions[1])
                pygame.draw.rect(bg, self.cell_colors[self.board[i][j].estado], rectangle)# pygame.draw.rect(bg, self.cell_colors[self.board[i][j].color], rectangle)
