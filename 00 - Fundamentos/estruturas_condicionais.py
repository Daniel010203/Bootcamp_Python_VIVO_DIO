#VARIAVEIS
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Informe sua idade: "))

#Usando somente o IF
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE :
    print("Menor de idade, não pode tirar a CNH.")
    
#Usando IF e o ELSE
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else :
    print("Menor de idade, não pode tirar a CNH.")

#USANDO IF, ELIF e ELSE
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não as Praticas.")
else :
    print("Menor de idade, não pode tirar a CNH.")