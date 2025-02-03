import tkinter as tk
from tkinter import ttk, messagebox

# Función para cerrar la aplicación
def salir():
    ventana.quit()

# Función de login (Ejemplo básico)
def login():
    usuario = entry_usuario.get()
    password = entry_password.get()
    if usuario == "admin" and password == "1234":  # Credenciales de prueba
        ventana_login.destroy()
        menu_principal()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Ventana de Inicio de Sesión
ventana_login = tk.Tk()
ventana_login.title("Zapatería - Login")
ventana_login.geometry("300x200")

tk.Label(ventana_login, text="Usuario:").pack(pady=5)
entry_usuario = tk.Entry(ventana_login)
entry_usuario.pack()

tk.Label(ventana_login, text="Contraseña:").pack(pady=5)
entry_password = tk.Entry(ventana_login, show="*")
entry_password.pack()

btn_login = tk.Button(ventana_login, text="Ingresar", command=login)
btn_login.pack(pady=10)

ventana_login.mainloop()

# Función para mostrar el menú principal
def menu_principal():
    global ventana
    ventana = tk.Tk()
    ventana.title("Sistema de Zapatería")
    ventana.geometry("500x300")

    ttk.Label(ventana, text="Bienvenido al Sistema de Zapatería", font=("Arial", 14)).pack(pady=20)

    ttk.Button(ventana, text="Gestionar Ventas", command=gestionar_ventas).pack(pady=5)
    ttk.Button(ventana, text="Gestionar Inventario", command=gestionar_inventario).pack(pady=5)
    ttk.Button(ventana, text="Salir", command=salir).pack(pady=5)

    ventana.mainloop()

# Función para abrir la ventana de ventas
def gestionar_ventas():
    ventana_ventas = tk.Toplevel(ventana)
    ventana_ventas.title("Gestión de Ventas")
    ventana_ventas.geometry("400x300")

    tk.Label(ventana_ventas, text="Registro de Venta", font=("Arial", 12)).pack(pady=10)

    tk.Label(ventana_ventas, text="Cliente:").pack()
    entry_cliente = tk.Entry(ventana_ventas)
    entry_cliente.pack()

    tk.Label(ventana_ventas, text="Producto:").pack()
    entry_producto = tk.Entry(ventana_ventas)
    entry_producto.pack()

    tk.Label(ventana_ventas, text="Cantidad:").pack()
    entry_cantidad = tk.Entry(ventana_ventas)
    entry_cantidad.pack()

    btn_guardar = ttk.Button(ventana_ventas, text="Registrar Venta", command=lambda: messagebox.showinfo("Info", "Venta Registrada"))
    btn_guardar.pack(pady=10)

# Función para abrir la ventana de inventario
def gestionar_inventario():
    ventana_inventario = tk.Toplevel(ventana)
    ventana_inventario.title("Gestión de Inventario")
    ventana_inventario.geometry("400x300")

    tk.Label(ventana_inventario, text="Registro de Producto", font=("Arial", 12)).pack(pady=10)

    tk.Label(ventana_inventario, text="Nombre del Producto:").pack()
    entry_nombre = tk.Entry(ventana_inventario)
    entry_nombre.pack()

    tk.Label(ventana_inventario, text="Cantidad en Stock:").pack()
    entry_stock = tk.Entry(ventana_inventario)
    entry_stock.pack()

    btn_guardar = ttk.Button(ventana_inventario, text="Registrar Producto", command=lambda: messagebox.showinfo("Info", "Producto Registrado"))
    btn_guardar.pack(pady=10)
