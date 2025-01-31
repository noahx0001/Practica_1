from lista import Lista
import json

class Estudiante(Lista):
    def __init__(self, matricula=None, nombre=None, apPaterno=None, apMaterno=None, correo=None):
        self.isObject = matricula and nombre and apPaterno and apMaterno and correo
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
            estudianteDict = dict(
                matricula=self.matricula,
                nombre=self.nombre,
                apPaterno=self.apPaterno,
                apMaterno=self.apMaterno,
                correo=self.correo
            )
            return estudianteDict
        elif hasattr(self, "elementos"):
            estudiantes = []
            for estudiante in self.elementos:
                estudianteDict = estudiante.conversion()
                estudiantes.append(estudianteDict)
            return estudiantes
        else:
            return None

    def crearObjeto(self, myjson):
        if isinstance(myjson, dict):
            return Estudiante(
                myjson["matricula"],
                myjson["nombre"],
                myjson["apPaterno"],
                myjson["apMaterno"],
                myjson["correo"]
            )
        elif isinstance(myjson, list):
            self.elementos = []
            for v in myjson:
                self.agregar_elemento(self.crearObjeto(v))
            return self
        else:
            return None

    def cargarJson(self, nombreArchivo):
        with open(nombreArchivo + ".json", "r") as file:
            myjson = json.load(file)
        return self.crearObjeto(myjson)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    estudiantes = Estudiante()
    estudiantes.cargarJson("estudiantes")
    estudiantes.crearArchivo("estudiantes")

    print(estudiantes)