import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

obras_sociales = ["PAMI", "OSEP", "IOSFA", "SWISS MEDICAL"]

def validar():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()

    if usuario == "admin" and contrasena == "123":
        ventana_validacion = tk.Toplevel(ventana)
        ventana_validacion.title("Validación de paciente")
        ventana_validacion.geometry("400x300")

        etiqueta_nombre = tk.Label(ventana_validacion, text="Nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_validacion)
        entrada_nombre.pack()

        etiqueta_apellido = tk.Label(ventana_validacion, text="Apellido:")
        etiqueta_apellido.pack()

        entrada_apellido = tk.Entry(ventana_validacion)
        entrada_apellido.pack()

        etiqueta_obra_social = tk.Label(ventana_validacion, text="Obra Social:")
        etiqueta_obra_social.pack()

        entrada_obra_social = tk.Entry(ventana_validacion)
        entrada_obra_social.pack()

        def guardar_datos():
            nombre = entrada_nombre.get()
            apellido = entrada_apellido.get()
            obra_social = entrada_obra_social.get()

            if obra_social in obras_sociales:
                descuento = True
            else:
                descuento = False

            generar_pdf(nombre, apellido, obra_social, descuento)

            entrada_nombre.delete(0, tk.END)
            entrada_apellido.delete(0, tk.END)
            entrada_obra_social.delete(0, tk.END)

            messagebox.showinfo("Datos guardados", "Datos del paciente guardados correctamente")

        boton_guardar = tk.Button(ventana_validacion, text="Guardar", command=guardar_datos)
        boton_guardar.pack()
    else:
        messagebox.showerror("Error de validación", "Usuario o contraseña incorrectos")

    entrada_usuario.delete(0, tk.END)
    entrada_contrasena.delete(0, tk.END)

def generar_pdf(nombre, apellido, obra_social, descuento):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Recetario del Paciente", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Apellido: {apellido}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Obra Social: {obra_social}", ln=True, align="L")
    
    if descuento:
        pdf.cell(200, 10, txt="Descuento del 15% aplicado", ln=True, align="L")

    pdf.output("recetario.pdf")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hospital Futura")
ventana.geometry("400x250")

# Crear la etiqueta de usuario
etiqueta_usuario = tk.Label(ventana, text="Usuario:")
etiqueta_usuario.pack()

# Crear la entrada de usuario
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()

# Crear la etiqueta de contraseña
etiqueta_contrasena = tk.Label(ventana, text="Contraseña:")
etiqueta_contrasena.pack()

# Crear la entrada de contraseña
entrada_contrasena = tk.Entry()
