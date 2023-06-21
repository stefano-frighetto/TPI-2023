from Models.Agenda import Agenda
from Models.Cliente import Cliente
from Models.Evento import Evento
from Models.Servicio import Servicio
from Views.VistaAgenda import VistaAgenda

class ControladorAgenda:
    def __init__(self):
        self.vista_agenda = VistaAgenda()
        self.agenda = Agenda()
        self.servicios = [
            Servicio(1, "DJ", 500),
            Servicio(2, "Decoración", 800),
            Servicio(3, "Cotillón", 300),
            Servicio(4, 'Máquina de Humo', 200),
            Servicio(5, 'Maquillaje', 250),
            Servicio(6, 'Música en vivo', 1000)]

    
    def ejecutar(self):
        while True:
            self.vista_agenda.mostrar_menu_principal()
            opcion_elegida = self.vista_agenda.validar_entero(1,3)
            match opcion_elegida:
                case 1:
                    nombre_cliente, dni_cliente = self.vista_agenda.solicitar_datos_cliente()
                    cliente_evento = Cliente(dni_cliente, nombre_cliente)
                    fecha_solicitada = self.vista_agenda.solicitar_fecha()
                    if not self.agenda.verificar_fecha(fecha_solicitada):
                        propuesta = self.agenda.proponer_fecha(fecha_solicitada)
                        fecha_sirve = self.vista_agenda.mostrar_proponer_fecha(propuesta)
                        if fecha_sirve:
                            fecha_solicitada = propuesta
                        else:
                            continue
                    servicios_solicitados = self.vista_agenda.solicitar_servicio(self.servicios)
                    evento_cliente = Evento(cliente_evento, fecha_solicitada, servicios_solicitados)
                    self.agenda.reservar_evento_agenda(evento_cliente)
                    self.vista_agenda.mostrar_senia(evento_cliente.get_importe_senia())
                case 2:
                    self.vista_agenda.mostrar_eventos_reservados(self.agenda.get_eventos())
                    rta = self.vista_agenda.validar_entero(1,len(self.agenda.get_eventos()))
                    evento_a_cancelar = self.agenda.get_eventos()[rta-1]
                    evento_a_cancelar.set_estado_evento(False)
                    self.vista_agenda.mostrar_cancelacion(evento_a_cancelar)
                case 3:
                    break

