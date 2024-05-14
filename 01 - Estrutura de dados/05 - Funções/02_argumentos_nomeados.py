'''Comentários e Explicação do Código:
O código define uma função que simula o salvamento de informações de um carro em um banco de dados e demonstra três maneiras diferentes de chamar essa função, passando os argumentos.'''

#1. Definição da Função:

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

'''def salvar_carro(marca, modelo, ano, placa):: Define uma função chamada salvar_carro que recebe quatro argumentos: marca, modelo, ano e placa.
salva carro no banco de dados...: É um comentário que indica que, em um cenário real, essa função realizaria a inserção dos dados do carro em um banco de dados.
print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}"): Imprime uma mensagem de sucesso formatada com os dados do carro, utilizando f-string para inserir as variáveis na string.'''

#2. Chamadas da Função:

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})


'''salvar_carro("Fiat", "Palio", 1999, "ABC-1234"): Chama a função passando os argumentos na ordem em que foram definidos na função (posicional).
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234"): Chama a função passando os argumentos com seus respectivos nomes (keyword arguments). Isso torna a chamada mais legível e independente da ordem dos argumentos.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}): Chama a função utilizando um dicionário que contém os nomes dos argumentos como chaves e seus valores. O operador ** desempacota o dicionário, passando os valores como argumentos nomeados para a função.'''

#3. Saída:

'''A saída do código, em todos os casos, será:
Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234
Use code with caution.
Em resumo:
Este código demonstra diferentes maneiras de chamar uma função em Python, passando argumentos posicionais, nomeados (keyword arguments) ou desempacotando um dicionário. A escolha da forma de chamar a função depende do contexto e da legibilidade desejada.'''