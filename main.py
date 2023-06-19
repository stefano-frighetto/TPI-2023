#ESTO ESTÁ DE MUESTRA NOMÁS, SE HACE AL ÚLTIMO
from Views.VistaAgenda import VistaAgenda
from Controllers.ControladorAgenda import ControladorAgenda
vista = VistaAgenda()
controlador = ControladorAgenda(vista)

controlador.ejecutar()