class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())


# Explicação sobre encapsulamento em python
'''
Em Python, o encapsulamento é um princípio fundamental da programação orientada a objetos (POO) que visa proteger os dados internos de uma classe e controlar o acesso a eles.  Ele promove a organização, segurança e manutenibilidade do código. 

**Conceitos-chave:**

* **Atributos Privados:** Atributos declarados com um sublinhado (`_`) como prefixo (por exemplo, `_saldo`). Embora tecnicamente acessíveis, eles sinalizam que devem ser usados internamente pela classe e não diretamente por outros códigos.

* **Métodos de Acesso:** Métodos especiais chamados de *getters* e *setters* são usados para controlar como os atributos são acessados e modificados.
    * **Getter:** Um método que retorna o valor de um atributo privado.
    * **Setter:** Um método que modifica o valor de um atributo privado, aplicando possíveis validações ou regras.

**Exemplo:**

```python
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo  # Atributo privado
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor  # Modifica o atributo privado internamente

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente!")

    def get_saldo(self):  # Getter
        return self._saldo

    def set_saldo(self, novo_saldo):  # Setter
        if novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("Saldo inválido!")

conta = Conta("0001", 100)
conta.depositar(50)

# Acesso ao saldo usando o getter
print(conta.get_saldo())  # Saída: 150

# Tentativa de modificar o saldo diretamente (não recomendado)
# conta._saldo = -100  # Isso é possível, mas viola o encapsulamento

# Modificando o saldo usando o setter
conta.set_saldo(200)
print(conta.get_saldo())  # Saída: 200
```

**Benefícios do Encapsulamento:**

* **Segurança:** Impede que outros códigos modifiquem os dados internos da classe de forma inesperada.
* **Manutenibilidade:** Facilita a modificação da estrutura interna da classe sem afetar o código que usa a classe.
* **Modularidade:** Permite que a classe seja reutilizada em outros projetos sem se preocupar com conflitos entre os atributos internos e o código externo.
* **Abstração:** Esconde os detalhes de implementação da classe, permitindo que outros códigos se concentrem na funcionalidade da classe.

**Observações:**

* Em Python, o encapsulamento é mais uma convenção do que uma regra.  Atributos privados podem ser acessados diretamente, mas isso é geralmente considerado uma má prática.
* O encapsulamento em Python é menos rígido do que em linguagens como Java ou C++. 
* O uso de getters e setters é opcional, mas é considerado uma boa prática para controlar o acesso aos atributos da classe.

Espero que esta explicação tenha sido útil! 
'''
