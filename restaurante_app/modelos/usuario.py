class Usuario:
    def __init__(self, id, nombre, usuario, password, rol):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.password = password
        self.rol = rol

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password,
            "rol": self.rol
        }