import pygame, sys
from pygame.locals import *
from Tablero import Tablero

class Juego:
    def __init__(self, title, version, cell_dimensions, framerate, occupancy, colors, board_dimensions):
        self.title = title
        self.version = version
        self.cell_dimensions = cell_dimensions
        self.framerate = framerate
        self.tablero = Tablero(colors, cell_dimensions, board_dimensions, occupancy)


    def ejecutar_juego(self, pattern):
        # Initialize pygame elements
        screen, bg, clock = self.init_pygame(self.tablero.board_dimensions)
        # Initialize random board
        self.tablero.inicializar_patron(pattern)
        # Enter the game loop
        while True:
            # Slow things down to match the framerate
            clock.tick(self.framerate)
            # Update the board
            self.tablero.update_board()
            # Draw the board on the background
            self.tablero.draw_board(bg)
            # Blit bg to the screen, flip display buffers
            screen.blit(bg, (0, 0))
            pygame.display.flip()
            # Queue user input to catch QUIT signals
            for e in pygame.event.get():
                if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                    # Print farewell message
                    print("\nThanks for watching!")
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                    self.ejecutar_juego(pattern)


    # Initialize pygame elements
    def init_pygame(self, board_dimensions):
        # Initialize the pygame modules
        pygame.init()
        # Determine and set the screen dimensions
        dimensions = (board_dimensions[0] * self.cell_dimensions[0], board_dimensions[1] * self.cell_dimensions[1])
        screen = pygame.display.set_mode(dimensions)
        # Set the title string of the root window
        pygame.display.set_caption(self.title + " " + self.version)
        # Grab the background surface of the screen
        bg = screen.convert()
        # Grab the game clock
        clock = pygame.time.Clock()
        # Return the screen, the background surface, and the game clock
        return screen, bg, clock