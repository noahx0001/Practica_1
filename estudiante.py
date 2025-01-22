from lista import Lista
class Estudiante(Lista):
    def __init__(self=None, matricula=None, nombre=None, apPaterno=None, apMaterno=None, correo=None):

        self.isObject=matricula and nombre and apPaterno and apMaterno and correo    
        if self.isObject:
            self.matricula = matricula
            self.nombre = nombre
            self.apPaterno = apPaterno
            self.apMaterno = apMaterno
            self.correo = correo
        else:
            super().__init__()

    
    def __str__(self):
        return str(self.conversion())
    
    def conversion(self):
        if self.isObject:
            estudianteDict = dict(matricula=self.matricula, nombre=self.nombre, apPaterno=self.apPaterno, apMaterno=self.apMaterno, correo=self.correo)
            return estudianteDict
        elif hasattr(self, "elementos"):
            estudiantes = []
            for estudiante in self.elementos:
                estudianteDict = estudiante.conversion()
                estudiantes.append(estudianteDict)
            return estudiantes
        else:
            return None
    def crearObjeto(self,file_name):
        dictionary = self.cargar(file_name)
        if isinstance(dictionary, dict):
            return Estudiante(dictionary["matricula"], dictionary["nombre"], dictionary["apPaterno"], dictionary["apMaterno"], dictionary["correo"])
        else:
            self.elementos
            for estudiante in dictionary:
                estudiantes.agregar_elemento(self.crearObjeto(estudiante))
            return estudiantes
        
    def __repr__(self):
        return self.__str__()
if __name__ == "__main__":
    estudiante1 = Estudiante(123, "Juan", "Perez", "Gomez", "cBp7o@example.com")
    estudiante2 = Estudiante(456, "Pedro", "Lopez", "Garcia", "2r4y6@example.com")
    estudiante3 = Estudiante(789, "Maria", "Gonzalez", "Gomez", "VXyOa@example.com")
    estudiantes = Estudiante();
    
    estudiantes.agregar_elemento(estudiante1);
    estudiantes.agregar_elemento(estudiante2);
    estudiantes.agregar_elemento(estudiante3);

    estudiantes.crearArchivo("estudiantes")

    estudiante1.crearArchivo("estudiante1")

    estudiantes = estudiantes.crearObjeto("estudiantes")
    estudiante = estudiantes.crearObjeto("estudiante1")

    print(estudiante)
    print(type(estudiante))
    print(estudiantes)
    print(type(estudiantes))





