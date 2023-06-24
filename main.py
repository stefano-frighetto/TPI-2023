from Controllers.ControladorAgenda import ControladorAgenda

archivo_agenda = 'eventos_agendados.txt'
archivo_servicios = 'servicios_disponibles.txt'
controlador_main = ControladorAgenda(archivo_agenda, archivo_servicios)

controlador_main.ejecutar()