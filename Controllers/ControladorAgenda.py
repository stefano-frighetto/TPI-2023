from Models.Agenda import Agenda
from Models.Cliente import Cliente
from Models.Evento import Evento
from Models.Servicio import Servicio
from Views.VistaAgenda import VistaAgenda
import datetime

class ControladorAgenda:
    def __init__(self, vista_agenda):
        self.vista_agenda = vista_agenda
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
            opcion_elegida = self.vista_agenda.validar_entero(1,5)
            match opcion_elegida:
                case 1:
                    nombre_cliente, dni_cliente = self.vista_agenda.solicitar_datos_cliente()
                    cliente_evento = Cliente(dni_cliente, nombre_cliente)
                    fecha_solicitada = self.vista_agenda.solicitar_fecha()
                    if not self.agenda.verificar_fecha(fecha_solicitada):
                        propuesta = self.agenda.proponer_fecha(fecha_solicitada)
                        fecha_sirve = self.vista_agenda.mostrar_fecha_propuesta(propuesta)
                        if fecha_sirve:
                            fecha_solicitada = propuesta
                        else:
                            pass#CONTINUE
                    
                    servicios_solicitados = self.vista_agenda.solicitar_servicio(self.servicios)
                    evento_cliente = Evento(cliente_evento, fecha_solicitada, servicios_solicitados)
                    costo_senia = evento_cliente.importe_minimo_senia
                    if self.vista_agenda.solicitar_senia(costo_senia):
                        evento_cliente.set_estado_evento(True)
                    self.agenda.reservar_evento_agenda(evento_cliente)
                case 2:
                    self.vista_agenda.mostrar_eventos_no_seniados(self.agenda.get_eventos())
                case 3:
                    pass




        # if opcion_elegida == 1:
        #     pass
        # elif opcion_elegida == 2:
        #     pass

        # while True:
        #     self.mostrar_menu_principal()
        #     opcion = input("Ingrese una opción: ")
            
