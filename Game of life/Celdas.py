class Celda:
    def __init__(self, tam_x, tam_y, pos_x, pos_y, estado_inicial=0):
        self.tam_x = tam_x #tamaño de la celda en x
        self.tam_y = tam_y #tamaño de la celda en y
        self.pos_x = pos_x #tamaño de la celda en x
        self.pos_y = pos_y #tamaño de la celda en y
        self.estado = estado_inicial #estado de la celda

    def esta_viva(self):
        self.estado = 1

    def esta_muerta(self):
        self.estado = 0
