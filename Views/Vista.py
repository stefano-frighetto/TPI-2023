import datetime
from Models import Agenda,Cliente,Evento,Servicio

class Vista:
    def _init_(self):
        self.agenda = Agenda()  # Instanciamos la Agenda
    
    def mostrar_menu_principal(self):
        print("Bienvenido al sistema de reservas de SocialEvent S.A.")
        print("1. Realizar una nueva reserva")
        print("2. Cancelar una reserva")
        print("3. Salir")
    
    def realizar_reserva(self):
        dni_cliente = input("Ingrese el DNI del cliente: ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cliente = Cliente(dni_cliente, nombre_cliente)
        
        fecha_solicitada = input("Ingrese la fecha solicitada del evento (DD/MM/AAAA): ")
        fecha_solicitada = datetime.datetime.strptime(fecha_solicitada, "%d/%m/%Y").date()
        
        if not self.agenda.verificar_fecha(fecha_solicitada):
            fecha_sugerida = self.agenda.proponer_fecha(fecha_solicitada)
            print(f"La fecha solicitada no está disponible. Se propone la fecha {fecha_sugerida.strftime('%d/%m/%Y')}")
            opcion = input("¿Desea reservar en la fecha sugerida? (S/N): ")
            if opcion.lower() == "s":
                fecha_solicitada = fecha_sugerida
        
        evento = Evento(cliente, fecha_solicitada)
        
        print("Servicios disponibles:")
        # Mostrar servicios disponibles y sus costos
        servicios_disponibles = [
            Servicio(1, "DJ", 500),
            Servicio(2, "Decoración", 800),
            Servicio(3, "Cotillón", 300),
            # Agregar más servicios disponibles según sea necesario
        ]
        for servicio in servicios_disponibles:
            print(servicio)
        
        opcion_servicios = input("Ingrese los números de los servicios deseados separados por comas: ")
        numeros_servicios = opcion_servicios.split(",")
        for numero_servicio in numeros_servicios:
            servicio_elegido = servicios_disponibles[int(numero_servicio) - 1]
            evento.contratar_servicio(servicio_elegido)
        
        self.agenda.reservar_evento_agenda(evento)
        print("¡Reserva realizada con éxito!")
    
    def cancelar_reserva(self):
        # Mostrar lista de eventos reservados
        eventos = self.agenda.get_eventos()
        if len(eventos) == 0:
            print("No hay eventos reservados.")
            return
        
        print("Eventos reservados:")
        for i, evento in enumerate(eventos):
            print(f"{i+1}. Fecha: {evento.get_fecha_evento().strftime('%d/%m/%Y')}, Cliente: {evento.get_cliente_evento().get_nombre_cliente()}")
        
        opcion_cancelar = input("Ingrese el número del evento que desea cancelar: ")
        numero_evento = int(opcion_cancelar) - 1
        
        evento_cancelar = eventos[numero_evento]
        self.agenda.cancelar_evento_agenda(evento_cancelar)
        print("¡Reserva cancelada con éxito!")
    
    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Ingrese una opción: ")
            
            if opcion == "1":
                self.realizar_reserva()
            elif opcion == "2":
                self.cancelar_reserva()
            elif opcion == "3":
                pass