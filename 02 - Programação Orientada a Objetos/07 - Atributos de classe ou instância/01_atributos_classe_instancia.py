class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

# Explicação do código

'''
Este código define uma classe chamada `Estudante` e a utiliza para criar objetos que representam estudantes. Vamos analisar passo a passo:

**1. Definindo a Classe `Estudante`**

```python
class Estudante:
    escola = "DIO"
```

* **`class Estudante:`**: Esta linha define uma nova classe chamada `Estudante`. Classes são como blueprints para criar objetos.
* **`escola = "DIO"`**: Esta linha define um atributo de classe chamado `escola`. Atributos de classe são compartilhados por todos os objetos da classe. Neste caso, todos os estudantes inicialmente pertencem à escola "DIO".

**2. Método Construtor `__init__`**

```python
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
```

* **`def __init__(self, nome, matricula):`**: Este é o método construtor. Ele é chamado automaticamente quando um novo objeto `Estudante` é criado.
* **`self`**:  É uma referência ao objeto atual sendo criado.
* **`nome` e `matricula`**: São parâmetros que recebem o nome e a matrícula do estudante.
* **`self.nome = nome` e `self.matricula = matricula`**: Estas linhas atribuem os valores recebidos aos atributos do objeto. `self.nome` e `self.matricula` são atributos de instância, únicos para cada objeto `Estudante`.

**3. Método `__str__`**

```python
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
```

* **`def __str__(self) -> str:`**: Este método é chamado quando o objeto `Estudante` é convertido para uma string (por exemplo, ao usar `print(aluno_1)`).
* **`return f"{self.nome} - {self.matricula} - {self.escola}"`**: Retorna uma string formatada com o nome, matrícula e escola do estudante.

**4. Função `mostrar_valores`**

```python
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
```

* **`def mostrar_valores(*objs):`**: Define uma função que recebe um número variável de argumentos (usando `*objs`).
* **`for obj in objs:`**: Itera sobre os argumentos recebidos.
* **`print(obj)`**: Imprime cada objeto na tela.

**5. Criando Objetos `Estudante`**

```python
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
```

* Estas linhas criam dois objetos `Estudante`, um chamado `aluno_1` com nome "Guilherme" e matrícula 1, e outro chamado `aluno_2` com nome "Giovanna" e matrícula 2.

**6. Usando a Função `mostrar_valores`**

```python
mostrar_valores(aluno_1, aluno_2)
```

* Esta linha chama a função `mostrar_valores` passando os objetos `aluno_1` e `aluno_2` como argumentos. O método `__str__` é chamado para cada objeto, e a saída será:
    * Guilherme - 1 - DIO
    * Giovanna - 2 - DIO

**7. Modificando o Atributo de Classe `escola`**

```python
Estudante.escola = "Python"
```

* Esta linha altera o atributo de classe `escola` para "Python". Agora, todos os novos objetos `Estudante` serão criados com esta escola.

**8. Criando um Novo Objeto `Estudante`**

```python
aluno_3 = Estudante("Chappie", 3)
```

* Esta linha cria um novo objeto `Estudante` chamado `aluno_3`, com nome "Chappie" e matrícula 3. 

**9. Usando `mostrar_valores` Novamente**

```python
mostrar_valores(aluno_1, aluno_2, aluno_3)
```

* Esta linha imprime os três objetos. A saída será:
    * Guilherme - 1 - DIO
    * Giovanna - 2 - DIO
    * Chappie - 3 - Python

**Observações:**

* Os objetos `aluno_1` e `aluno_2` foram criados antes da mudança do atributo de classe `escola`, por isso eles ainda mantêm a escola "DIO".
* O objeto `aluno_3` foi criado após a mudança, então ele tem a escola "Python".

Este exemplo demonstra a diferença entre atributos de classe e atributos de instância, bem como como os métodos especiais `__init__` e `__str__` facilitam a criação e representação de objetos em Python.
'''