import datetime

class VistaAgenda:
    def mostrar_menu_principal(self):
        print('"""""""""""""""""""""""""""""""""""""""""""""""""""""')
        print("Bienvenido al sistema de reservas de SocialEvent S.A.")
        print('"""""""""""""""""""""""""""""""""""""""""""""""""""""')
        print("1. Realizar una nueva reserva")      
        print("2. Cancelar una reserva")
        print("3. Salir")
    
    def validar_entero(self, lim_inf, lim_sup):
        while True:
            try:
                choice = int(input(f'Ingrese una opción entre {lim_inf} y {lim_sup}\n'))
            except ValueError:
                print('Opción inválida. Intente nuevamente:')
                continue
            else:
                if choice < lim_inf or choice > lim_sup:
                    print('Opción inválida. Intente de nuevo:')
                    continue
                else:
                    return choice
    
    def solicitar_datos_cliente(self):
        print('Ingrese el nombre del cliente:')
        nombre = input()
        print('Ingrese el DNI del cliente')
        dni = input()
        return nombre, dni
    
    def solicitar_fecha(self):
        print('¿Qué fecha desea reservar para su evento')
        while True:
            print('Ingrese el día')
            day = self.validar_entero(1,31)
            print('Ingrese el mes')
            month = self.validar_entero(1,12)
            print('Ingrese el año')
            year = self.validar_entero(2023,2026)
            fecha_ingresada = datetime.date(year, month, day)
            if fecha_ingresada < datetime.date.today():
                print('¡Esa fecha ya pasó!')
                continue
            else:
                return fecha_ingresada
    
    def mostrar_proponer_fecha(self, date):
        print('La fecha solicitada no está disponible')
        print('Se ofrece la siguiente fecha a modo de reemplazo:')
        print(f'{date.day}/{date.month}/{date.year}')
        print('¿Desea reservar ésta fecha?')
        print('1- Sí')
        print('2- No (Mostrar otra opción)')
        print('3- No (Cancelar solicitud de evento)')
        rta = self.validar_entero(1,3)
        #No estoy para nada seguro de si funciona manejar estos return
        if rta == 1:
            return True
        elif rta == 2:
            self.mostrar_proponer_fecha(date + datetime.timedelta(days=1))
        else:
            return False
    
    def solicitar_servicio(self, lista_de_servicios):
        servicios_escogidos = []
        rta = 0
        while True:
            print('Seleccione un servicio de la lista:')
            for i, servicio in enumerate(lista_de_servicios):
                # print(f'{servicio.id_servicio}- {servicio}')
                print(f'{i+1}- {servicio}')
            print(f'{len(lista_de_servicios) + 1}- No quiero más servicios')
            rta = self.validar_entero(1,len(lista_de_servicios)+1)
            if rta == len(lista_de_servicios) + 1:
                return servicios_escogidos
            else:
                servicios_escogidos.append(lista_de_servicios[rta-1])
    
    def mostrar_senia(self, costo_senia):
        print(f'El monto de la seña para reservar este evento es de ${costo_senia}')
    
    def mostrar_eventos_reservados(self, lista_de_eventos):
        for i, evento in enumerate(lista_de_eventos):
            if evento.estado_evento:
                print(f'{i+1}- {evento}')
    
    def mostrar_cancelacion(self, evento):
        fecha_actual = datetime.date.today()
        diferencia = evento.fecha_evento - fecha_actual
        diferencia_dias = diferencia.days
        if  diferencia_dias > 15:
            print(f'Su cancelación fue realizada con anticipación, por lo que se le reintegrarán ${evento.importe_senia * 0.3}')
        else:
            print('Su cancelación ha sido realizada con una anticipación menor a 15 días, por lo que no corresponde reintegro.')
    
    def mostrar_sin_eventos(self):
        print('No hay ningún evento reservado')
    
    def mostrar_detalle_evento(self, evento):
        print('Detalle de la reserva:')
        print(f'Estado de la reserva: {evento.estado_evento}')
        print(f'Cliente: {evento.cliente_evento}')
        print(f'Fecha del evento: {evento.fecha_evento}')
        print(f'Servicios Contratados:')
        for servicio in evento.servicios_contratados:
            print(servicio)
        print(f'Importe total: ${evento.importe_total}')
        print(f'Importe seña: ${evento.importe_senia}')