class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())

# Explicação do código
'''
Este código demonstra o conceito de herança em Python, mas também destaca um mau uso de herança através do exemplo do avião. Vamos quebrar o código passo a passo:

**1. Definindo a Classe Pai `Passaro`**

```python
class Passaro:
    def voar(self):
        print("Voando...")
```

* `class Passaro:` define uma classe chamada "Passaro".
* `def voar(self):` define um método chamado "voar" dentro da classe. 
* `self` é uma referência ao objeto da classe.
* `print("Voando...")` imprime a mensagem "Voando..." quando o método `voar` é chamado.

**2. Definindo Classes Filhas que Herdam de `Passaro`**

```python
class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")
```

* `class Pardal(Passaro):` define a classe "Pardal", que herda da classe "Passaro". Isso significa que "Pardal" automaticamente possui todos os métodos de "Passaro".
* `class Avestruz(Passaro):` define a classe "Avestruz", também herdando de "Passaro".
* Ambas as classes "Pardal" e "Avestruz" sobrescrevem o método `voar` da classe pai para fornecer comportamento específico.

**3. Um Mau Uso de Herança: `Aviao`**

```python
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")
```

* `class Aviao(Passaro):` define a classe "Aviao" que herda de "Passaro".
* **Este é o exemplo ruim**: Um avião não é um tipo de pássaro. Herdar de "Passaro" cria uma relação hierárquica que não faz sentido no mundo real. O avião não tem a mesma natureza biológica e funcional de um pássaro.

**4. Função `plano_voo`**

```python
def plano_voo(obj):
    obj.voar()
```

* `def plano_voo(obj):` define uma função chamada "plano_voo" que recebe um objeto como argumento.
* `obj.voar()` chama o método `voar` do objeto passado como argumento.

**5. Usando as Classes**

```python
plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
```

* `plano_voo(Pardal())` cria uma instância da classe "Pardal" e passa essa instância para a função `plano_voo`.
* A função `plano_voo` então chama o método `voar` da instância de "Pardal", imprimindo "Pardal pode voar".
* O mesmo processo ocorre para "Avestruz" e "Aviao", imprimindo seus respectivos comportamentos "voar".

**Em resumo:**

Este código demonstra o conceito de herança em Python, mas o exemplo do avião mostra um mau uso do conceito. A herança é adequada quando existe uma relação "é um" entre as classes (um pardal é um pássaro). No entanto, usar herança para um avião, que não é um pássaro, é inadequado e pode levar a código confuso e difícil de entender.

**Para uma melhor organização do código:**

* É recomendável usar interfaces ou mixins quando se deseja implementar um comportamento comum sem criar uma relação hierárquica "é um" entre classes que não compartilham essa relação.
* As classes "Pardal", "Avestruz" e "Aviao" poderiam ter uma classe base comum (por exemplo, "Voador") que define o método `voar`, e então implementar esse método de forma específica em cada classe.

Espero que essa explicação tenha sido útil.
'''