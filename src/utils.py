import json #guardar y leer archivos .json
import os #para construir rutas

DATA_FILE = os.path.join("data","tareas.json") #crear la ruta para las tareas

def cargar_tareas() -> list:
    """cargar tareas desde archivo JSON si existe """
    if os.path.exists(DATA_FILE): #comprueba si el archivo existe
        with open(DATA_FILE, "r", encoding="utf-8") as f: #abre y carga contenido en el archivo que existe
            return json.load(f)
    return [] #si no existe, retorna una lista vacía

def guardar_tareas(tareas:list) -> None: #recibe la lista de tareas y no retorna nada
    """Guarda la lista de tareas en el archivo JSON"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)#crea data/ si no existe
    with open(DATA_FILE, "w", encoding="utf-8") as f: #abre en modo escritura (w) para sobreescribirlo
        json.dump(tareas, f, indent=4, ensure_ascii=False) #guarda la lista de tareas en JSON y con sangría para que sea legible
