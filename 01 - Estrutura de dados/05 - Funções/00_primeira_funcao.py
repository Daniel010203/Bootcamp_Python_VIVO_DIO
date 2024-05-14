'''Comentários e Explicação do Código:
O código define três funções que imprimem mensagens na tela e depois as chama para demonstrar seu funcionamento. Vamos analisar cada parte:'''

#1. Definição das funções:


def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


'''def exibir_mensagem():: Define uma função chamada exibir_mensagem que não recebe nenhum argumento (parâmetro). Ela simplesmente imprime a mensagem "Olá mundo!".
def exibir_mensagem_2(nome):: Define a função exibir_mensagem_2 que recebe um argumento chamado nome. Ela utiliza f-string para formatar a mensagem e incluir o valor do argumento nome na saudação.
def exibir_mensagem_3(nome="Anônimo"):: Define a função exibir_mensagem_3 que recebe um argumento nome com um valor padrão "Anônimo". Isso significa que, se nenhum valor for fornecido para nome ao chamar a função, ela usará "Anônimo" como padrão. A função também usa f-string para formatar a mensagem.
'''

#2. Chamadas das funções:

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

'''
exibir_mensagem(): Chama a função exibir_mensagem sem nenhum argumento.
exibir_mensagem_2(nome="Guilherme"): Chama a função exibir_mensagem_2, passando o argumento nome com o valor "Guilherme".
exibir_mensagem_3(): Chama a função exibir_mensagem_3 sem passar nenhum argumento, utilizando o valor padrão "Anônimo" para nome.
exibir_mensagem_3(nome="Chappie"): Chama a função exibir_mensagem_3, passando o argumento nome com o valor "Chappie".'''

#3. Saída:

'''Ao executar esse código, a saída será:
Olá mundo!
Seja bem vindo Guilherme!
Seja bem vindo Anônimo!
Seja bem vindo Chappie!
Use code with caution.
Em resumo:
Este código demonstra a criação e utilização de funções em Python, mostrando como passar argumentos para funções e como definir valores padrão para esses argumentos. Ele também ilustra o uso de f-strings para formatar strings de forma eficiente.'''


