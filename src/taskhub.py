import argparse #para leer argumentos desde la terminal
import json #guardar y leer archivos .json
import os #para construir rutas
from datetime import datetime #para registrar fecha y hora cuando se agrega una tarea
from typing import Dict #para decir cuando una variable forma parte de un diccionario con clave y valores

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

def main():
    #crea el objeto parser que lee los inputs de la terminal
    parser = argparse.ArgumentParser(description="TaskHub, gestor de tareas laborales") 
    #crea un conjunto de subcomandos
    subparsers = parser.add_subparsers(dest="comando", required=True)
    
    #Subcomando: agregar
    #define lo que el subcomando agregar recibe
    agregar_parser = subparsers.add_parser("agregar", help="agregar nueva tarea")
    agregar_parser.add_argument("--nombre", required=True, help="nombre de la tarea")
    agregar_parser.add_argument("--tiempo", required=True, type=int, help="tiempo estimado de la tarea en minutos")
    agregar_parser.add_argument("--proyecto", default="General", help="Nombre del proyecto (opcional)")

    listar_parser = subparsers.add_parser("listar", help="Listar todos los comandos")
    listar_parser.add_argument("--proyecto", help="Filtrar por nombre del proyecto(Opcional)")

    args = parser.parse_args() #analiza lo escrito en la terminal
    #verifica que el comando haya sido agregar
    if args.comando == "agregar":
        #llama a la función agregar_tareas con los datos recibidos
        agregar_tareas(args.nombre, args.tiempo, args.proyecto)
    elif args.comando == "listar":
        listar_tareas(args.proyecto)

    #ejemplo en la consola:
    #python src/taskhub.py agregar --nombre "Enviar informe" --tiempo 20 --proyecto "Contabilidad"

if __name__ == "__main__":
    main()