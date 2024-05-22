class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

# Exlicação do código

'''
O código define uma classe chamada `Pessoa` e demonstra o uso de métodos de classe e métodos estáticos. Vamos analisar passo a passo:

**1. Classe `Pessoa`**

```python
class Pessoa:
```

* Define uma nova classe chamada `Pessoa` para representar objetos do tipo pessoa.

**2. Método Construtor `__init__`**

```python
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

* O método `__init__` é o construtor da classe. Ele é chamado automaticamente quando um novo objeto `Pessoa` é criado. 
* `self` é uma referência ao objeto atual sendo criado.
* `nome` e `idade` são parâmetros que recebem o nome e a idade da pessoa.
* `self.nome = nome` e `self.idade = idade` atribuem os valores recebidos aos atributos `nome` e `idade` do objeto.

**3. Método de Classe `criar_de_data_nascimento`**

```python
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
```

* `@classmethod`: Um decorador que indica que este é um método de classe. Métodos de classe são chamados na classe em si (ex: `Pessoa.criar_de_data_nascimento(...)`) e recebem a classe como primeiro argumento (`cls`).
* `cls` é uma referência à classe `Pessoa`. 
* `criar_de_data_nascimento`:  O método recebe o ano, mês, dia e nome da pessoa. Ele calcula a idade com base no ano de nascimento e retorna um novo objeto `Pessoa` usando o construtor da classe. 

**4. Método Estático `e_maior_idade`**

```python
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
```

* `@staticmethod`: Um decorador que indica que este é um método estático. Métodos estáticos não recebem a classe (`cls`) nem o objeto (`self`) como argumentos.
* `e_maior_idade`: O método recebe uma idade e retorna `True` se a idade for maior ou igual a 18, indicando que a pessoa é maior de idade, e `False` caso contrário.

**5. Criando um Objeto `Pessoa`**

```python
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
```

* Esta linha cria um novo objeto `Pessoa` chamado `p` usando o método de classe `criar_de_data_nascimento`. 
* Note que o método é chamado na classe `Pessoa` em vez de um objeto.

**6. Imprimindo os Atributos**

```python
print(p.nome, p.idade)
```

* Imprime o nome e a idade do objeto `p`.

**7. Usando o Método Estático `e_maior_idade`**

```python
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
```

* Chama o método estático `e_maior_idade` diretamente na classe `Pessoa` para verificar se as idades 18 e 8 são maiores que 18.

**Em resumo:**

* O código demonstra como métodos de classe e métodos estáticos podem ser usados para criar objetos e realizar operações relacionadas à classe sem a necessidade de criar um objeto.
* Métodos de classe são úteis para criar objetos de maneira mais organizada, enquanto métodos estáticos são úteis para funções que não dependem do estado de um objeto.
'''