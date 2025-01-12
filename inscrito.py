
from estudiante import Estudiante
from curso import Curso
from lista import Lista
from datetime import datetime

class Inscrito(Lista):
    def __init__(self,estudiante=None, curso=None, fechaInscripcion=None):
        self.isObject=estudiante and curso and fechaInscripcion
        if self.isObject:
            self.estudiante = estudiante
            self.curso = curso
            self.fechaInscripcion = fechaInscripcion
        else:
            super().__init__()

    def __str__(self):
         if self.isObject:
            return f"Estudiante: {self.estudiante}, Curso: {self.curso}, Fecha de Inscripcion: {self.fechaInscripcion}"
         elif hasattr(self, "elementos"):
            return "\n".join([str(inscrito) for inscrito in self.elementos])
         else:
            return "No hay inscritos disponibles"
    
if __name__ == "__main__":
        estudiante1 = Estudiante(123, "Juan", "Perez", "Gomez", "cBp7o@example.com")
        curso1 = Curso("Programacion", "Curso de Python", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
        curso2= Curso("Matematica", "Curso de Calculo", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
        curso3 = Curso("Fisica", "Curso de Fisica", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
        inscrito1 = Inscrito(estudiante1, curso1, datetime.now())
        inscrito2 = Inscrito(estudiante1, curso2, datetime.now())
        inscrito3 = Inscrito(estudiante1, curso3, datetime.now())

        print(inscrito1)

        inscritos=Inscrito();

        inscritos.agregar_elemento(inscrito1)

        print(inscritos)