class Diagnostico_imc:

    def __init__(self, imc):
        self.imc = imc

    def diagnostico_imc(self):
        if self.imc < 18.5:
            return 'O paciente está ABAIXO DO PESO!'
        elif self.imc >= 18.5 and self.imc <= 25:
            return 'O paciente está no PESO IDEAL!'
        elif self.imc >= 25 and self.imc <= 30:
            return 'O paciente está SOBREPESO!'
        elif self.imc >= 30 and self.imc <= 35:
            return 'O paciente está OBESIDADE GRAU I'
        elif self.imc >= 35 and self.imc <= 40:
            return 'O paciente esta OBESIDADE GRAU II ( SEVERA )'
        else:
            return 'O paciente esta OBESIDADE GRAU III ( MÓRBIDA )'


