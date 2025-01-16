
from estudiante import Estudiante
from curso import Curso
from lista import Lista
from datetime import datetime

class Inscrito(Lista):
    def __init__(self,estudiantes: list[Estudiante]=None, curso: Curso=None, fechaInscripcion=None):
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
            inscritoDict = dict(estudiantes=self.estudiantes.conversion(), curso=self.curso.conversion(), fechaInscripcion=self.fechaInscripcion)
            return inscritoDict
         elif hasattr(self, "elementos"):
            inscritos = []
            for inscrito in self.elementos:
                inscritoDict = inscrito.conversion()
                inscritos.append(inscritoDict)
            return inscritos
         else:
            return None
    
if __name__ == "__main__":
        estudiante1 = Estudiante(123, "Juan", "Perez", "Gomez", "cBp7o@example.com")
        estudiante2 = Estudiante(456, "Pedro", "Lopez", "Garcia", "2r4y6@example.com")
        estudiante3 = Estudiante(789, "Maria", "Gonzalez", "Gomez", "VXyOa@example.com")

        curso1 = Curso("Programacion", "Curso de Python", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")

        estudiantes=Estudiante();

        estudiantes.agregar_elemento(estudiante1)
        estudiantes.agregar_elemento(estudiante2)
        estudiantes.agregar_elemento(estudiante3)

        inscritos=Inscrito(estudiantes,curso1,datetime(2023, 6, 1))

        print(type(inscritos.estudiantes))
