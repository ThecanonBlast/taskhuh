from utils import cargar_tareas

def listar_tareas(proyecto_filtro: str =None) ->None:
    """Permite mostrar las tareas almacenadas, opcionalmente filtradas por proyectos"""
    tareas = cargar_tareas()

    if not tareas:
        print("No hay tareas registradas")
        return

    if proyecto_filtro:
        tareas=[t for t in tareas if t["proyecto"].lower() == proyecto_filtro.lower()]
        if not tareas: 
            print(f"no hay tareas registradas para el proyecto '{proyecto_filtro}'.")
            return
        
    print("\n Lista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "OK" if tarea["completada"] else "nop"
        print(f"{i}. {tarea['Nombre']} [{tarea['proyecto']}] - {tarea ['fecha']} - {estado}")
