from estudiante import Estudiante
from interfaz import Interfaz
from tabulate import tabulate

class InterfazEstudiante(Interfaz):
    def __init__(self, myestudiantes=None):
        self.myestudiantes = myestudiantes if myestudiantes else Estudiante().cargarJson("estudiantes")

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
                        objetoCreado = self.crearObjeto()
                        self.crearArchivo(objetoCreado)
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
            return Estudiante(matricula, nombre, apPaterno, apMaterno, correo)

    def mostrar(self):
        tabla = []
        for indice,estudiante in enumerate(self.myestudiantes.elementos, start=1):
            fila = [indice,estudiante.matricula, estudiante.nombre, estudiante.apPaterno, estudiante.apMaterno, estudiante.correo]
            tabla.append(fila)
        encabezados = ["ID","Matricula", "Nombre", "Apellido Paterno", "Apellido Materno", "Correo"]
        print(tabulate(tabla, headers=encabezados, tablefmt="fancy_grid"))

    def crearArchivo(self, objetoCreado):
        self.myestudiantes.agregar_elemento(objetoCreado)
        self.myestudiantes.crearArchivo("estudiantes")


    def eliminar(self):
        elemento = input("Ingrese el elemento a eliminar: ")
        try:
            elemento = int(elemento)
        except ValueError:
            print("\n(Error) ¡El valor ingresado no es un numero!\n")
        else:
            self.myestudiantes.eliminar_elemento(elemento)
            self.myestudiantes.crearArchivo("estudiantes")
            print("\n(Eliminado) ¡El estudiante ha sido eliminado!\n")
    def actualizar(self):
        elementoActualizar = input("Ingrese el ID del elemento a actualizar: ")
        try:
            elementoActualizar = int(elementoActualizar)
        except ValueError:
            print("\n(Error) ¡El valor ingresado no es un numero!\n")
        else:
            objetoCreado = self.crearObjeto()
            self.myestudiantes.actualizar_elemento(elementoActualizar, objetoCreado)
            self.myestudiantes.crearArchivo("estudiantes")
            print("\n(Actualizado) ¡El estudiante ha sido actualizado!\n")

if __name__ == "__main__":
    interfaz = InterfazEstudiante()
    interfaz.menu()
