import datetime

class Agenda:
    def __init__(self):
        self.eventos = []
    
    def get_eventos(self):
        return self.eventos
    
    def set_eventos(self, nuevos_eventos):
        self.eventos = nuevos_eventos
    
    def verificar_fecha(self, fecha):
        for evento in self.eventos:
            if fecha == evento.fecha:
                return False
        return True
    
    def proponer_fecha(self, fecha_inicial):
        while not self.verificar_fecha(fecha_inicial):
            fecha_propuesta = fecha_inicial + datetime.timedelta(days = 1)
        return fecha_propuesta

    def reservar_evento_agenda(self, evento):
        self.eventos.append(evento)
    
    def cancelar_evento_agenda(self, evento):
        for reserva in self.eventos:
            if reserva == evento:
                reserva.estado_evento = False
                break