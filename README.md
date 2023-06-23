# ProyectoFinal-TercerSemestre-OldSchool


-Sistema de Órdenes de Compras-

Este es un sistema básico de órdenes de compras desarrollado en Python utilizando la biblioteca Tkinter para la interfaz gráfica y SQLite para la base de datos.

El sistema permite a los usuarios ingresar órdenes de compras, visualizar la lista de órdenes ingresadas, calcular el total de gastos y generar informes o reportes basados en las órdenes de compra almacenadas en la base de datos.

-Requisitos-
Python 3.x
Tkinter (incluido en la mayoría de las instalaciones de Python)
SQLite (incluido en la mayoría de las instalaciones de Python)
Pillow (biblioteca de Python para el manejo de imágenes)

-Instalación y Ejecución-
Clona o descarga este repositorio en tu máquina local.

Abre una terminal y navega hasta el directorio del proyecto.

Crea y activa un entorno virtual (opcional pero se recomienda).

Instala las dependencias requeridas ejecutando el siguiente comando:
pip install -r requirements.txt

Ejecuta el programa utilizando el siguiente comando:
python orden_compra.py

-Características-

Inicio de Sesión: El programa solicita al usuario que ingrese un nombre de usuario y una contraseña para acceder al sistema. Actualmente, se utiliza una combinación fija de usuario y contraseña para la demostración.

Ventana Principal: Después de iniciar sesión correctamente, se abre la ventana principal del sistema. Aquí se pueden ingresar órdenes de compras, visualizar la lista de órdenes ingresadas, calcular el total de gastos, generar informes y salir del programa.

Ingreso de Órdenes de Compra: Se pueden ingresar órdenes de compras especificando el producto, la cantidad y el precio. Al hacer clic en el botón "Agregar Orden", se guarda la orden en la base de datos y se actualiza la lista de órdenes y el total de gastos.

Eliminación de Órdenes de Compra: Se puede seleccionar una orden de compra de la lista y hacer clic en el botón "Eliminar Producto" para eliminarla de la base de datos y de la lista visualmente. El total de gastos se actualiza automáticamente.

Generación de Informes: Se puede generar un informe o reporte basado en las órdenes de compra almacenadas en la base de datos. Actualmente, el informe muestra una tabla con los detalles de todas las órdenes ingresadas.

Salir del Programa: Se puede hacer clic en el botón "Salir" para cerrar el programa.

-Personalización-

Colores y Fuentes: Los colores de fondo, los colores de texto y las fuentes utilizadas en la interfaz gráfica se pueden personalizar modificando los parámetros correspondientes en el código.

Tamaño del Icono: El tamaño del icono se puede ajustar creando un nuevo archivo de icono con las dimensiones deseadas utilizando una herramienta de edición de imágenes y reemplazando el archivo "icono.ico" en el directorio del proyecto.

-Contribución-

Si deseas contribuir a este proyecto, siéntete libre de enviar pull requests o abrir issues con tus sugerencias o mejoras.

Esperamos que esta guía README te ayude a entender y utilizar el sistema de órdenes de compras. Si tienes alguna pregunta adicional, no dudes en contactarnos.

¡Gracias por utilizar el sistema de órdenes de compras de Old School!

![Logo OldSchool](oldschool.png)
