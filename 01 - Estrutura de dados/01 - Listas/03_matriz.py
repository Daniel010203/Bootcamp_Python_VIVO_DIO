# Lista aninhada
matriz = [
    [1, "a", 2], # Primeira linha(linha 0), linha -3
    ["b", 3, 4], # Segunda linha(linha 1), linha -2
    [6, 5, "c"]  # Terceira linha(linha 2), linha -1
]

print(matriz[0])  # [1, "a", 2] aqui está pegando a linha 0
print(matriz[0][0])  # 1 aqui está pegando o elemento que está na linha 0 e na coluna 0
print(matriz[0][-1])  # 2 aqui está pegando o elemento da linha 0 e da  ultima coluna dela
print(matriz[-1][-1])  # "c" aqui esta pegando o elemento da ultima linha e da ultima coluna
print(matriz[-2][-2])  # 3 aqui esta pegando o elemento da linha 1 ( linha -2) e a coluna 1 (coluna -2)