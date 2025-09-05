import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def obtener_usbs():
    resultado = subprocess.run(
        ["lsblk", "-o", "NAME,MODEL,TRAN,SIZE,MOUNTPOINT", "-J"],
        capture_output=True, text=True
    )
    import json
    dispositivos = []
    data = json.loads(resultado.stdout)
    for device in data["blockdevices"]:
        if device.get("tran") == "usb":
            nombre = f"/dev/{device['name']} ({device.get('model','')}, {device['size']})"
            dispositivos.append(nombre)
    return dispositivos

def seleccionar_imagen():
    filename = filedialog.askopenfilename(title="Selecciona la imagen")
    imagen_var.set(filename)

def flashear():
    ruta_imagen = imagen_var.get()
    dispositivo = dispositivo_var.get()
    if not ruta_imagen or not dispositivo:
        messagebox.showerror("Error", "Selecciona imagen y dispositivo.")
        return
    path_dispositivo = dispositivo.split(" ")[0]
    comando = ["sudo", "dd", f"if={ruta_imagen}", f"of={path_dispositivo}", "bs=64M", "status=progress", "conv=fsync"]
    messagebox.showinfo("Info", "Se iniciará el flasheo en la terminal.")
    root.destroy()
    subprocess.run(comando)

root = tk.Tk()
root.title("Flasheador simple")

imagen_var = tk.StringVar()
dispositivo_var = tk.StringVar()

# Sección 1: Selección de imagen
frame_imagen = tk.LabelFrame(root, text="1. Selecciona la imagen", padx=10, pady=10)
frame_imagen.pack(fill="x", padx=10, pady=5)
tk.Entry(frame_imagen, textvariable=imagen_var, width=50).pack(side="left", padx=5)
tk.Button(frame_imagen, text="Examinar", command=seleccionar_imagen).pack(side="left", padx=5)

# Sección 2: Selección de USB
frame_usb = tk.LabelFrame(root, text="2. Selecciona el dispositivo USB", padx=10, pady=10)
frame_usb.pack(fill="x", padx=10, pady=5)
usbs = obtener_usbs()
tk.OptionMenu(frame_usb, dispositivo_var, *usbs).pack(side="left", padx=5)

# Sección 3: Botón de empezar
frame_empezar = tk.LabelFrame(root, text="3. Flashear imagen", padx=10, pady=10)
frame_empezar.pack(fill="x", padx=10, pady=5)
tk.Button(frame_empezar, text="Empezar", command=flashear, height=2, width=20).pack(pady=5)

tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

root.geometry("500x250")
root.mainloop()