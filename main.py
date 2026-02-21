from cafeteria import Persona, Cliente, Empleado, ProductoBase, Bebida, Pedido, Inventario

def main():
    # Crear inventario
    inventario = Inventario()

    # Crear cliente
    cliente1 = Cliente(1, "Alejandro", "alejandro@email.com")

    # Crear bebida
    bebida1 = Bebida(101, "Latte", 50, "Grande", "CALIENTE")
    bebida1.agregarExtra("Shot extra", 10)

    # Crear pedido
    pedido1 = Pedido(5001, cliente1)
    pedido1.agregarProducto(bebida1)

    # Validar stock
    pedido1.validarStock()

    # Calcular total
    total = pedido1.calcularTotal()
    print("Total del pedido:", total)

    # Cliente realiza pedido
    cliente1.realizarPedido(pedido1)

    # Crear empleado
    empleado1 = Empleado(2, "Carlos", "carlos@email.com", 1001, "BARISTA")
    empleado1.cambiarEstadoPedido(pedido1, "LISTO")
    
if __name__ == "__main__":
    main()