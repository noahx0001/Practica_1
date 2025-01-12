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
        if self.isObject:
            return f"Matricula: {self.matricula}, Nombre: {self.nombre}, Apellido Paterno: {self.apPaterno}, Apellido Materno: {self.apMaterno}, Correo: {self.correo}"
        elif hasattr(self, "elementos"):
            return "\n".join([str(estudiante) for estudiante in self.elementos])
        else:
            return "No hay estudiantes disponibles"
        
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

    print(estudiantes)





