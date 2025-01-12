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
        self.elementos.remove(elemento)

    def buscar_elemento(self, elemento):
        return elemento in self.elementos
    
    def actualizar_elemento(self, elemento, nuevo_elemento):
        self.eliminar_elemento(elemento)
        self.agregar_elemento(nuevo_elemento)