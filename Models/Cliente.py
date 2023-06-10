#Por los requerimientos del enunciado, puede que la clase Cliente no sea absolutamente necesaria.

class Cliente:
    def __init__(self, nombre_cliente):#, eventos_contratados = []):
        self.nombre_cliente = nombre_cliente
        #self.eventos_contratados = eventos_contratados