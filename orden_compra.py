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
    conexion.commit()

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
