import tkinter as tk
from opciones import *

def registrar_ui():
    resultado = registrar(entry_name.get(), entry_heigh.get(), 
                           entry_gender.get(),entry_Last_name.get())
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, resultado)

def mostrar_ui():
    resultado = mostrar()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, resultado)

def borrar_ui():
    apellido = borrar_entry.get()
    resultado = borrar(apellido)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, resultado)

window = tk.Tk()
window.title("Registro de estudiantes")

tk.Label(window, text="Ingrese el nombre de un estudiante: ").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Ingrese el apellido del estudiante: ").pack()
entry_Last_name = tk.Entry(window)
entry_Last_name.pack()

tk.Label(window, text="Ingrese la altura del estudiante: ").pack()
entry_heigh = tk.Entry(window)
entry_heigh.pack()

tk.Label(window, text="Ingrese el genero del estudiante: ").pack()
entry_gender = tk.Entry(window)
entry_gender.pack()


tk.Button(window, text="Registrar Estudiante", command=registrar_ui).pack(pady=5)
tk.Button(window, text="Mostrar Estudiantes", command=mostrar_ui).pack(pady=5)

tk.Label(window, text="Apellido a borrar:").pack()
borrar_entry = tk.Entry(window)
borrar_entry.pack()
tk.Button(window, text="Borrar Estudiante", command=borrar_ui).pack(pady=5)

tk.Label(window, text="Salida:").pack()
output_text = tk.Text(window, height=10, width=60)
output_text.pack(pady=10)

