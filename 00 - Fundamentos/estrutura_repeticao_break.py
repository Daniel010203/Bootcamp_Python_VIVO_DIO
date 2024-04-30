while True : # Loop infinito
    numero = int(input("Informe um número: "))

    if numero == 10:
       break # Para a execução do loop prematuramente

    if numero %2 == 0:
        continue # Continuar com o próximo item da sequência sem executar o resto do bloco de código para aquela iteração específica

    print(f"{numero} é um número impar!")