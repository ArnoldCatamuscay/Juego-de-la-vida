from Celdas import Celda
import numpy as np

class Tablero:
    def __init__(self, cell_colors, cell_dimensions, board_dimensions):
        self.cell_colors = cell_colors
        self.board_dimensions = board_dimensions
        self.cell_dimensions = cell_dimensions
        self.board = dict()

    def inicializar_patron(self, pattern):
        # Inicializar el tablero con un patrón específico
        pass

    def get_board(self):
        return self.board