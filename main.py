from Views.VistaAgenda import VistaAgenda
from Controllers.ControladorAgenda import ControladorAgenda
vista_main = VistaAgenda()
controlador_main = ControladorAgenda(vista_main)

controlador_main.ejecutar()