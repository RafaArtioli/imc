from paciente import Paciente
from diagnostico_imc import Diagnostico_imc

nome = str(input('Digite o nome do paciente: '))
idade = int(input('Digite a idade do paciente: '))
peso = float(input('Digite o peso do paciente: '))
altura = float(input('Digite a altura do paciente: '))

paciente = Paciente(nome, idade, altura, peso)
imc_paciente = paciente.imc()

diagnostico_imc = Diagnostico_imc(paciente.get_imc)
diagnostico_imc = diagnostico_imc.diagnostico_imc()

paciente.set_diagnostico_imc(diagnostico_imc)

#print(paciente)

