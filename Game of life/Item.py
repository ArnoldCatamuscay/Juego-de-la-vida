class Item:
    def __init__(self, estado_inicial):
        self.estado = estado_inicial #estado de la celda

    def vive(self):
        self.estado = 1

    def muere(self):
        self.estado = 0