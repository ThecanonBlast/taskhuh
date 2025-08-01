from typing import Dict #para decir cuando una variable forma parte de un diccionario con clave y valores
from datetime import datetime #para registrar fecha y hora cuando se agrega una tarea
from utils import guardar_tareas
from utils import cargar_tareas

def agregar_tareas(nombre: str, tiempo_estimado: int, proyecto: str = "General") ->None: #recibe datos de las tareas
    """Agregar una nueva tarea a la lista"""
    tareas = cargar_tareas() #carga las tareas existentes
    nueva_tarea: Dict = { #crea el diccionario de tareas con los datos que se trajeron
        "Nombre": nombre,
        "tiempo_estimado": tiempo_estimado,
        "proyecto": proyecto,
        "completada": False,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tareas.append(nueva_tarea) #las agrega a la lista
    guardar_tareas(tareas) #nuevamente guarda las tareas
    print(f"Tarea'{nombre}' añadida correctamente. ") #confirma
