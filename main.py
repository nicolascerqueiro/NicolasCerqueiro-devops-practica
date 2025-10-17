from models.Producto import ProductoElectronico, ProductoRopa, Producto
from services.Tienda_service import TiendaService

def main():
    tienda = TiendaService()

    # Crear usuarios
    c1 = tienda.registrar_usuario("cliente", "Ana", "ana@example.com", "Calle Sol 123")
    c2 = tienda.registrar_usuario("cliente", "Luis", "luis@example.com", "Av. Luna 45")
    c3 = tienda.registrar_usuario("cliente", "Marta", "marta@example.com", "Plaza Mar 78")
    admin = tienda.registrar_usuario("admin", "Admin1", "admin@example.com")

    # Crear productos
    p1 = ProductoElectronico("Portátil", 1200.0, 5, garantia=24)
    p2 = ProductoElectronico("Smartphone", 800.0, 10, garantia=12)
    p3 = ProductoRopa("Camiseta", 20.0, 50, talla="M", color="Rojo")
    p4 = ProductoRopa("Pantalón", 35.0, 30, talla="L", color="Azul")
    p5 = Producto("Silla de oficina", 150.0, 15)

    # Añadir al inventario
    for p in [p1, p2, p3, p4, p5]:
        tienda.agregar_producto(p)

    # Listar productos
    print("Inventario inicial:")
    for prod in tienda.listar_productos():
        print(prod)

    # Realizar pedidos
    pedido1 = tienda.realizar_pedido(c1.id, [(p1.id, 1), (p3.id, 2)])
    pedido2 = tienda.realizar_pedido(c2.id, [(p2.id, 1), (p4.id, 1)])
    pedido3 = tienda.realizar_pedido(c3.id, [(p3.id, 5), (p5.id, 1)])

    print("\nPedidos realizados:")
    print(pedido1)
    print(pedido2)
    print(pedido3)

    # Histórico de pedidos de un cliente
    print("\nHistórico de pedidos de Ana:")
    for p in tienda.listar_pedidos_usuario(c1.id):
        print(p)

    # Inventario actualizado
    print("\nInventario tras pedidos:")
    for prod in tienda.listar_productos():
        print(prod)


if __name__ == "__main__":
    main()