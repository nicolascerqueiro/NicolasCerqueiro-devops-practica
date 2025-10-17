import uuid

class Usuario:
    def __init__(self, nombre: str, correo: str):
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.correo: str = correo

    def is_admin(self) -> bool:
        return False

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.correo}"


class Cliente(Usuario):
    def __init__(self, nombre: str, correo: str, direccion: str):
        super().__init__(nombre, correo)
        self.direccion: str = direccion

    def __str__(self) -> str:
        return f"[{self.id}] Cliente: {self.nombre} - {self.correo} - Dirección: {self.direccion}"


class Administrador(Usuario):
    def __init__(self, nombre: str, correo: str):
        super().__init__(nombre, correo)

    def is_admin(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"[{self.id}] Administrador: {self.nombre} - {self.correo}"