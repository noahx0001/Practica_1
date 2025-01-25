
from datetime import datetime
from lista import Lista
import json
class Curso(Lista):
    def __init__(self, nombre=None, descripcion=None, fechaInicio=None, fechaFin=None, modalidad=None):

        self.isObject=nombre and descripcion and fechaInicio and fechaFin and modalidad

        if self.isObject:
            self.nombre = nombre
            self.descripcion = descripcion
            self.fechaInicio = fechaInicio
            self.fechaFin = fechaFin
            self.modalidad = modalidad
        else:
             super().__init__()

    def __str__(self):
        return str(self.conversion())
    
    def conversion(self):
        if self.isObject:
            cursoDict = dict(nombre=self.nombre, descripcion=self.descripcion, fechaInicio=self.fechaInicio.isoformat(), fechaFin=self.fechaFin.isoformat(), modalidad=self.modalidad)
            return cursoDict
        elif hasattr(self, "elementos"):
            cursos = []
            for curso in self.elementos:
                cursoDict = curso.conversion()
                cursos.append(cursoDict)
            return cursos
        else:
            return None
    def crearObjeto(self, myjson):
        if isinstance(myjson, dict):
            return Curso(myjson["nombre"], myjson["descripcion"], datetime.fromisoformat(myjson["fechaInicio"]), datetime.fromisoformat(myjson["fechaFin"]), myjson["modalidad"])
        elif isinstance(myjson, list):
            cursos = Curso()
            for v in myjson:
                cursos.agregar_elemento(self.crearObjeto(v))    
            return cursos
        else:
            return None
        
if __name__ == "__main__":
    curso1 = Curso("Programacion", "Curso de Python", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso2 = Curso("Matematica", "Curso de Calculo", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso3 = Curso("Fisica", "Curso de Fisica", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")

    cursos= Curso();
    cursos.agregar_elemento(curso1)
    cursos.agregar_elemento(curso2)
    cursos.agregar_elemento(curso3)

    cursos.crearArchivo("cursos") 

    curso1.crearArchivo("curso1") 

    cursosObject = cursos.crearObjeto(cursos.cargar("cursos"))
    cursoObject = cursos.crearObjeto(curso1.cargar("curso1"))

    print(cursosObject.elementos[0].nombre)
