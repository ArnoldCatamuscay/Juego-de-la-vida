import random, pygame

class Tablero:
    def __init__(self, cell_colors, cell_dimensions, board_dimensions, occupancy):
        self.colors = cell_colors
        self.board_dimensions = board_dimensions
        self.cell_dimensions = cell_dimensions
        self.occupancy = occupancy
        self.board = dict()


    def inicializar_patron(self, pattern):
        if pattern == "random":
            self.make_random_board()


    def make_random_board(self):
        # 0 indicates an empty cell; 1 indicates an occupied cell
        for x in range(self.board_dimensions[0]):
            for y in range(self.board_dimensions[1]):
                if random.random() < self.occupancy:
                    self.board[(x % self.board_dimensions[0], y % self.board_dimensions[1])] = 1
                else:
                    self.board[(x % self.board_dimensions[0], y % self.board_dimensions[1])] = 0


    # Update the board according to the rules of the game
    def update_board(self):
        # For every cell in the board...
        for cell in self.board:
            # How many occupied neighbors does this cell have?
            neighbors = self.count_neighbors(cell)
            val = self.board[cell]
            # print ('(%d\t%d)\t\r'%(val,neighbors))
            # If the cell is empty and has 3 neighbors, mark it for occupation
            if self.board[cell] == 0 and neighbors == 3:
                self.board[cell] = 2
            # On the other hand, if the cell is occupied and doesn't have 2 or 3
            # neighbors, mark it for death
            elif self.board[cell] == 1 and not neighbors in [2, 3]:
                self.board[cell] = -1
        # Now, go through it again, making all the approved changes
        for cell in self.board:
            if self.board[cell] == 2: self.board[cell] = 1
            if self.board[cell] == -1: self.board[cell] = 0


    # Return the number of occupied neighbors this cell has
    def count_neighbors(self, cell):
        # Figure out the potential neighboring cells (need to watch the edges)
        neighbors = [(cell[0] - 1, cell[1]), (cell[0] - 1, cell[1] - 1),
                    (cell[0], cell[1] - 1), (cell[0] + 1, cell[1] - 1),
                    (cell[0] + 1, cell[1]), (cell[0] + 1, cell[1] + 1),
                    (cell[0], cell[1] + 1), (cell[0] - 1, cell[1] + 1)]
        # Modify the neighbors position if it is out of the limits
        for i in range(len(neighbors)):
            if neighbors[i][0] < 0:
                neighbors[i] = (self.board_dimensions[0] - 1, neighbors[i][1])
            if neighbors[i][1] < 0:
                neighbors[i] = (neighbors[i][0], self.board_dimensions[1] - 1)
            if neighbors[i][0] >= self.board_dimensions[0]:
                neighbors[i] = (0, neighbors[i][1])
            if neighbors[i][1] >= self.board_dimensions[1]:
                neighbors[i] = (neighbors[i][0], 0)
        # For each potential neighbor, if the cell is occupied add one to the score
        score = 0
        for neighbor in neighbors:
            # Is this a real neighbor, or is it out-of-bounds? FRONTERA
            if neighbor in self.board.keys():
                # Remember that neighbors which are marked for death count, too!
                if self.board[neighbor] in [1, -1]: score += 1
        # Return the score
        return score


    # Draw the board on the background
    def draw_board(self, bg):
        # Draw every cell in the board as a rectangle on the screen
        for cell in self.board:
            rectangle = (cell[0] * self.cell_dimensions[0], cell[1] * self.cell_dimensions[1],
                            self.cell_dimensions[0], self.cell_dimensions[1])
            pygame.draw.rect(bg, self.colors[self.board[cell]], rectangle)