class Evento:
    def __init__(self, cliente, fecha, servicios_contratados = []):
        self.fecha_evento = fecha
        self.cliente_evento = cliente
        self.servicios_contratados = servicios_contratados
        self.importe_administrativo = 1000 #Considerando al importe administrativo como un importe fijo
        self.importe_iva = 1.21
        self.calcular_importes() #servicios, total, seña
        self.estado_evento = True
    
    def get_estado_evento(self):
        return self.estado_evento
    
    def set_estado_evento(self,nuevo_estado):
        self.estado_evento = nuevo_estado
    
    def get_fecha_evento(self):
        return self.fecha_evento
    
    def set_fecha_evento(self, nueva_fecha):
        self.fecha_evento = nueva_fecha
    
    def get_cliente_evento(self):
        return self.cliente_evento
    
    def set_cliente_evento(self, nuevo_cliente):
        self.cliente_evento = nuevo_cliente
    
    def get_servicios_contratados(self):
        return self.servicios_contratados
    
    def set_servicios_contratados(self, nuevos_servicios):
        self.servicios_contratados = nuevos_servicios
    
    #No es necesario declarar setters para los importes, ya que se calculan en base a valores fijos y a los servicios contratados.
    def get_importe_servicios(self):
        return self.importe_servicios
    
    def get_importe_administrativo(self):
        return self.importe_administrativo
    
    def get_importe_iva(self):
        return self.importe_iva
    
    def get_importe_total(self):
        return self.importe_total
    
    def get_importe_senia(self):
        return self.importe_senia
    
    def __str__(self):
        return f'{self.fecha_evento.day}/{self.fecha_evento.month}/{self.fecha_evento.year} - {self.cliente_evento}'

    def calcular_importes(self):
        self.importe_servicios = sum(servicio.costo_servicio for servicio in self.servicios_contratados)
        self.importe_total = (self.importe_administrativo + self.importe_servicios) * self.importe_iva
        self.importe_senia = 0.3 * self.importe_total

    def contratar_servicio(self, servicio):
        self.servicios_contratados.append(servicio)
        self.calcular_importes()

    def anular_servicio(self, servicio):
        self.servicios_contratados.remove(servicio)
        self.calcular_importes()