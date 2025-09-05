# Sardina

Sardina es un programa simple para flashear imágenes en dispositivos de almacenamiento desde la terminal o con interfaz.

## Modo GUI
![](./resources/capture-gui.png)

## Modo CLI
![](./resources/capture-cli.png)

## Instalación

Para usar el modo *CLI* necesitarás `questionary` como dependencia de Python, puedes lanzarlo con un entorno `venv` gestionado con python/pip, mediante `uv` o usando la shell `nix` preparada en el proyecto.

Para el modo *GUI* necistarás `tkinter`, puedes instalarlo en sistemas debian/ubuntu mediante `sudo apt install python3-tk`

### Debian/Ubuntu:

```bash
# gui
git clone https://github.com/weirdflexbutokz/sardina
cd sardina 
python3 gui.py
```

### NixOs

```bash
git clone https://github.com/weirdflexbutokz/sardina
cd sardina
nix-shell
python3 gui.py
```

### venv

```bash
git clone https://github.com/weirdflexbutokz/sardina
cd sardina
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 gui.py
```

### uv

```bash
git clone https://github.com/weirdflexbutokz/sardina
cd sardina
uv venv
source .venv/bin/activate
uv add -r requirements.txt
python3 gui.py
```

### nix

```bash
git clone https://github.com/weirdflexbutokz/sardina
cd sardina
nix-shell
python3 cli.py
python3 gui.py
```