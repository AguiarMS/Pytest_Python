class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b
    
    def eh_par(self, num):
        return num % 2 == 0
    
    def fatorial(self, n):
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n == 0:
            return 1
        return n * self.fatorial(n - 1)