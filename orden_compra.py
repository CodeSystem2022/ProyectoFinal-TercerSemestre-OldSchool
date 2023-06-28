import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
from reportlab.pdfgen import canvas

def verificar_credenciales():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    if usuario == "admin" and contrasena == "admin123":
        ventana_login.destroy()
        abrir_ventana_principal()
    else:
        messagebox.showerror("Error", "Contraseña/usuario incorrecto")

        

def abrir_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema de Órdenes de Compras")
    ventana_principal.configure(bg="DarkOliveGreen")

    ventana_principal.iconbitmap("Orden-de.ico") # Icono


    ventana_principal.iconbitmap("Orden-de.ico")# Icono


    conexion = sqlite3.connect("ordenes_compra.db")
    cursor = conexion.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS ordenes_compra (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT,
            cantidad INTEGER,
            precio REAL
        )
    """)



    def agregar_orden():
        producto = producto_entry.get()
        cantidad = cantidad_entry.get()
        precio = precio_entry.get()

        if producto and cantidad and precio:
            cantidad = int(cantidad)
            precio = float(precio)

            cursor.execute("INSERT INTO ordenes_compra (producto, cantidad, precio) VALUES (?, ?, ?)", (producto, cantidad, precio))
            conexion.commit()

            actualizar_lista()
            calcular_total()

            producto_entry.delete(0, tk.END)
            cantidad_entry.delete(0, tk.END)
            precio_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")


    def eliminar_orden():
        # Obtener el índice de la orden seleccionada en la lista
        seleccion = lista_orden.curselection()

        # Verificar si se seleccionó una orden
        if seleccion:
            # Obtener la orden seleccionada
            orden_seleccionada = lista_orden.get(seleccion)

            # Obtener el producto de la orden seleccionada
            producto = orden_seleccionada.split(' (')[0]

            # Eliminar la orden de la base de datos
            cursor.execute("DELETE FROM ordenes_compra WHERE producto=?", (producto,))
            conexion.commit()

            # Eliminar la orden de la lista visual
            lista_orden.delete(seleccion)

            # Actualizar el total
            calcular_total()
        else:
            messagebox.showwarning("Error", "No se ha seleccionado ninguna orden.")


    def actualizar_lista():
        cursor.execute("SELECT * FROM ordenes_compra")
        ordenes = cursor.fetchall()

        lista_orden.delete(0, tk.END)

        for orden in ordenes:
            producto = orden[1]
            cantidad = orden[2]
            precio = orden[3]
            lista_orden.insert(tk.END, f"{producto} ({cantidad}) - ${precio:.2f}")

    def calcular_total():
        total = 0

        for i in range(lista_orden.size()):
            orden = lista_orden.get(i)
            precio_inicio = orden.rfind("$") + 1
            precio = float(orden[precio_inicio:])
            total += precio


        total_label.config(text=f"Total: ${total:.2f}")

           


    def generar_informe():
        # Conexión a la base de datos
        conexion = sqlite3.connect("ordenes_compra.db")
        cursor = conexion.cursor()

        # Obtener los datos de las órdenes de compra
        cursor.execute("SELECT * FROM ordenes_compra")
        ordenes = cursor.fetchall()

        # Crear el documento PDF
        c = canvas.Canvas("informe_ordenes.pdf")

        # Título del informe
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, 750, "Informe de Órdenes de Compra")
        c.setFont("Helvetica", 12)

        # Contenido del informe
        y = 700  # Posición vertical inicial

        # Crear una lista para almacenar los datos de las órdenes
        datos_orden = []

        for orden in ordenes:
            producto = orden[1]
            cantidad = orden[2]
            precio = orden[3]

            # Agregar los datos de la orden a la lista
            datos_orden.append(f"{producto} ({cantidad}) - ${precio:.2f}")

        # Imprimir los datos de las órdenes en el informe
        for dato in datos_orden:
            c.drawString(50, y, dato)
            y -= 20

        # Guardar y cerrar el documento PDF
        c.save()

        messagebox.showinfo("Informe generado", "Se ha generado el informe de órdenes de compra.")



    # Interfaz de usuario

 # Interfaz de usuario

    titulo_label = tk.Label(ventana_principal, text="Sistema de Órdenes de Compras", font=("Helvetica", 18), bg="DarkOliveGreen", fg="white")
    titulo_label.pack(pady=10)

    # Marco para ingresar los datos de la orden
    marco_orden = tk.LabelFrame(ventana_principal, text="Nueva Orden de Compra", bg="DarkOliveGreen", fg="white", padx=20, pady=20)
    marco_orden.pack(padx=10, pady=10)

    # Campos de entrada de datos
    producto_label = tk.Label(marco_orden, text="Producto:", bg="DarkOliveGreen", fg="white")
    producto_label.grid(row=0, column=0)
    producto_entry = tk.Entry(marco_orden)
    producto_entry.grid(row=0, column=1)

    cantidad_label = tk.Label(marco_orden, text="Cantidad:", bg="DarkOliveGreen", fg="white")
    cantidad_label.grid(row=1, column=0)
    cantidad_entry = tk.Entry(marco_orden)
    cantidad_entry.grid(row=1, column=1)

    precio_label = tk.Label(marco_orden, text="Precio:", bg="DarkOliveGreen", fg="white")
    precio_label.grid(row=2, column=0)
    precio_entry = tk.Entry(marco_orden)
    precio_entry.grid(row=2, column=1)

    agregar_button = tk.Button(marco_orden, text="Agregar Orden", command=agregar_orden)
    agregar_button.grid(row=3, columnspan=2, pady=10)

    # Marco para mostrar la lista de órdenes
    marco_lista = tk.LabelFrame(ventana_principal, text="Lista de Órdenes de Compra", bg="DarkOliveGreen", fg="white", padx=20, pady=20)
    marco_lista.pack(padx=10, pady=10)

    lista_orden = tk.Listbox(marco_lista, width=50)
    lista_orden.pack()

    eliminar_button = tk.Button(marco_lista, text="Eliminar Orden", command=eliminar_orden)
    eliminar_button.pack(pady=10)

    # Etiqueta para mostrar el total
    total_label = tk.Label(ventana_principal, text="Total: $0.00", font=("Helvetica", 14), bg="DarkOliveGreen", fg="white")
    total_label.pack(pady=10)

    # Botón para generar el informe
    informe_button = tk.Button(ventana_principal, text="Generar Informe", command=generar_informe)
    informe_button.pack(pady=10)

    # Cargar las órdenes existentes al iniciar la aplicación
    actualizar_lista()
    calcular_total()

    ventana_principal.mainloop()



ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("400x400")
ventana_login.configure(bg="DarkOliveGreen")




background_image = ImageTk.PhotoImage(Image.open("oldschool.png"))
background_label = tk.Label(ventana_login, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


ventana_login.iconbitmap("Orden-de.ico") # Icono

usuario_label = tk.Label(ventana_login, text="Usuario:", bg="DarkOliveGreen", fg="white")
usuario_label.pack(pady=9)
usuario_entry = tk.Entry(ventana_login)
usuario_entry.pack(pady=5)

contrasena_label = tk.Label(ventana_login, text="Contraseña:", bg="DarkOliveGreen", fg="white")
contrasena_label.pack(pady=10)
contrasena_entry = tk.Entry(ventana_login, show="*")
contrasena_entry.pack(pady=5)

login_button = tk.Button(ventana_login, text="Iniciar sesión", command=verificar_credenciales)
login_button.pack(pady=10)

ventana_login.mainloop()


