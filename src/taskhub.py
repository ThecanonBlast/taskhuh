import argparse #para leer argumentos desde la terminal
from agregar import agregar_tareas
from listar import listar_tareas

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