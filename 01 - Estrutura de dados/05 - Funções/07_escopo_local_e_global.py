salario =float(input(f"Digite o valor do salário: \n"))


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_com_bonus = salario_bonus(float(input("Digite o valor do Bonus Mensal: ")))

print(salario_com_bonus)



# Maneira de fazer este código sem usar função escopo global

#def calcular_salario_com_bonus(salario, bonus):
'''Calcula o salário com bônus.
Args:
salario: O salário base.
bonus: O valor do bônus.

Returns:
O salário total com o bônus adicionado.
'''
# return salario + bonus

#salario_base = float(input("Digite o valor do salário: "))
#bonus_mensal = float(input("Digite o valor do bônus mensal: "))

#salario_total = calcular_salario_com_bonus(salario_base, bonus_mensal)

#print(f"O salário total com bônus é: {salario_total:.2f}")



'''Melhorias:
Evitar variáveis globais: O código original utiliza uma variável global salario, o que pode levar a efeitos colaterais e dificultar a manutenção do código. A versão melhorada elimina a necessidade de variáveis globais, passando o salário como argumento para a função.
Nomes mais descritivos: Os nomes das variáveis foram alterados para serem mais descritivos (salario_base, bonus_mensal, salario_total).
Docstring: A função agora inclui uma docstring explicando o que ela faz, quais argumentos recebe e o que retorna.
Tipo de dado: A função input() retorna uma string, então é necessário converter o valor para um tipo numérico (float) antes de realizar cálculos.
Formatação de saída: A saída agora utiliza f-string para formatar o valor do salário com duas casas decimais.
Essas alterações tornam o código mais legível, modular, fácil de entender e manter.'''