
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
        if self.isObject:
            return f"Nombre: {self.nombre}, Descripcion: {self.descripcion}, Fecha de Inicio: {self.fechaInicio}, Fecha de Fin: {self.fechaFin}, Modalidad: {self.modalidad} "
        elif hasattr(self, "elementos"):
            return "\n".join([str(curso) for curso in self.elementos])
        else:
            return "No hay cursos disponibles"

# Ejemplo de uso esta se ejecuta cuando yo ejecuto el archivo.
if __name__ == "__main__":
    curso1 = Curso("Programacion", "Curso de Python", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    curso2 = Curso("Matematica", "Curso de Calculo", datetime(2023, 6, 1), datetime(2023, 6, 30), "Presencial")
    cursos= Curso();
    cursos.agregar_elemento(curso1)
    cursos.agregar_elemento(curso2)
    
    print(cursos)


    
