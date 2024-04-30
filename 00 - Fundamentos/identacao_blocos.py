def sacar(valor):
    saldo = 500

    if saldo >= valor:
       print("Valor sacado!")
       print("Retire seu dinheiro na boca do caixa.")
    else:

       print("Saldo insuficiente")


    print("Obrigado por ser nosso Cliente, tenha um bom dia")   

def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)