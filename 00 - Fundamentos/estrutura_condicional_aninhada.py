conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 2500
cheque_especial = 450


if conta_normal:

    if saldo >= saque:
     print("Saque realizado com sucesso.")
    elif saque <= (saldo+ cheque_especial):
     print("Saque realizado com uso do cheque especial.")
    else:
      print("Não foi possivel efetuar o saque, saldo insuficiente.")

elif conta_universitaria:
   
   if saldo >= saque:
     print("Saque realizado com sucesso.")
   else:
     print("Saldo insuficiente")

elif conta_especial:
  
  print("Conta especial Selecionada")
else:
  print("Sistema não reconheceu tipo de conta, entre em contato com o gerente!")


