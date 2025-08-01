import argparse
import json
import os
from datetime import datetime
from typing import Dict 

DATA_FILE = os.path.join("data","tareas.json")

def cargar_tareas() -> list:
    """cargar tareas desde archivo JSON si existe """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_tareas(tareas:list) -> None:
    """Guarda la lista de tareas en el archivo JSON"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

def agregar_tareas(nombre: str, tiempo_estimado: int, proyecto: str = "General") ->None:
    """Agregar una nueva tarea a la lista"""
    tareas = cargar_tareas()
    nueva_tarea: Dict = {
        "Nombre": nombre,
        "tiempo_estimado": tiempo_estimado,
        "proyecto": proyecto,
        "completada": False,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(f"Tarea'{nombre}' añadida correctamente. ")

def main():
    parser = argparse.ArgumentParser(description="TaskHub, gestor de tareas laborales")

    subparsers = parser.add_subparsers(dest="comando", required=True)
    
    #Subcomando: agregar
    agregar_parser = subparsers.add_parser("agregar", help="agregar nueva tarea")
    agregar_parser.add_argument("--nombre", required=True, help="nombre de la tarea")
    agregar_parser.add_argument("--tiempo", required=True, type=int, help="tiempo estimado de la tarea en minutos")
    agregar_parser.add_argument("--proyecto", default="General", help="Nombre del proyecto (opcional)")

    args = parser.parse_args()

    if args.comando == "agregar":
        agregar_tareas(args.nombre, args.tiempo, args.proyecto)

if __name__ == "__main__":
    main()