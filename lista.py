import json
class Lista:
    def __init__(self):
        self.elementos = [] 

    def __str__(self):
        return "\n".join([str(elemento) for elemento in self.elementos])

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def obtener_elementos(self):
        return self.elementos

    def eliminar_elemento(self, elemento):
        self.elementos.pop(elemento - 1)

    def buscar_elemento(self, elemento):
        return elemento in self.elementos
    
    def actualizar_elemento(self, elemento, nuevo_elemento):
        self.elementos[elemento - 1] = nuevo_elemento

    def crearArchivo(self, nombreArchivo):
        f = open(nombreArchivo+".json", "w")
        f.write(json.dumps(self.conversion(), indent=4))
        f.close()