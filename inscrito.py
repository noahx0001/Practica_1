
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
        return self.conversion()
    def conversion(self):
         if self.isObject:
            inscritoDictEstudiante = dict(matricula=self.estudiante.matricula, nombre=self.estudiante.nombre, apPaterno=self.estudiante.apPaterno, apMaterno=self.estudiante.apMaterno, correo=self.estudiante.correo)  
            inscritoDictCurso = dict(nombre=self.curso.nombre, descripcion=self.curso.descripcion, fechaInicio=self.curso.fechaInicio, fechaFin=self.curso.fechaFin, modalidad=self.curso.modalidad)
            inscritoDict = dict(estudiante=inscritoDictEstudiante, curso=inscritoDictCurso, fechaInscripcion=self.fechaInscripcion)
            return str(inscritoDict)
         elif hasattr(self, "elementos"):
            inscritos = []
            for inscrito in self.elementos:
                inscritoDict = inscrito.conversion()
                inscritos.append(inscritoDict)
            return str(inscritos)
         else:
            return "No hay inscritos disponibles"
    
if __name__ == "__main__":
        estudiante1 = Estudiante(123, "Juan", "Perez", "Gomez", "cBp7o@example.com")
        estudiante2 = Estudiante(456, "Pedro", "Lopez", "Garcia", "2r4y6@example.com")
        curso1 = Curso("Programacion", "Curso de Python", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
        curso2= Curso("Matematica", "Curso de Calculo", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
        curso3 = Curso("Fisica", "Curso de Fisica", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
        inscrito1 = Inscrito(estudiante1, curso1, datetime.now())
        inscrito2 = Inscrito(estudiante2, curso2, datetime.now())

        inscritos=Inscrito();

        inscritos.agregar_elemento(inscrito1)
        inscritos.agregar_elemento(inscrito2)

        print(inscritos)

        