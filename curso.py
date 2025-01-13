
from datetime import datetime
from lista import Lista
class Curso(Lista):
    def __init__(self, nombre=None, descripcion=None, fechaInicio=None, fechaFin=None, modalidad=None):

        self.isObject=nombre and descripcion and fechaInicio and fechaFin and modalidad

        if self.isObject:
            self.nombre =  nombre
            self.descripcion = descripcion
            self.fechaInicio = fechaInicio
            self.fechaFin = fechaFin
            self.modalidad = modalidad
        else:
             super().__init__()

    def __str__(self):
        return self.conversion()
    
    def conversion(self):
        if self.isObject:
            cursoDict = dict(nombre=self.nombre, descripcion=self.descripcion, fechaInicio=self.fechaInicio, fechaFin=self.fechaFin, modalidad=self.modalidad)
            return str(cursoDict)
        elif hasattr(self, "elementos"):
            cursos = []
            for curso in self.elementos:
                cursoDict = curso.conversion()
                cursos.append(cursoDict)
            return str(cursos)
        else:
            return "No hay cursos disponibles"

# Ejemplo de uso esta se ejecuta cuando yo ejecuto el archivo.
if __name__ == "__main__":
    curso1 = Curso("Programacion", "Curso de Python", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso2 = Curso("Matematica", "Curso de Calculo", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso3 = Curso("Fisica", "Curso de Fisica", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")

    cursos= Curso();
    cursos.agregar_elemento(curso1)
    cursos.agregar_elemento(curso2)
    cursos.agregar_elemento(curso3)

    print(cursos)


    
