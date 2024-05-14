'''Comentários e Explicação do Código:
O código define uma função que imprime um poema formatado com data, versos e metadados. Vamos analisar cada parte:'''

#1. Definição da função:

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


# def exibir_poema(data_extenso, *args, **kwargs):: Define uma função chamada exibir_poema que recebe três tipos de argumentos:
# data_extenso: Um argumento obrigatório que representa a data do poema em formato extenso.
# *args: Uma quantidade variável de argumentos posicionais que representam os versos do poema.
# **kwargs: Uma quantidade variável de argumentos nomeados (keyword arguments) que representam os metadados do poema, como autor, ano, etc.
# texto = "\n".join(args): Cria uma string texto concatenando os versos do poema (passados como *args) com quebras de linha ("\n").
# meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]): Cria uma string meta_dados formatada com os metadados do poema. Utiliza list comprehension para iterar sobre os pares chave-valor em kwargs.items(), formatando cada chave com a primeira letra maiúscula (chave.title()) e concatenando com o valor, separados por ": ". Os pares chave-valor são unidos por quebras de linha.
# mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}": Formata a mensagem final do poema, incluindo a data, os versos e os metadados, separados por duas quebras de linha.
# print(mensagem): Imprime a mensagem formatada na tela.

# 2. Chamada da Função:

exibir_poema(
    "Sexta-feira, 26 de agosto 2022",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)



'''Chama a função exibir_poema passando:
"Zen of Python" como argumento data_extenso.
Os versos do poema como argumentos posicionais (*args).
autor="Tim Peters" e ano=1999 como argumentos nomeados (**kwargs).'''


# 3. Saída:

'''A saída do código será o poema formatado, incluindo a data, os versos e os metadados:
Sexta-feira, 26 de agosto 2022

Zen of Python

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

Autor: Tim Peters
Ano: 1999
Use code with caution.
Em resumo:
Este código demonstra o uso de argumentos posicionais (*args) e nomeados (**kwargs) em funções Python para criar uma função flexível que pode imprimir poemas com diferentes quantidades de versos e metadados. Ele também ilustra o uso de list comprehension e f-strings para formatação eficiente de strings.'''
