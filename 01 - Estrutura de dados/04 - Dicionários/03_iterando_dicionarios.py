'''
Este código demonstra duas maneiras diferentes de iterar e exibir os dados armazenados no dicionário contatos.
Parte 1: Iterando pelas chaves

for chave in contatos:
    print(chave, contatos[chave])

for chave in contatos:: Esta linha inicia um loop for. A variável chave assume, a cada iteração, o valor de uma chave do dicionário contatos.
print(chave, contatos[chave]): Dentro do loop, esta linha imprime a chave atual (chave) e o valor correspondente a essa chave no dicionário (contatos[chave]). O valor, neste caso, é outro dicionário contendo o nome e telefone da pessoa.
Parte 2: Iterando por chave e valor simultaneamente
print("=" * 100)
for chave, valor in contatos.items():
    print(chave, valor)

print("=" * 100): Esta linha imprime uma linha divisória de sinais de igual para separar visualmente as duas partes do código.
for chave, valor in contatos.items(): Este loop utiliza o método .items() do dicionário, que retorna uma lista de tuplas, onde cada tupla contém a chave e o valor correspondente.
print(chave, valor): Similar ao primeiro loop, esta linha imprime a chave e o valor, mas desta vez obtidos diretamente da tupla (chave, valor) gerada por contatos.items().
Em resumo:
O código demonstra duas formas de percorrer um dicionário em Python:
Iterando somente pelas chaves e acessando os valores dentro do loop.
Iterando simultaneamente por chave e valor usando o método .items().
Ambas as abordagens produzem o mesmo resultado: exibir o email (chave) e as informações de contato (nome e telefone, contidos no valor) de cada pessoa armazenada no dicionário contatos.
'''


contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)
