Restaurante Sabor Andino
Semana 15 – Manejo de eventos
Descripción

Este proyecto corresponde a la evolución de la aplicación restaurante_app desarrollada durante las semanas anteriores de la asignatura de Programación Orientada a Objetos.

En esta Semana 15 se incorporó una sección de ventas para demostrar los conceptos fundamentales del manejo de eventos mediante una interfaz gráfica desarrollada con Tkinter.

Objetivo

Implementar un flujo básico de manejo de eventos en el que una acción realizada por el usuario active un botón mediante command=, ejecute un callback, delegue la operación al servicio correspondiente y almacene la información en un archivo JSON.

Funcionalidades
Inicio de sesión de usuarios.
Consulta de usuarios.
Consulta de productos.
Registro de ventas.
Selección de un usuario.
Selección de un producto.
Persistencia de las ventas en ventas.json.
Visualización de las ventas mediante Treeview.
Actualización de la información después de registrar una venta.
Manejo de eventos

El registro de una venta utiliza el siguiente flujo:

Usuario
↓
Botón Registrar venta
↓
command=
↓
Callback registrar_venta()
↓
RestauranteServicio
↓
Persistencia en ventas.json
↓
Actualización de la interfaz

El botón de registro utiliza:

command=self.registrar_venta

El callback obtiene los datos seleccionados en la interfaz y delega la operación al RestauranteServicio.

Arquitectura

El proyecto mantiene una arquitectura modular:

restaurante_app/
├── datos/
├── modelos/
├── servicios/
├── ui/
├── assets/
├── main.py
└── README.md
Persistencia

La información se almacena mediante archivos JSON:

usuarios.json
productos.json
ventas.json

La interfaz no manipula directamente los archivos JSON. La lectura y escritura se realiza mediante los servicios correspondientes.

Modelo de venta

Una venta relaciona:

Usuario.
Producto.
Precio.
Fecha.
Ejecución

Para ejecutar el proyecto se requiere tener Python instalado.

Desde la terminal de Visual Studio Code se ejecuta:

python main.py

También puede utilizarse:

py main.py
Datos de prueba

Para realizar las pruebas se utilizaron datos simulados de usuarios y productos correspondientes a la continuidad del proyecto de semanas anteriores.

Usuario de prueba:

Usuario: braulio
Contraseña: 1234
Conclusión

La Semana 15 permitió incorporar el manejo básico de eventos a restaurante_app, demostrando cómo una acción del usuario puede iniciar una operación mediante command=, un callback y la delegación hacia la capa de servicios. La información generada se almacena en ventas.json y posteriormente se presenta en la interfaz.