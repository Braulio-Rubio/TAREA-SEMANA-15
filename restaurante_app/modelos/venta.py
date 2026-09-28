class Venta:
    def __init__(self, id, usuario_id, usuario_nombre, producto_id,
                 producto_nombre, precio, fecha):
        self.id = id
        self.usuario_id = usuario_id
        self.usuario_nombre = usuario_nombre
        self.producto_id = producto_id
        self.producto_nombre = producto_nombre
        self.precio = precio
        self.fecha = fecha

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "usuario_nombre": self.usuario_nombre,
            "producto_id": self.producto_id,
            "producto_nombre": self.producto_nombre,
            "precio": self.precio,
            "fecha": self.fecha
        }