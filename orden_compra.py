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
