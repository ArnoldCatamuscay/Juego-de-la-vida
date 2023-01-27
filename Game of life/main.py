import sys
from threading import Thread
from Juego import Juego

class testit(Thread):
    def __init__(self, args):
        Thread.__init__(self)
        self.args = args

    def run(self):
        self.main(self.args)

    def main(self, args):
        if len(args) != 3: sys.exit("USAGE: life.py X_CELLS Y_CELLS")
        print("=============================================")
        print("Tamaño de las celdas: ")
        print("Framerate: ")
        print("Occupancy: ")
        print("Color celda viva: ")
        print("Color celda muerta: ")
        print("Dimensiones del lattice: ")
        objeto_simuladorAC = Juego(title="The Game of Life",
                                        version="2.0",
                                        cell_dimensions=(8,8),
                                        framerate=20,
                                        occupancy=0.20,
                                        cell_colors={0: (0, 0, 0), 1: (200, 200, 100)},
                                        board_dimensions=(int(args[1]), int(args[2])))
        objeto_simuladorAC.ejecutar_juego("random")


# The following code is executed upon command-line invocation
if __name__ == "__main__":
    program = testit(sys.argv)
    print("")
    print(sys.argv)# "life.py 80 80"
    program.start()