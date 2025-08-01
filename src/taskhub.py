import argparse #para leer argumentos desde la terminal
from agregar import agregar_tareas
from listar import listar_tareas
from completar import completar_tarea
from eliminar import eliminar_tarea
from editar import editar_tarea


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

    #listar
    listar_parser = subparsers.add_parser("listar", help="Listar todos los comandos")
    listar_parser.add_argument("--proyecto", help="Filtrar por nombre del proyecto(Opcional)")

    #completar
    completar_parser = subparsers.add_parser("completar", help="marcar como completada")
    completar_parser.add_argument("--indice", required=True, type=int, help="indice de la tarea a completar")

    #eliminar
    eliminar_parser = subparsers.add_parser("eliminar", help="Eliminar una tarea por su indice")
    eliminar_parser.add_argument("--indice", required=True, type=int, help="indice de la tarea a eliminar")

    #Editar
    editar_parser = subparsers.add_parser("editar", help="Editar una tarea existente")
    editar_parser.add_argument("--indice", required=True, type=int, help="Índice de la tarea a editar")
    editar_parser.add_argument("--nombre", help="Nuevo nombre de la tarea")
    editar_parser.add_argument("--tiempo", type=int, help="Nuevo tiempo estimado (minutos)")    
    editar_parser.add_argument("--proyecto", help="Nuevo nombre del proyecto")

    args = parser.parse_args() #analiza lo escrito en la terminal
    #verifica que el comando haya sido agregar
    if args.comando == "agregar":
        #llama a la función agregar_tareas con los datos recibidos
        agregar_tareas(args.nombre, args.tiempo, args.proyecto)
    elif args.comando == "listar":
        listar_tareas(args.proyecto)

    if args.comando == "completar":
        completar_tarea(args.indice)
    
    if args.comando == "eliminar":
        eliminar_tarea(args.indice)
    elif args.comando == "editar":
        editar_tarea(args.indice, args.nombre, args.tiempo, args.proyecto)

    #ejemplo en la consola:
    #python src/taskhub.py agregar --nombre "Enviar informe" --tiempo 20 --proyecto "Contabilidad"

if __name__ == "__main__":
    main()