class Evento:
    def __init__(self, cliente, fecha, servicios_contratados = []):
        self.fecha_evento = fecha
        self.cliente_evento = cliente
        self.servicios_contratados = servicios_contratados
        self.importe_administrativo = 100 #Considerando al importe administrativo como un importe fijo. Sino (se me ocurre), podría ser calculado según los servicios y/o según la proximidad de la fecha
        self.importe_iva = 1.21
        self.importe_recibido_senia = 0
        self.calcular_importes() #servicios, total, mínimo seña, restante
        self.estado_evento = False #El evento se inicia inactivo, ya que es necesario abonar la seña antes de realizar la reserva, y la seña es calculada desde el evento (debe ser instanciado)
    
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
    
    #No es necesario declarar setters para los importes, ya que se calculan en base a valores fijos y a los servicios contratados. Tampoco tengo muy en claro si estos getters van a ser necesarios
    def get_importe_servicios(self):
        return self.importe_servicios
    
    def get_importe_administrativo(self):
        return self.importe_administrativo
    
    def get_importe_iva(self):
        return self.importe_iva
    
    def get_importe_total(self):
        return self.importe_total
    
    def get_importe_minimo_senia(self):
        return self.importe_minimo_senia
    
    def get_importe_recibido_senia(self):
        return self.get_importe_recibido_senia
    
    #Para la seña recibida sí hay setter, porque se inicializa en cero
    def set_importe_recibido_senia(self, nuevo_importe):
        self.importe_recibido_senia = nuevo_importe
    
    def __str__(self):
        return f'{self.fecha_evento} - {self.cliente_evento}'

    def calcular_importes(self):
        self.importe_servicios = sum(servicio.costo_servicio for servicio in self.servicios_contratados)
        self.importe_total = (self.importe_administrativo + self.importe_servicios) * self.importe_iva
        self.importe_minimo_senia = 0.3 * self.importe_total
        self.importe_restante = self.importe_total - self.importe_recibido_senia

    def contratar_servicio(self, servicio):
        self.servicios_contratados.append(servicio)
        self.calcular_importes()

    def anular_servicio(self, servicio):
        self.servicios_contratados.remove(servicio)
        self.calcular_importes()