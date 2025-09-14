import pytest
from calculadora import Calculadora

class TestCalculadora:
    def setup_method(self):
        """Executado antes de cada teste"""
        self.calc = Calculadora()
    
    # Testes de soma
    def test_soma_positivos(self):
        assert self.calc.soma(2, 3) == 5
    
    def test_soma_resultado_negativo(self):
        # Teste 3: negativo + positivo (resultado negativo)
        resultado = self.calc.soma(0, -1)
        assert resultado < 0
            
    def test_soma_mistos(self):
        assert self.calc.soma(5, -3) == 2
        
    def test_soma_mistos_v2(self):
        assert self.calc.soma(50, -3) == 2
    
    # Testes de subtração
    def test_subtracao(self):
        assert self.calc.subtracao(10, 5) == 5
        assert self.calc.subtracao(5, 10) == -5
    
    # Testes de multiplicação
    def test_multiplicacao(self):
        assert self.calc.multiplicacao(4, 5) == 20
        assert self.calc.multiplicacao(-4, 5) == -20
    
    # Testes de divisão
    def test_divisao_normal(self):
        assert self.calc.divisao(10, 2) == 5
    
    def test_divisao_por_zero(self):
        with pytest.raises(ValueError, match="Não é possível dividir por zero"):
            self.calc.divisao(10, 0)
    
    # Testes de números pares
    def test_eh_par(self):
        assert self.calc.eh_par(4) == True
        assert self.calc.eh_par(7) == False
        assert self.calc.eh_par(0) == True
    
    # Testes de fatorial
    def test_fatorial_positivo(self):
        assert self.calc.fatorial(5) == 120
        assert self.calc.fatorial(0) == 1
    
    def test_fatorial_negativo(self):
        with pytest.raises(ValueError, match="Fatorial não definido para números negativos"):
            self.calc.fatorial(-5)
    
    # Teste com parâmetros (data-driven testing)
    @pytest.mark.parametrize("a, b, esperado", [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
    ])
    def test_soma_parametrizada(self, a, b, esperado):
        assert self.calc.soma(a, b) == esperado