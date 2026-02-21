class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

    def login(self):
        print(self.nombre, "inició sesión")

    def actualizarPerfil(self, nuevoEmail):
        self.email = nuevoEmail
        print("Email actualizado a:", self.email)

class Cliente(Persona):
    def __init__(self, idPersona, nombre, email):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad = 0
        self.historialPedidos = []

    def realizarPedido(self, pedido):
        self.historialPedidos.append(pedido)
        self.puntosFidelidad += 10
        print("Pedido realizado. Puntos actuales:", self.puntosFidelidad)

    def consultarHistorial(self):
        print("Historial de pedidos:")
        for pedido in self.historialPedidos:
            print("Pedido ID:", pedido.idPedido)

    def canjearPuntos(self, puntos):
        if self.puntosFidelidad >= puntos:
            self.puntosFidelidad -= puntos
            print("Puntos canjeados.")
        else:
            print("No tienes suficientes puntos.")

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, idEmpleado, rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol  # "BARISTA", "MESERO", "GERENTE"

    def actualizarInventario(self, inventario, ingrediente, cantidad):
        inventario.reducirStock(ingrediente, cantidad)

    def cambiarEstadoPedido(self, pedido, nuevoEstado):
        pedido.estado = nuevoEstado
        print("Estado del pedido cambiado a:", nuevoEstado)

class ProductoBase:
    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño = tamaño
        self.temperatura = temperatura  # "FRIA" o "CALIENTE"
        self.modificadores = []

    def agregarExtra(self, extra, precioExtra):
        self.modificadores.append((extra, precioExtra))

    def calcularPrecioFinal(self):
        total = self.precioBase
        for extra in self.modificadores:
            total += extra[1]
        return total
    

class Pedido:
    def __init__(self, idPedido, cliente):
        self.idPedido = idPedido
        self.cliente = cliente
        self.productos = []
        self.estado = "PENDIENTE"
        self.total = 0

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularTotal(self):
        self.total = 0
        for producto in self.productos:
            self.total += producto.calcularPrecioFinal()
        return self.total

    def validarStock(self):
        print("Stock validado correctamente (simulado).")

class Inventario:
    def __init__(self):
        self.ingredientes = {
            "cafe": 10,
            "leche": 10,
            "azucar": 20
        }

    def reducirStock(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes:
            if self.ingredientes[ingrediente] >= cantidad:
                self.ingredientes[ingrediente] -= cantidad
                print("Stock actualizado.")
            else:
                self.notificarFaltante(ingrediente)
        else:
            print("Ingrediente no existe.")

    def notificarFaltante(self, ingrediente):
        print("Falta el ingrediente:", ingrediente)