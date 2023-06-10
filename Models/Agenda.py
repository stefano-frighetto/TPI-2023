class Agenda:
    def __init__(self):
        self.eventos = []
    
    def reservar_evento_agenda(self, evento):
        self.eventos.append(evento)
    
    def cancelar_evento_agenda(self, evento):
        self.eventos.remove(evento)
    
    def verificar_fecha(self, fecha):
        for evento in self.eventos:
            if fecha == evento.fecha:
                return False
        return True