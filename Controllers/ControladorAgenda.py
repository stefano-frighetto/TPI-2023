from Models.Agenda import Agenda
from Models.Cliente import Cliente
from Models.Evento import Evento
from Models.Servicio import Servicio
from Views.VistaAgenda import VistaAgenda
import datetime

class ControladorAgenda:
    def __init__(self, vista):
        self.vista_agenda = vista
        self.agenda = Agenda()
        self.servicios = [
            Servicio(1, "DJ", 500),
            Servicio(2, "Decoración", 800),
            Servicio(3, "Cotillón", 300),]

    
    def ejecutar(self):
        self.vista_agenda.mostrar_menu()
        opcion_elegida = self.vista_agenda.validar_entero(1,5)
        match opcion_elegida:
            case 1:
                nombre_cliente, dni_cliente = self.vista_agenda.solicitar_datos_cliente()
                cliente_evento = Cliente(dni_cliente, nombre_cliente)
                fecha_solicitada = self.vista_agenda.solicitar_fecha()
                if not self.agenda.verificar_fecha(fecha_solicitada):
                    self.agenda.proponer_fecha()
                servicios_solicitados = self.vista_agenda.solicitar_servicio()
                evento_cliente = Evento(cliente_evento, fecha_solicitada, servicios_solicitados)
                costo_senia = evento_cliente.importe_minimo_senia
                if self.vista_agenda.solicitar_senia(costo_senia):
                    evento_cliente.set_estado_evento(True)   
            case 2:
                pass
            case 3:
                pass




        # if opcion_elegida == 1:
        #     pass
        # elif opcion_elegida == 2:
        #     pass





        # while True:
        #     self.mostrar_menu_principal()
        #     opcion = input("Ingrese una opción: ")
            
