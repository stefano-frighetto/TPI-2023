# Por los requerimientos del enunciado, no parece ser necesario que el servicio contenga una lista de eventos asociados, por lo que fueron comentados.

class Servicio:
    def __init__(self, nombre_servicio, costo_servicio):#, eventos_asociados = []):
        self.nombre_servicio = nombre_servicio
        self.costo_servicio = costo_servicio
        # self.eventos_asociados = eventos_asociados
    
    def __str__(self):
        return f'Servicio: {self.nombre_servicio}\nCosto: ${self.costo_servicio}'
    
    # def agregar_evento_asociado(self, evento):
        # self.eventos_asociados.append(evento)
    
    def get_nombre_servicio(self):
        return self.nombre_servicio
    
    def get_costo_servicio(self):
        return self.costo_servicio
    
    # def get_eventos_asociados(self):
        # return self.eventos_asociados
    
    def set_nombre_servicio(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio
    
    def set_costo_servicio(self, costo_servicio):
        self.costo_servicio = costo_servicio
    
    # def set_eventos_asociados(self, eventos_asociados):
        # self.eventos_asociados = eventos_asociados