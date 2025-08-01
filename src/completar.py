from utils import cargar_tareas, guardar_tareas

def completar_tarea(indice:int) -> None:
    tareas = cargar_tareas()
    
    if 0 <= indice < len(tareas):
        if tareas[indice]["completada"]:
            print(f"la tarea #'{indice}' ya estaba marcada como completada")
        else:
            tareas[indice]["completada"] = True
            guardar_tareas(tareas)
            print(f"tarea #'{indice}' marcada como completada")

    else: print(f"indice fuera de rango. Hay '{len(tareas)}' tarea(s) registradas")