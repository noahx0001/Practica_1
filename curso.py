
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
            self.elementos = []
            for v in myjson:
                self.agregar_elemento(self.crearObjeto(v))    
            return self.elementos
        else:
            return None
    def cargarJson(self, nombreArchivo):
        myjson = json.load(open(nombreArchivo+".json"))
        return self.crearObjeto(myjson)
    def __repr__(self):
        return str(self.conversion())
        
if __name__ == "__main__":
    """
    curso1 = Curso("Programacion", "Curso de Python", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso2 = Curso("Matematica", "Curso de Calculo", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso3 = Curso("Fisica", "Curso de Fisica", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso4 = Curso("Quimica", "Curso de Quimica", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso5 = Curso("Biologia", "Curso de Biologia", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    """
    """
    cursos.agregar_elemento(curso1)
    cursos.agregar_elemento(curso2)
    cursos.agregar_elemento(curso3)
    cursos.agregar_elemento(curso4)
    cursos.agregar_elemento(curso5)

    cursos.crearArchivo("cursos") 

    curso1.crearArchivo("curso1") 

    cursos.crearObjeto(cursos.leerJson("cursos"))

    print(cursos)
    """

    cursos= Curso()

    cursos.cargarJson("cursos")

    cursos.crearArchivo("cursos")

    print(cursos)
