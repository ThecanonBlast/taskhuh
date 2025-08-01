from utils import cargar_tareas, guardar_tareas

def editar_tarea(indice: int, nombre: str = None, tiempo: int = None, proyecto: str = None) -> None:
    tareas = cargar_tareas()

    if 0 <= indice < len(tareas):
        tarea = tareas[indice]
        if nombre:
            tarea["Nombre"] = nombre
        if tiempo is not None:
            tarea["tiempo_estimado"] = tiempo
        if proyecto:
            tarea["proyecto"] = proyecto

        guardar_tareas(tareas)
        print(f"Tarea #{indice} actualizada correctamente.")
    else:
        print(f"Índice fuera de rango. Hay {len(tareas)} tarea(s) registradas.")
