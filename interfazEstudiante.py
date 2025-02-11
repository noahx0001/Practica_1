from estudiante import Estudiante
from tabulate import tabulate

class InterfazEstudiante:
    def __init__(self, myestudiantes=None):
        if myestudiantes:
            self.myestudiantes = myestudiantes
            self.isJson = False
        else:
            self.myestudiantes = Estudiante().cargarJson("estudiantes")
            self.isJson = True

    def menu(self):
       
        isTrue = True
        while isTrue:
            print("---------------------- | Estudiante | ----------------")
            print("| 0. Insertar                                        |\n| 1. Actualizar                                      |\n| 2. Delete                                          |\n| 3. Mostrar                                         |\n| 4. Menu                                            |\n------------------------------------------------------")
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
            print("--------------(Crear: Estudiante-Objeto)--------------")
            nombre = input("- Ingrese el nombre del estudiante: ")
            matricula = input("- Ingrese la matricula del estudiante: ")
            apPaterno = input("- Ingrese el apellido paterno del estudiante: ")
            apMaterno = input("- Ingrese el apellido materno del estudiante: ")
            correo = input("- Ingrese el correo del estudiante: ")
            estudiante = Estudiante(matricula, nombre, apPaterno, apMaterno, correo)
            self.myestudiantes.agregar_elemento(estudiante)
            self.guardarEstudiantes("estudiantes")
            print("\n(Creado) ¡El estudiante ha sido creado!\n")
            return self.myestudiantes


    def mostrar(self):
        tabla = []
        for indice,estudiante in enumerate(self.myestudiantes.elementos, start=1):
            fila = [indice,estudiante.matricula, estudiante.nombre, estudiante.apPaterno, estudiante.apMaterno, estudiante.correo]
            tabla.append(fila)
        encabezados = ["ID","Matricula", "Nombre", "Apellido Paterno", "Apellido Materno", "Correo"]
        print(tabulate(tabla, headers=encabezados, tablefmt="fancy_grid"))

    def eliminar(self):
        self.mostrar()
        elemento = input("Ingrese el elemento a eliminar: ")
        try:
            elemento = int(elemento)
        except ValueError:
            print("\n(Error) ¡El valor ingresado no es un numero!\n")
        else:
            self.myestudiantes.eliminar_elemento(elemento)
            self.guardarEstudiantes("estudiantes")
            print("\n(Eliminado) ¡El estudiante ha sido eliminado!\n")
    def actualizar(self):
        if self.myestudiantes.isObject:
            self.myestudiantes.matricula = input("Ingrese la matricula del estudiante: ")
            self.myestudiantes.nombre = input("Ingrese el nombre del estudiante: ")
            self.myestudiantes.apPaterno = input("Ingrese el apellido paterno del estudiante: ")
            self.myestudiantes.apMaterno = input("Ingrese el apellido materno del estudiante: ")
            self.myestudiantes.correo = input("Ingrese el correo del estudiante: ")
            self.guardarEstudiantes("estudiantes")
            print("\n(Actualizado) ¡El estudiante ha sido actualizado!\n")
            return self.myestudiantes
        else:
            self.mostrar()
            elementoActualizar = input("Ingrese el ID del elemento a actualizar: ")
            while True:
                try:
                    elementoActualizar = int(elementoActualizar)
                    break
                except ValueError:
                    print("\n(Error) ¡El valor ingresado no es un numero!\n")
            self.myestudiantes.elementos[elementoActualizar - 1].matricula = input("Ingrese la matricula del estudiante: ")
            self.myestudiantes.elementos[elementoActualizar - 1].nombre = input("Ingrese el nombre del estudiante: ")
            self.myestudiantes.elementos[elementoActualizar - 1].apPaterno = input("Ingrese el apellido paterno del estudiante: ")
            self.myestudiantes.elementos[elementoActualizar - 1].apMaterno = input("Ingrese el apellido materno del estudiante: ")
            self.myestudiantes.elementos[elementoActualizar - 1].correo = input("Ingrese el correo del estudiante: ")
            self.guardarEstudiantes("estudiantes")
            print("\n(Actualizado) ¡El estudiante ha sido actualizado!\n")
            return self.myestudiantes
    def guardarEstudiantes(self, nombreArchivo):
        if self.isJson:
            self.myestudiantes.crearArchivo(nombreArchivo)

if __name__ == "__main__":
    interfaz = InterfazEstudiante()
    interfaz.menu()
