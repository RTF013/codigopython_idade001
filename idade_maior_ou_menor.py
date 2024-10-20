# ESSE CODIGO EU FIZ SOZINHO

def inserir_dados():
    idade = int(input('Digite sua idade: '))
    return idade

def resultado_dados(idade):
    if idade >= 18:
        print('Seja bem vindo, maior de idade!')
    else:
        print('Infelizmente é menor de idade!')

idade_usuario = inserir_dados()
resultado_dados(idade_usuario)








