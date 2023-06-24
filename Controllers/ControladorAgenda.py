from Models.Agenda import Agenda
from Models.Cliente import Cliente
from Models.Evento import Evento
from Models.Servicio import Servicio
from Views.VistaAgenda import VistaAgenda
import datetime

class ControladorAgenda:
    def __init__(self, eventos_file, servicios_file):
        self.vista_agenda = VistaAgenda()
        self.servicios = []
        #Llenamos la lista del atributo servicios con el archivo de texto proporcionado
        try:
            with open(servicios_file) as archivo_con_servicios:
                for line in archivo_con_servicios:
                    info_servicio = line.strip().split(',')
                    servicio_individual = Servicio(int(info_servicio[0]),info_servicio[1],int(info_servicio[2]))
                    self.servicios.append(servicio_individual)
        except FileNotFoundError:
            print('No hay servicios cargados')
        #Instanciamos la agenda en un atributo del controlador, con eventos previos o no según el contenido del archivo (registro de eventos)
        try:
            archivo_con_eventos = open(eventos_file)
        except FileNotFoundError:
            self.agenda = Agenda()
        else:
            eventos_agendados = []
            lista_de_eventos = archivo_con_eventos.readlines()
            for renglon in lista_de_eventos:
                renglon_listado = renglon.strip().strip(',').split(',')
                estado_renglon = bool(int(renglon_listado[0]))
                cliente_renglon = Cliente(renglon_listado[1],renglon_listado[2])
                fecha_renglon = datetime.date(int(renglon_listado[5]),int(renglon_listado[4]),int(renglon_listado[3]))
                servicios_renglon = []
                if len(renglon_listado) > 6:                    
                    for i in range(6,len(renglon_listado)):
                        indice_servicio = int(renglon_listado[i])
                        servicios_renglon.append(self.servicios[indice_servicio-1])
                eventos_agendados.append(Evento(estado_renglon, cliente_renglon,fecha_renglon,servicios_renglon))
            self.agenda = Agenda(eventos_agendados)
    
    def actualizar_archivo(self):
        with open('eventos_agendados.txt','w+') as archivo:
            for evento in self.agenda.get_eventos():
                servicios_ids = [servicio.get_id_servicio() for servicio in evento.get_servicios_contratados()]
                servicios_a_escribir = ''
                if len(servicios_ids) > 0:
                    servicios_a_escribir = f'{",".join(map(str, servicios_ids))},'
                archivo.write(f'{int(evento.get_estado_evento())},{evento.get_cliente_evento().get_dni_cliente()},{evento.get_cliente_evento().get_nombre_cliente()},{evento.get_fecha_evento().day},{evento.get_fecha_evento().month},{evento.get_fecha_evento().year},{servicios_a_escribir}\n')
    
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
                    evento_cliente = Evento(True, cliente_evento, fecha_solicitada, servicios_solicitados)
                    self.agenda.reservar_evento_agenda(evento_cliente)
                    self.vista_agenda.mostrar_senia(evento_cliente.get_importe_senia())
                    self.actualizar_archivo()
                case 2:
                    self.vista_agenda.mostrar_eventos_reservados(self.agenda.get_eventos())
                    rta = self.vista_agenda.validar_entero(1,len(self.agenda.get_eventos()))
                    evento_a_cancelar = self.agenda.get_eventos()[rta-1]
                    evento_a_cancelar.set_estado_evento(False)
                    self.vista_agenda.mostrar_cancelacion(evento_a_cancelar)
                    self.actualizar_archivo()
                case 3:
                    break