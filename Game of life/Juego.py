import pygame, sys
from pygame.locals import *
from Tablero import Tablero

class Juego:
    def __init__(self, title, version, cell_dimensions, framerate, occupancy, colors, board_dimensions):
        self.title = title
        self.version = version
        self.cell_dimensions = cell_dimensions
        self.framerate = framerate
        self.occupancy = occupancy
        self.colors = colors
        self.tablero = Tablero(colors, cell_dimensions, board_dimensions)


    def ejecutar_juego(self):
        # Initialize pygame elements
        screen, bg, clock = self.init_pygame(self.tablero.board_dimensions, self.title, self.version, self.cell_dimensions)
        # Initialize random board
        board = self.make_random_board(self.tablero.board_dimensions, self.occupancy)
        # Enter the game loop
        quit_game = False
        while not quit_game:
            # Slow things down to match the framerate
            clock.tick(self.framerate)
            # Update the board
            self.update_board(board)
            # Draw the board on the background
            self.draw_board(board, bg)
            # Blit bg to the screen, flip display buffers
            screen.blit(bg, (0, 0))
            pygame.display.flip()
            # Queue user input to catch QUIT signals
            for e in pygame.event.get():
                if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                # if e.type == QUIT:
                #     quit_game = True
        # Print farewell message
        print("Thanks for watching!")


    # Initialize pygame elements
    def init_pygame(self, board_dimensions, title, version, cell_dimensions):
        # Initialize the pygame modules
        pygame.init()
        # Determine and set the screen dimensions
        dimensions = (board_dimensions[0] * cell_dimensions[0],
                        board_dimensions[1] * cell_dimensions[1])
        screen = pygame.display.set_mode(dimensions)
        # Set the title string of the root window
        pygame.display.set_caption(title + " " + version)
        # Grab the background surface of the screen
        bg = screen.convert()
        # Grab the game clock
        clock = pygame.time.Clock()
        # Return the screen, the background surface, and the game clock
        return screen, bg, clock

    # # Create a "seed" board of given dimensions at random
    # def make_random_board(self, board_dimensions, occupancy):
    #     # Instantiate the board as a dictionary with a fraction occupied
    #     # 0 indicates an empty cell; 1 indicates an occupied cell
    #     board = self.tablero.board
    #     for x in range(board_dimensions[0]):
    #         for y in range(board_dimensions[1]):
    #             if random.random() < occupancy:
    #                 board[(x, y)] = 1
    #             else:
    #                 board[(x, y)] = 0
    #     # Return the board
    #     return board


    # # Update the board according to the rules of the game
    # def update_board(self, board):
    #     # For every cell in the board...
    #     for cell in board:
    #         # How many occupied neighbors does this cell have?
    #         neighbors = self.count_neighbors(cell, board)
    #         val = board[cell]
    #         # If the cell is empty and has 3 neighbors, mark it for occupation
    #         if board[cell] == 0 and neighbors == 3:
    #             board[cell] = 2
    #         # On the other hand, if the cell is occupied and doesn't have 2 or 3
    #         # neighbors, mark it for death
    #         elif board[cell] == 1 and not neighbors in [2, 3]:
    #             board[cell] = -1
    #     # Now, go through it again, making all the approved changes
    #     for cell in board:
    #         if board[cell] == 2: board[cell] = 1
    #         if board[cell] == -1: board[cell] = 0


    

    