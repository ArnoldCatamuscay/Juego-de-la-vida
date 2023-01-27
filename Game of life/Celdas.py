class Celda:
    def __init__(self, tam_x, tam_y, pos_x, pos_y, color, estado_inicial=0):
        self.tam_x = tam_x #tamaño de la celula en x
        self.tam_y = tam_y #tamaño de la celula en y
        self.pos_x = pos_x #tamaño de la celula en x
        self.pos_y = pos_y #tamaño de la celula en y
        # self.color = color #color de la celula
        self.estado = estado_inicial #estado de la celula

    def esta_viva(self):
        self.estado = 1

    def esta_muerta(self):
        self.estado = 0

    # def cambiar_estado(self):
    #     if self.estado == 0:
    #         self.esta_viva()
    #     else:
    #         self.esta_muerta()
