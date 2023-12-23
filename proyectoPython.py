
class Nodo:
    def __init__(self):
        self.valor = 0
    pass

    def __str__(self):
        return f"{self.valor} valores"

class Arista:
    def __init__(self):
        self.inico = ""
        self.final = ""

    def puntasDelNodo(self,inicio,final):
        self.inico = inicio
        self.final = final
        print(self.inico, self.final," puntas")
class Grafo:

    def __init__(self):
        self.nodos = Nodo()
        self.aristas = Arista()

        print("wenas")

    def guardarNodos(self, nodos):
        self.nodos = nodos
        print(self.nodos[0])
        print(nodos.__str__())
    def guardarAristas(self, aristas):
        self.aristas = aristas
        print(self.aristas)


opc = "y"
grafo = Grafo()
nodos = []
aristas = []
tupla = []
#Bucle menú
while True:
    arr = []
    if opc == 'y' or opc == 'Y':
        entrada = input("Ingrese un nodo y sus vecinos\nejemplo: A B C\nlos vecnios de A son B y C\n").split()
        for j in entrada:
            arr.append(j)
        nodos.append(arr[0])
        aristas.append(arr)

    elif opc == 'n' or opc == 'N':
        if not nodos in aristas:
            print("error")
        print(aristas, " aristas")
        for j in aristas:
            print(j, " j", len(j))
            k = 0
            if len(j) == 1:
                tupla.append([j[0],None])
            else:
                for i in range(1, len(j)):
                    tupla.append([j[0], j[i]])
        print(tupla)
        grafo.guardarNodos(nodos)
        grafo.guardarAristas(tupla)
        break
    else:
        print("ingrese una opción correcta")
    opc = str(input("¿Desea continuar? y/n: "))
