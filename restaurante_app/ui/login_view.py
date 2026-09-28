import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:

    def __init__(self, root, servicio, mostrar_principal):
        self.root = root
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        self.root.title("Restaurante Sabor Andino")
        self.root.geometry("450x350")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        contenedor = ttk.Frame(self.root, padding=30)
        contenedor.pack(expand=True)

        titulo = ttk.Label(
            contenedor,
            text="RESTAURANTE SABOR ANDINO",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        ttk.Label(
            contenedor,
            text="Usuario:"
        ).pack(anchor="w")

        self.entrada_usuario = ttk.Entry(
            contenedor,
            width=35
        )
        self.entrada_usuario.pack(pady=5)

        ttk.Label(
            contenedor,
            text="Contraseña:"
        ).pack(anchor="w")

        self.entrada_password = ttk.Entry(
            contenedor,
            width=35,
            show="*"
        )
        self.entrada_password.pack(pady=5)

        boton = ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        )
        boton.pack(pady=20)

    def iniciar_sesion(self):

        usuario = self.entrada_usuario.get().strip()
        password = self.entrada_password.get().strip()

        if not usuario or not password:
            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )
            return

        resultado = self.servicio.validar_login(
            usuario,
            password
        )

        if resultado:
            self.mostrar_principal(resultado)
        else:
            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )