from utils import cargar_tareas, guardar_tareas

def eliminar_tarea(indice:int) -> None:
    tareas = cargar_tareas()

    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        guardar_tareas(tareas)
        print(f"tarea '{tarea_eliminada['Nombre']}' eliminada correctamente")
    else:
        print(f"indice fuera de rango. Hay {len(tareas)} tarea(s) registradas")    
    