# coleta de informação
def coleta_informacao():

    peso = int(input("Digite seu peso :"))
    altura = float(input("Digite sua altura :"))
    return peso,altura

# calculo imc
def calculo_imc(peso,altura):
    imc = peso/(altura*altura) 
    return imc

informacoes = coleta_informacao()

peso = informacoes[0]
altura = informacoes[1]

print(calculo_imc(peso,altura))


