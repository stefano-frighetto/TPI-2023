class Servicio:
    def __init__(self, idnumero, nombre_servicio, costo_servicio):
        self.id_servicio = idnumero
        self.nombre_servicio = nombre_servicio
        self.costo_servicio = costo_servicio
    
    def __str__(self):
        return f'Servicio: {self.nombre_servicio}\nCosto: ${self.costo_servicio}'
    
    def get_id_servicio(self):
        return self.id_servicio

    def get_nombre_servicio(self):
        return self.nombre_servicio
    
    def set_nombre_servicio(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio

    def get_costo_servicio(self):
        return self.costo_servicio
    
    def set_costo_servicio(self, costo_servicio):
        self.costo_servicio = costo_servicio