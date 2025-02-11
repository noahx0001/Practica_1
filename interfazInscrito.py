from inscrito import Inscrito
from tabulate import tabulate
from datetime import datetime
from interfazCurso import InterfazCurso
from interfazEstudiante import InterfazEstudiante
from estudiante import Estudiante
class InterfazInscrito:
    def __init__(self, myinscritos=None):
        if myinscritos:
            self.myinscritos = myinscritos
            self.isJson = False
        else:
            self.myinscritos = Inscrito().cargarJson("inscritos")
            self.isJson = True
 
    def menu(self):
        isTrue = True
        while isTrue:
            print("---------------------- | Inscrito | ------------------")
            print("| 0. Insertar                                        |\n| 1. Actualizar                                      |\n| 2. Delete                                          |\n| 3. Mostrar                                         |\n| 4. Salir                                           |\n------------------------------------------------------")
            opcion = input("Ingrese una opcion: ")
            try:
                opcion = int(opcion)
            except ValueError:
                print("\n(Error) ¡El valor ingresado no es un numero!\n")
            else:
                match opcion:
                    case 0:
                        self.crearObjeto()
                    case 1:
                        self.actualizar()
                    case 2:
                        self.eliminar()
                    case 3:
                        self.mostrar()
                    case 4:
                        isTrue = False
                    case _:
                        print("\n(Error) ¡La opcion ingresada no es valida!\n")

    def crearObjeto(self):
        curso = InterfazCurso().crearObjeto()
        interfazEstudiante = InterfazEstudiante(Estudiante())
        interfazEstudiante.menu()
        estudiantes = interfazEstudiante.myestudiantes
        print("--------------(Crear: Inscripción-Objeto)--------------")
        while True:
            try:
                fechaInscripcion = datetime.fromisoformat(input("- Ingrese la fecha de inscripción: "))
                break
            except ValueError:
                print("\n(Error) ¡Ingrese en formato YYYY-MM-DD!\n")
        inscrito = Inscrito(estudiantes,curso,fechaInscripcion)
        self.myinscritos.agregar_elemento(inscrito)
        print("\n(Creado) ¡La inscripción ha sido creada!\n")

    def eliminar(self):
        self.mostrar()
        elemento = input("Ingrese el ID de la inscripción a eliminar: ")
        try:
            elemento = int(elemento)
            self.myinscritos.eliminar_elemento(elemento)
            self.guardarInscritos("inscritos")
            print("\n(Eliminado) ¡La inscripción ha sido eliminada!\n")
        except ValueError:
            print("\n(Error) ¡El valor ingresado no es un número!\n")

    def actualizar(self):
        self.mostrar()
        opcion = input("\nIngrese el ID de la inscripción a actualizar: ")
        try: 
            opcion = int(opcion)
        except ValueError:
            print("\n(Error) ¡El valor ingresado no es un número!\n")
        else:
            insSelected = self.myinscritos.elementos[opcion - 1]
            print("\n1. Estudiantes\n2. Curso\n3. Fecha de Inscripción\n")
            opcion2 = input("¿Que desea actualizar?")
            try:
                opcion2 = int(opcion2)
            except ValueError:
                print("\n(Error) ¡El valor ingresado no es un número!\n")
            else:
                match opcion2:
                    case 1:
                        interfazEstudiante = InterfazEstudiante(self.myinscritos.elementos[opcion - 1].estudiantes)
                        interfazEstudiante.menu()
                        insSelected.estudiantes = interfazEstudiante.myestudiantes
                        self.guardarInscritos("inscritos")
                    case 2:
                        cursoNuevo = InterfazCurso(self.myinscritos.elementos[opcion - 1].curso).actualizar()
                        insSelected.curso = cursoNuevo
                        self.guardarInscritos("inscritos")
                    case 3:
                        while True:
                            try:
                                fechaInscripcion = datetime.fromisoformat(input("- Ingrese la fecha de inscripción: "))
                                break
                            except ValueError:
                                print("\n(Error) ¡Ingrese en formato YYYY-MM-DD!\n")
                        insSelected.fechaInscripcion = fechaInscripcion
                        self.guardarInscritos("inscritos")
                        print("\n(Actualizado) ¡La inscripción ha sido actualizada!\n")


    def mostrar(self):
        tabla = []
        for indice, inscrito in enumerate(self.myinscritos.elementos, start=1):
            try:
                estudiantes = []
                for i,estudiante in enumerate(inscrito.estudiantes.elementos, start=1):
                    estudiantes.append(f"{i}. {estudiante.nombre} {estudiante.apPaterno} {estudiante.apMaterno}")
                fila = [indice,"\n".join(estudiantes), inscrito.curso.nombre, inscrito.fechaInscripcion.strftime('%Y-%m-%d')]
                tabla.append(fila)
            except AttributeError as e:
                print(f"Error al acceder a los atributos: {e}")
                continue
        
        encabezados = ["ID", "Estudiantes", "Curso", "Fecha Inscripción"]
        print(tabulate(tabla, headers=encabezados, tablefmt="fancy_grid"))
    def guardarInscritos(self, nombreArchivo):
        if self.isJson:
            self.myinscritos.crearArchivo(nombreArchivo)
if __name__ == "__main__":
    interfaz = InterfazInscrito()
    interfaz.menu()