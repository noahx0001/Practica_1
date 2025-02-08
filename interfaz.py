class Interfaz:
    def __init__(self):
        pass

    def menu(self):
        isTrue = True
        while isTrue:
            print("---------------------- | Menu | ----------------------")
            print("| 0. Curso                                           |")
            print("| 1. Estudiante                                      |")
            print("| 2. Inscrito                                        |")
            print("| 3. << Salir >>                                     |")
            print("------------------------------------------------------")
            opcion = input("Ingrese una opcion: ")
            try:
                opcion = int(opcion)
            except ValueError:
                print("\n(Error) ¡El valor ingresado no es un numero!\n")
            else:
                return opcion

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.menu()