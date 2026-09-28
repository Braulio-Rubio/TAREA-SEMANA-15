import os
from datetime import datetime

from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.ruta_usuarios = os.path.join(
            base, "datos", "usuarios.json"
        )

        self.ruta_productos = os.path.join(
            base, "datos", "productos.json"
        )

        self.ruta_ventas = os.path.join(
            base, "datos", "ventas.json"
        )

    def obtener_usuarios(self):
        return ArchivoServicio.leer_json(self.ruta_usuarios)

    def obtener_productos(self):
        return ArchivoServicio.leer_json(self.ruta_productos)

    def obtener_ventas(self):
        return ArchivoServicio.leer_json(self.ruta_ventas)

    def validar_login(self, usuario, password):
        usuarios = self.obtener_usuarios()

        for item in usuarios:
            if (
                item["usuario"] == usuario
                and item["password"] == password
            ):
                return item

        return None

    def registrar_venta(self, usuario_id, producto_id):

        usuarios = self.obtener_usuarios()
        productos = self.obtener_productos()
        ventas = self.obtener_ventas()

        usuario = next(
            (u for u in usuarios if u["id"] == usuario_id),
            None
        )

        producto = next(
            (p for p in productos if p["id"] == producto_id),
            None
        )

        if usuario is None:
            return False, "El usuario seleccionado no existe."

        if producto is None:
            return False, "El producto seleccionado no existe."

        nuevo_id = 1

        if ventas:
            nuevo_id = max(v["id"] for v in ventas) + 1

        nueva_venta = {
            "id": nuevo_id,
            "usuario_id": usuario["id"],
            "usuario_nombre": usuario["nombre"],
            "producto_id": producto["id"],
            "producto_nombre": producto["nombre"],
            "precio": producto["precio"],
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        ventas.append(nueva_venta)

        ArchivoServicio.guardar_json(
            self.ruta_ventas,
            ventas
        )

        return True, "Venta registrada correctamente."