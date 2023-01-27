import sys
from threading import Thread
from Juego import Juego

class testit(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        self.main()

    def main(self):
        print("==========================================================================================")
        c_dim_x = int(input("Ingrese un numero entero para el ancho de las celdas: "))#8
        c_dim_y = int(input("Ingrese un numero entero para el alto de las celdas: "))#8
        v_framerate = int (input("Ingrese un numero entero para el framerate: "))#20
        v_occupancy = float(input("Ingrese un numero de punto flotante para occupancy: "))#0.20
        color_muerta = input("Ingrese 3 numeros enteros separados por espacio para el RGB de las celulas muertas: ")#0,0,0
        a, b, c = color_muerta.split()
        r1, g1, b1 = int(a), int(b), int(c)
        color_viva = input("Ingrese 3 numeros enteros separados por espacio para el RGB de la celulas vivas: ")#200,200,100
        d, e, f = color_viva.split()
        r2, g2, b2 = int(d), int(e), int(f)
        b_dim = int(input("Ingrese un numero entero para el ancho y alto del lattice: "))#80
        # b_dim_y = int(input("Alto del lattice: "))#80
        objeto_simuladorAC = Juego(title="The Game of Life",
                                        version="2.0",
                                        cell_dimensions=(c_dim_x,c_dim_y),
                                        framerate=v_framerate,
                                        occupancy=v_occupancy,
                                        cell_colors={0: (r1, g1, b1), 1: (r2, g2, b2)},
                                        board_dimensions=(b_dim, b_dim))
        objeto_simuladorAC.ejecutar_juego("random")