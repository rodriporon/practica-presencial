
class Operacion:

    def __init__(self, a, b, resultado):
        self.a = a
        self.b = b
        self.resultado = resultado

    def getA(self):
        return self.a
    
    def getB(self):
        return self.b

    def getResultado(self):
        return self.resultado

    def setA(self, a):
        self.a = a
    
    def setB(self, b):
        self.b = b

    def setResultado(self, resultado):
        self.resultado = resultado