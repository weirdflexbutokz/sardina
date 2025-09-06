import questionary
import subprocess
import os
import json

def obtener_usbs():
    resultado = subprocess.run(
        ["lsblk", "-o", "NAME,MODEL,TRAN,SIZE,MOUNTPOINT", "-J"],
        capture_output=True, text=True
    )
    dispositivos = []
    data = json.loads(resultado.stdout)
    for device in data["blockdevices"]:
        if device.get("tran") == "usb":
            nombre = f"/dev/{device['name']} ({device.get('model','')}, {device['size']})"
            dispositivos.append(nombre)
    return dispositivos

def main():
    ruta_imagen = questionary.path("¿Cuál es el path de la imagen que deseas flashear?").ask()
    ruta_imagen = os.path.expanduser(ruta_imagen)

    usbs = obtener_usbs()
    if not usbs:
        print("No se detectaron dispositivos USB.")
        return
    dispositivo = questionary.select(
        "¿En qué dispositivo USB deseas flashear la imagen?",
        choices=usbs
    ).ask()
    print(f"Imagen: {ruta_imagen}")
    print(f"Dispositivo seleccionado: {dispositivo}")

    print("\nResumen de selección:")
    print(f"- Imagen a flashear: {ruta_imagen}")
    print(f"- Dispositivo USB: {dispositivo}")
    proceder = questionary.confirm("¿Deseas proceder con el flasheo?").ask()
    if proceder:
        print("Procediendo con el flasheo...")
        path_dispositivo = dispositivo.split(" ")[0]
        comando = [
            "sudo", "dd", f"if={ruta_imagen}", f"of={path_dispositivo}", "bs=64M", "status=progress", "conv=fsync"
        ]
        proceso = subprocess.run(comando)
        if proceso.returncode == 0:
            print("Flasheo completado exitosamente.")
        else:
            print("Ocurrió un error durante el flasheo.")

if __name__ == "__main__":
    main()