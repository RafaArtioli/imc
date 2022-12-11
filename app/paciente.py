class Paciente:

    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.diagnostico_imc = "Sem Diagnóstico"
       

    def imc(self):
        self.imc = self.peso / (self.altura * self.altura)
        
        
    @property
    def get_imc(self):
        return self.imc
     
    def set_diagnostico_imc(self, diagnostico_imc):
        self.diagnostico_imc = diagnostico_imc

    def __str__(self):
        return f'Paciente com o nome {self.nome}, idade {self.idade} anos, tem o IMC de {self.imc:.2f} {self.diagnostico_imc}.'


    