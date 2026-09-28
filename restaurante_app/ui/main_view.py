import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(self, root, servicio, usuario_actual):

        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.root.title("Restaurante Sabor Andino")
        self.root.geometry("950x600")

        self.crear_interfaz()

    def crear_interfaz(self):

        encabezado = ttk.Frame(self.root, padding=15)
        encabezado.pack(fill="x")

        titulo = ttk.Label(
            encabezado,
            text="RESTAURANTE SABOR ANDINO",
            font=("Arial", 20, "bold")
        )
        titulo.pack(side="left")

        usuario = ttk.Label(
            encabezado,
            text=f"Usuario: {self.usuario_actual['nombre']}"
        )
        usuario.pack(side="right")

        separador = ttk.Separator(
            self.root,
            orient="horizontal"
        )
        separador.pack(fill="x")

        menu = ttk.Frame(self.root, padding=10)
        menu.pack(fill="x")

        ttk.Button(
            menu,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).pack(side="left", padx=5)

        ttk.Button(
            menu,
            text="Productos",
            command=self.mostrar_productos
        ).pack(side="left", padx=5)

        ttk.Button(
            menu,
            text="Ventas",
            command=self.mostrar_ventas
        ).pack(side="left", padx=5)

        self.contenido = ttk.Frame(
            self.root,
            padding=15
        )
        self.contenido.pack(
            fill="both",
            expand=True
        )

        self.mostrar_ventas()

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        columnas = (
            "id",
            "nombre",
            "usuario",
            "rol"
        )

        tabla = ttk.Treeview(
            self.contenido,
            columns=columnas,
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("usuario", text="Usuario")
        tabla.heading("rol", text="Rol")

        tabla.pack(
            fill="both",
            expand=True
        )

        for usuario in self.servicio.obtener_usuarios():

            tabla.insert(
                "",
                "end",
                values=(
                    usuario["id"],
                    usuario["nombre"],
                    usuario["usuario"],
                    usuario["rol"]
                )
            )

    def mostrar_productos(self):

        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Productos registrados",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        columnas = (
            "id",
            "nombre",
            "precio",
            "categoria"
        )

        tabla = ttk.Treeview(
            self.contenido,
            columns=columnas,
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Producto")
        tabla.heading("precio", text="Precio")
        tabla.heading("categoria", text="Categoría")

        tabla.pack(
            fill="both",
            expand=True
        )

        for producto in self.servicio.obtener_productos():

            tabla.insert(
                "",
                "end",
                values=(
                    producto["id"],
                    producto["nombre"],
                    f"${producto['precio']:.2f}",
                    producto["categoria"]
                )
            )

    def mostrar_ventas(self):

        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Gestión de Ventas",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        formulario = ttk.Frame(
            self.contenido
        )
        formulario.pack(fill="x", pady=10)

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.usuarios = self.servicio.obtener_usuarios()

        self.combo_usuario = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.combo_usuario["values"] = [
            f"{u['id']} - {u['nombre']}"
            for u in self.usuarios
        ]

        self.combo_usuario.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Producto:"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.productos = self.servicio.obtener_productos()

        self.combo_producto = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.combo_producto["values"] = [
            f"{p['id']} - {p['nombre']} - ${p['precio']:.2f}"
            for p in self.productos
        ]

        self.combo_producto.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # IMPORTANTE:
        # command= recibe el nombre del método,
        # no se colocan paréntesis.
        boton = ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta
        )

        boton.grid(
            row=2,
            column=1,
            pady=10
        )

        ttk.Label(
            self.contenido,
            text="Ventas registradas",
            font=("Arial", 13, "bold")
        ).pack(pady=10)

        columnas = (
            "id",
            "usuario",
            "producto",
            "precio",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            self.contenido,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading(
            "id",
            text="ID"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "precio",
            text="Precio"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.pack(
            fill="both",
            expand=True
        )

        self.actualizar_tabla_ventas()

    # ESTE ES EL CALLBACK DE LA SEMANA 15
    def registrar_venta(self):

        seleccion_usuario = self.combo_usuario.get()
        seleccion_producto = self.combo_producto.get()

        if not seleccion_usuario:
            messagebox.showwarning(
                "Venta",
                "Seleccione un usuario."
            )
            return

        if not seleccion_producto:
            messagebox.showwarning(
                "Venta",
                "Seleccione un producto."
            )
            return

        usuario_id = int(
            seleccion_usuario.split(" - ")[0]
        )

        producto_id = int(
            seleccion_producto.split(" - ")[0]
        )

        exito, mensaje = self.servicio.registrar_venta(
            usuario_id,
            producto_id
        )

        if exito:

            messagebox.showinfo(
                "Venta registrada",
                mensaje
            )

            self.actualizar_tabla_ventas()

            self.combo_usuario.set("")
            self.combo_producto.set("")

        else:

            messagebox.showerror(
                "Error",
                mensaje
            )

    def actualizar_tabla_ventas(self):

        for fila in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(fila)

        ventas = self.servicio.obtener_ventas()

        for venta in ventas:

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta["id"],
                    venta["usuario_nombre"],
                    venta["producto_nombre"],
                    f"${venta['precio']:.2f}",
                    venta["fecha"]
                )
            )