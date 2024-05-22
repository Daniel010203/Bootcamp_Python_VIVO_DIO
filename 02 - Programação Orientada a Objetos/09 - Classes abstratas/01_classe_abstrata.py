from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

# Explicação do código
'''
Este código em Python demonstra o conceito de programação orientada a objetos (POO) utilizando classes abstratas e herança. Vamos analisá-lo passo a passo:

**1. Importações:**

```python
from abc import ABC, abstractmethod, abstractproperty
```

* `ABC`: Define a classe base abstrata.
* `abstractmethod`: Declara métodos abstratos, que devem ser implementados pelas classes filhas.
* `abstractproperty`: Declara propriedades abstratas, que devem ser implementadas pelas classes filhas.

**2. Classe Abstrata `ControleRemoto`:**

```python
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass
```

* Esta classe define o comportamento básico de um controle remoto, mas não implementa as ações específicas.
* `ligar` e `desligar` são métodos abstratos, que devem ser implementados pelas classes filhas.
* `marca` é uma propriedade abstrata, que também deve ser implementada pelas classes filhas.

**3. Classe `ControleTV`:**

```python
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"
```

* Esta classe herda de `ControleRemoto` e implementa os métodos abstratos `ligar`, `desligar` e a propriedade `marca`.
* Ela representa um controle remoto específico para uma TV, com marca "Philco".

**4. Classe `ControleArCondicionado`:**

```python
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"
```

* Similar à `ControleTV`, esta classe herda de `ControleRemoto` e implementa os métodos e a propriedade abstratos.
* Representa um controle remoto para um Ar Condicionado, com marca "LG".

**5. Instâncias e Uso:**

```python
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
```

* Duas instâncias são criadas, uma de `ControleTV` e outra de `ControleArCondicionado`.
* Os métodos `ligar`, `desligar` e a propriedade `marca` são chamados em cada instância, demonstrando o comportamento específico de cada tipo de controle remoto.

**Em resumo:**

* O código define uma estrutura abstrata para um controle remoto, com ações básicas como ligar e desligar, e uma propriedade de marca.
* Classes filhas (ControleTV e ControleArCondicionado) implementam o comportamento específico de cada tipo de controle remoto.
* A herança permite reutilização de código e organização da estrutura, enquanto as classes abstratas garantem que as classes filhas implementem os métodos e propriedades necessários.
'''