import uuid
from typing import Any

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def hay_stock(self, cantidad: int) -> bool:
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad: int) -> None:
        """Disminuye (ventas) o aumenta (reposiciones) el stock"""
        self.stock += cantidad

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.precio:.2f}€ - Stock: {self.stock}"


class ProductoElectronico(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, garantia: int):
        super().__init__(nombre, precio, stock)
        self.garantia: int = garantia

    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} (Electrónico) - {self.precio:.2f}€ - "
                f"Stock: {self.stock} - Garantía: {self.garantia} meses")


class ProductoRopa(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        super().__init__(nombre, precio, stock)
        self.talla: str = talla
        self.color: str = color

    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} (Ropa) - {self.precio:.2f}€ - "
                f"Stock: {self.stock} - Talla: {self.talla}, Color: {self.color}")