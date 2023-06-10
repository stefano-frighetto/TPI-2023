class Evento:
    def __init__(self, cliente, fecha, servicios_contratados = []):
        self.cliente = cliente
        self.fecha = fecha
        self.servicios_contratados = servicios_contratados
        self.importe_administrativo = 0
        self.importe_servicios = 0
        self.importe_total = (self.importe_administrativo + self.importe_servicios) * 1.21
    
    def contratar_servicios(self, *servicios):
        #Una manera más corta de lograrlo (*servicios se toma como tupla)
        #El método extend agrega cada elemento, en vez de agregar la tupla
        #self.servicios_contratados.extend(servicios)
        for servicio in servicios:
            self.servicios_contratados.append(servicio)