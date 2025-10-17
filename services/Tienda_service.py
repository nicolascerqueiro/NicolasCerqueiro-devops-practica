from typing import List, Dict, Tuple
from models.Usuario import Usuario, Cliente, Administrador
from models.Producto import Producto
from models.Pedido import Pedido

class TiendaService:
    def __init__(self):
        self.usuarios: Dict[str, Usuario] = {}
        self.productos: Dict[str, Producto] = {}
        self.pedidos: List[Pedido] = []

    # Registro de usuarios
    def registrar_usuario(self, tipo: str, *args, **kwargs) -> Usuario:
        if tipo == "cliente":
            user = Cliente(*args, **kwargs)
        elif tipo == "admin":
            user = Administrador(*args, **kwargs)
        else:
            raise ValueError("Tipo de usuario no válido")
        self.usuarios[user.id] = user
        return user

    # Gestión de productos
    def agregar_producto(self, producto: Producto) -> None:
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> None:
        if producto_id in self.productos:
            del self.productos[producto_id]

    def listar_productos(self) -> List[Producto]:
        return list(self.productos.values())

    # Gestión de pedidos
    def realizar_pedido(self, cliente_id: str, productos_cantidades: List[Tuple[str, int]]) -> Pedido:
        if cliente_id not in self.usuarios or not isinstance(self.usuarios[cliente_id], Cliente):
            raise ValueError("El usuario no existe o no es cliente")
        
        cliente = self.usuarios[cliente_id]
        productos: List[Tuple[Producto, int]] = []
        
        # Verificar stock
        for prod_id, cantidad in productos_cantidades:
            if prod_id not in self.productos:
                raise ValueError(f"Producto {prod_id} no existe")
            producto = self.productos[prod_id]
            if not producto.hay_stock(cantidad):
                raise ValueError(f"No hay stock suficiente de {producto.nombre}")
            productos.append((producto, cantidad))

        # Descontar stock
        for producto, cantidad in productos:
            producto.actualizar_stock(-cantidad)

        pedido = Pedido(cliente, productos)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_usuario(self, usuario_id: str) -> List[Pedido]:
        return [p for p in self.pedidos if p.cliente.id == usuario_id]
