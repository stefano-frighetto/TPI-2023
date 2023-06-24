#Utilizamos módulo datetime para manipular las fechas como objetos de tipo Fecha
import datetime

class Agenda:
    def __init__(self, eventos = []):
        #La agenda tiene como atributo una lista de objetos Evento
        self.eventos = eventos
    
    def get_eventos(self):
        return self.eventos
    
    def set_eventos(self, nuevos_eventos):
        self.eventos = nuevos_eventos
    
    def verificar_fecha(self, fecha):
        #Se verifica si la fecha ya existe comparándola con todos los eventos confirmados
        for evento in self.eventos:
            if fecha == evento.fecha_evento and evento.estado_evento:
                return False
        return True
    
    def proponer_fecha(self, fecha_inicial):
        #Se propone el día siguiente que no esté en los eventos confirmados, usando el método declarado anteriormente
        fecha_propuesta = fecha_inicial
        while not self.verificar_fecha(fecha_propuesta):
            fecha_propuesta += datetime.timedelta(days = 1)
        return fecha_propuesta

    def reservar_evento_agenda(self, evento):
        self.eventos.append(evento)
    
    def cancelar_evento_agenda(self, evento):
        for reserva in self.eventos:
            if reserva == evento:
                reserva.estado_evento = False
                break