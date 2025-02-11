from curso import Curso
from tabulate import tabulate
from datetime import datetime

class InterfazCurso:
    def __init__(self, mycursos=None):
        if mycursos:
            self.mycursos = mycursos
            self.isJson = False
        else:
            self.mycursos = Curso().cargarJson("cursos")
            self.isJson = True  

    def menu(self):
        isTrue = True
        while isTrue:
            print("---------------------- | Curso | --------------------")
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
        print("\n--------------(Crear: Curso-Objeto)-------------------\n")
        nombre = input("- Ingrese el nombre del curso: ")
        descripcion = input("- Ingrese la descripción del curso: ")
    
        while True:
            try: 
                fechaInicio = datetime.fromisoformat(input("- Ingrese la fecha de inicio: "))
                fechaFin = datetime.fromisoformat(input("- Ingrese la fecha de fin: "))
                break
            except ValueError:
                print("\n(Error) ¡Ingrese en formato YYYY-MM-DD!\n")
        
        modalidad = input("- Ingrese la modalidad del curso: ")
        
        curso = Curso(nombre, descripcion, fechaInicio, fechaFin, modalidad)
        if self.mycursos.isObject:
            self.mycursos = curso
        else:
            self.mycursos.agregar_elemento(curso)
        self.guardarCursos("cursos")
        print("\n(Creado) ¡El curso ha sido creado!\n")
        return curso

    def mostrar(self):
        tabla = []
        for indice, curso in enumerate(self.mycursos.elementos, start=1):
            fila = [indice, curso.nombre, curso.descripcion, 
                   curso.fechaInicio.strftime('%Y-%m-%d'), 
                   curso.fechaFin.strftime('%Y-%m-%d'), 
                   curso.modalidad]
            tabla.append(fila)
        encabezados = ["ID", "Nombre", "Descripción", "Fecha Inicio", "Fecha Fin", "Modalidad"]
        print(tabulate(tabla, headers=encabezados, tablefmt="fancy_grid"))

    def eliminar(self):
        self.mostrar()
        elemento = input("Ingrese el elemento a eliminar: ")
        try:
            elemento = int(elemento)
        except ValueError:
            print("\n(Error) ¡El valor ingresado no es un numero!\n")
        else:
            self.mycursos.eliminar_elemento(elemento)
            self.guardarCursos("cursos")
            print("\n(Eliminado) ¡El curso ha sido eliminado!\n")

    def actualizar(self):
        if self.mycursos.isObject:
            self.mycursos.nombre = input("Ingrese el nombre del curso: ")
            self.mycursos.descripcion = input("Ingrese la descripción del curso: ")

            while True:
                try: 
                    self.mycursos.fechaInicio = datetime.fromisoformat(input("Ingrese la fecha de inicio: "))
                    self.mycursos.fechaFin = datetime.fromisoformat(input("Ingrese la fecha de fin: "))
                    break
                except ValueError:
                    print("\n(Error) ¡Ingrese en formato YYYY-MM-DD!\n")

            self.mycursos.modalidad = input("Ingrese la modalidad del curso: ")
            self.guardarCursos("cursos")
            print("\n(Actualizado) ¡El curso ha sido actualizado!\n")
            return self.mycursos
        else:
            self.mostrar()
            elementoActualizar = input("Ingrese el ID del elemento a actualizar: ")
            while True:
                try:
                    elementoActualizar = int(elementoActualizar)
                    break
                except ValueError:
                    print("\n(Error) ¡El valor ingresado no es un numero!\n")
            self.mycursos.elementos[elementoActualizar - 1].nombre = input("Ingrese el nombre del curso: ")
            self.mycursos.elementos[elementoActualizar - 1].descripcion = input("Ingrese la descripción del curso: ")
            while True:
                try: 
                    self.mycursos.elementos[elementoActualizar - 1].fechaInicio = datetime.fromisoformat(input("Ingrese la fecha de inicio: "))
                    self.mycursos.elementos[elementoActualizar - 1].fechaFin = datetime.fromisoformat(input("Ingrese la fecha de fin: "))
                    break
                except ValueError:
                    print("\n(Error) ¡Ingrese en formato YYYY-MM-DD!\n")
            self.mycursos.elementos[elementoActualizar - 1].modalidad = input("Ingrese la modalidad del curso: ")
            self.guardarCursos("cursos")
            print("\n(Actualizado) ¡El curso ha sido actualizado!\n")
            return self.mycursos

    def guardarCursos(self, nombreArchivo):
        if self.isJson:
            self.mycursos.crearArchivo(nombreArchivo)
if __name__ == "__main__":
    interfaz = InterfazCurso()
    interfaz.menu()