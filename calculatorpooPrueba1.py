class Calculadora():
    def __init__(self):
        self.resultado = 0
        self.valor1 = 0
        self.valor2 = 0 
    
    def sumar(self):
        self.resultado = self.valor1 + self.valor2
    
    def restar(self):
        self.resultado = self.valor1 - self.valor2

    def multiplicar(self):
        self.resultado = self.valor1 * self.valor2

    def dividir(self):
        self.resultado = self.valor1 / self.valor2
    
    def mostrarResultado(self):
        return self.resultado

cal = Calculadora()
cal.valor1 = int(input('Ingrese un entero: '))
cal.valor2 = int(input('Ingrese un entero: '))
cal.sumar()
print(str(cal.valor1) + "+" + str(cal.valor2) + "=" + str(cal.mostrarResultado))