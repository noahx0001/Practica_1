from curso import Curso
from estudiante import Estudiante
from inscrito import Inscrito
class Interfaz:
    def __init__(self):
        pass
    def menu(self):
        print("---------------------- | Menu | ----------------------")
        print("| 0. Curso                                           |")
        print("| 1. Estudiante                                      |")
        print("| 2. Inscrito                                        |")
        print("| 3. << Salir >>                                     |")
        print("------------------------------------------------------")
        isTrue = True
        while isTrue:
            opcion = input("Ingrese una opcion: ")
            try:
                opcion = int(opcion)
            except ValueError:
                print("\n(Error) ¡El valor ingresado no es un numero!\n")
            else:
                match opcion:
                    case 0:
                        Interfaz.subMenu(opcion)
                    case 1:
                        print("Estudiante")
                    case 2:
                        print("Inscrito")
                    case 3:
                        isTrue = False
                        print("\n¡Hasta luego!\n")
                    case _:
                        print("\n-----------------| Opcion no valida |-----------------\n")
                
                print("---------------------- | Menu | ----------------------")
                print("| 0. Curso                                           |")
                print("| 1. Estudiante                                      |")
                print("| 2. Inscrito                                        |")
                print("| 3. << Salir >>                                     |")
                print("------------------------------------------------------")

    def subMenu(opcion):
        match opcion:
            case 0:
                 print("---------------------- | Curso | ----------------------")
            case 1:
                 print("---------------------- | Estudiante | ----------------------")
            case 2:
                 print("---------------------- | Inscrito | ----------------------")

        print("0. Crear")
        print("1. Actualizar")
        print("2. Delete")
        print("3. Mostrar")
        print("3. << Atras >> ")
        print("------------------------------------------------------")
        isTrue = True
        while isTrue:
            opcion = input("Ingrese una opcion: ")
            try:
                opcion = int(opcion)
            except ValueError:
                print("\n(Error) ¡El valor ingresado no es un numero!\n")
            else:
                match opcion:
                    case 0:
                        print("Crear")
                    case 1:
                        print("Actualizar")
                    case 2:
                        print("Delete")
                    case 3:
                        print("Mostrar")
                    case 4:
                        isTrue = False
                    case _:
                        print("\n-----------------| Opcion no valida |-----------------\n")
                



if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.menu()