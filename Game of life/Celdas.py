class Celda:
    def __init__(self, x, y, color, estado_inicial=0):
        self.dim_x = x #tamaño de la celula en x
        self.dim_y = y #tamaño de la celula en y
        self.color = color #color de la celula
        self.estado = estado_inicial #estado de la celula

    def viva(self):
        self.estado = 1

    def muerta(self):
        self.estado = 0

    def cambiar_estado(self):
        if self.estado == 0:
            self.viva()
        else:
            self.muerta()
