class Cliente:
    def __init__(self, dni, nombre_cliente):
        self.dni_cliente = dni
        self.nombre_cliente = nombre_cliente
    
    def get_dni_cliente(self):
        return self.dni_cliente
    
    def set_dni_cliente(self, nuevo_dni):
        self.dni_cliente = nuevo_dni
    
    def get_nombre_cliente(self):
        return self.nombre_cliente
    
    def set_nombre_cliente(self, nuevo_nombre):
        self.nombre_cliente = nuevo_nombre
    
    def __str__(self):
        return self.nombre_cliente