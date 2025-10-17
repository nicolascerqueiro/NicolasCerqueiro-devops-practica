import uuid
from datetime import datetime
from typing import List, Tuple
from .Usuario import Cliente
from .Producto import Producto

class Pedido:
    def __init__(self, cliente: Cliente, productos: List[Tuple[Producto, int]]):
        self.id: str = str(uuid.uuid4())
        self.fecha: datetime = datetime.now()
        self.cliente: Cliente = cliente
        self.productos: List[Tuple[Producto, int]] = productos

    def calcular_total(self) -> float:
        return sum(prod.precio * cantidad for prod, cantidad in self.productos)

    def __str__(self) -> str:
        productos_str = "\n".join(
            [f"- {prod.nombre} x{cantidad} = {prod.precio * cantidad:.2f}€"
             for prod, cantidad in self.productos]
        )
        return (f"Pedido [{self.id}] - Cliente: {self.cliente.nombre} - Fecha: {self.fecha}\n"
                f"{productos_str}\nTotal: {self.calcular_total():.2f}€")