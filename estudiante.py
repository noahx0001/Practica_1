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
        
    def crearObjeto(self,myjson):
        if isinstance(myjson, dict):
            return Estudiante(myjson["matricula"], myjson["nombre"], myjson["apPaterno"], myjson["apMaterno"], myjson["correo"])
        elif isinstance(myjson, list):
            estudiantes = Estudiante()
            for v in myjson:
                estudiantes.agregar_elemento(self.crearObjeto(v))
            return estudiantes
        else:
            return None
    def __repr__(self):
        return self.__str__()
if __name__ == "__main__":
    estudiante1 = Estudiante(123, "Juan", "Perez", "Gomez", "cBp7o@example.com")
    estudiante2 = Estudiante(456, "Pedro", "Lopez", "Garcia", "2r4y6@example.com")
    estudiante3 = Estudiante(789, "Maria", "Gonzalez", "Gomez", "VXyOa@example.com")
    estudiante4 = Estudiante(101, "Luis", "Gonzalez", "Gomez", "VXyOa@example.com")
    estudiante5 = Estudiante(101, "Dante", "Ramirez", "Lopez", "VXyOa@example.com")
    estudiantes = Estudiante();
    
    # Agregando elementos a la lista de estudiantes
    estudiantes.agregar_elemento(estudiante1);
    estudiantes.agregar_elemento(estudiante2);
    estudiantes.agregar_elemento(estudiante3);
    estudiantes.agregar_elemento(estudiante4);
    estudiantes.agregar_elemento(estudiante5);

    # Creacion del archivo json para estudiantes
    estudiantes.crearArchivo("estudiantes")

    # Creacion del archivo json para el estudiante
    estudiante1.crearArchivo("estudiante1")

    # Crear un objeto a partir de un archivo
    estudiantesObject = estudiantes.crearObjeto(estudiantes.cargar("estudiantes"))
    estudianteObject = estudiante1.crearObjeto(estudiante1.cargar("estudiante1"))

    print(estudiantesObject.elementos[0].nombre)
    print(estudianteObject.nombre)










