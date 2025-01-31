
from estudiante import Estudiante
from curso import Curso
from lista import Lista
from datetime import datetime
import json
class Inscrito(Lista):
    def __init__(self,estudiantes: Estudiante=None, curso: Curso=None, fechaInscripcion=None):
        self.isObject=estudiantes and curso and fechaInscripcion
        if self.isObject:    
            self.estudiantes = estudiantes
            self.curso = curso
            self.fechaInscripcion = fechaInscripcion
        else:
            super().__init__()

    def __str__(self):
        return str(self.conversion())
    def conversion(self):
         if self.isObject:
            inscritoDict = dict(
                estudiantes=self.estudiantes.conversion(),
                curso=self.curso.conversion(),
                fechaInscripcion=self.fechaInscripcion.isoformat())
            return inscritoDict
         elif hasattr(self, "elementos"):
            inscritos = []
            for inscrito in self.elementos:
                inscritoDict = inscrito.conversion()
                inscritos.append(inscritoDict)
            return inscritos
         else:
            return None
    def crearObjeto(self,myjson):
        if isinstance(myjson, dict):
            return Inscrito(
                Estudiante().crearObjeto(myjson["estudiantes"]),
                Curso().crearObjeto(myjson["curso"]),
                datetime.fromisoformat(myjson["fechaInscripcion"])
                )
        elif isinstance(myjson, list):
            self.elementos = []
            for v in myjson:
                inscritos.agregar_elemento(self.crearObjeto(v))
            return self.elementos
        else:
            return None
    def cargarJson(self, nombreArchivo):
        myjson = json.load(open(nombreArchivo+".json"))
        return self.crearObjeto(myjson)
    
if __name__ == "__main__":
        """
        
        """
        
        """
        inscritos.agregar_elemento(inscrito1)
        inscritos.agregar_elemento(inscrito1)

        inscrito1.crearArchivo("inscrito1")
        inscritos.crearArchivo("inscritos")

        estudiante4 = Estudiante(101, "Luis", "Gonzalez", "Gomez", "VXyOa@example.com")
        print 
        inscrito1.estudiantes.agregar_elemento(estudiante4)
        """
        estudiante1 = Estudiante(123, "Juan", "Perez", "Gomez", "cBp7o@example.com")
        estudiante2 = Estudiante(456, "Pedro", "Lopez", "Garcia", "2r4y6@example.com")
        estudiante3 = Estudiante(789, "Maria", "Gonzalez", "Gomez", "VXyOa@example.com")

        curso1 = Curso("Programacion", "Curso de Python", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")

        estudiantes=Estudiante();

        estudiantes.agregar_elemento(estudiante1)
        estudiantes.agregar_elemento(estudiante2)
        estudiantes.agregar_elemento(estudiante3)

        inscrito1 = Inscrito(estudiantes, curso1, datetime(2023, 6, 1))

        inscritos = Inscrito()

        inscritos.cargarJson("inscritos")

        inscritos.agregar_elemento(inscrito1)

        inscritos.crearArchivo("inscritos")

        print(inscritos)












