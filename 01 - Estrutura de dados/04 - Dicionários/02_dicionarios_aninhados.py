# Analisando o código:
'''
Vamos entender o que cada linha deste código faz:
contatos = { ... }:
Esta linha cria um dicionário chamado contatos.
Dicionários são estruturas de dados que armazenam pares de chave e valor.
Neste caso, as chaves são endereços de email e os valores são outros dicionários contendo o nome e telefone da pessoa correspondente.
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, ...:
Estas linhas dentro do dicionário contatos definem os pares chave-valor.
"guilherme@gmail.com" é a chave, e o valor associado é outro dicionário {"nome": "Guilherme", "telefone": "3333-2221"}.
Este dicionário interno armazena o nome e o telefone de Guilherme.
O mesmo padrão se repete para Giovanna, Chappie e Melaine.
telefone = contatos["giovanna@gmail.com"]["telefone"]:
Aqui, estamos acessando o valor associado à chave "giovanna@gmail.com" dentro do dicionário contatos, que é o dicionário {"nome": "Giovanna", "telefone": "3443-2121"}.
Em seguida, acessamos o valor associado à chave "telefone" dentro deste segundo dicionário, que é "3443-2121".
O valor final, o número de telefone da Giovanna, é então armazenado na variável telefone.
print(telefone):
Finalmente, esta linha imprime o valor da variável telefone, que é o número de telefone da Giovanna: "3443-2121".
Em Resumo:
O código cria um dicionário chamado contatos para armazenar informações de contato (nome e telefone) de diferentes pessoas, usando seus emails como chave de acesso. Em seguida, o código recupera e imprime o número de telefone de Giovanna, acessando o dicionário contatos com a chave "giovanna@gmail.com" e, em seguida, a chave "telefone".
'''

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)


