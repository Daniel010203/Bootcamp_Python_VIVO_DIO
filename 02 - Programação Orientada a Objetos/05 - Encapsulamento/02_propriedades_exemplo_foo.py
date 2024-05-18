class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)

# Explicação encapsulamento usando property decorators
'''

Este código demonstra uma maneira interessante de implementar encapsulamento em Python usando *property decorators* (decoradores de propriedade). Vamos analisar cada parte do código:

**1. Classe `Foo`**

   - **`__init__(self, x=None)`:**  O construtor da classe `Foo`. Ele inicializa um atributo privado `_x` com o valor passado para `x` na criação da instância. Se nenhum valor for passado, `_x` recebe `None`.

   - **`@property`  `def x(self):`:**  Esta é a parte que define o *getter* para o atributo `x`. O decorador `@property` transforma o método `x` em uma propriedade, tornando seu acesso semelhante ao de um atributo normal. 
      - Quando `foo.x` é chamado, o método `x` é executado e retorna o valor de `self._x`. Se `_x` for `None`, ele retorna 0.

   - **`@x.setter`  `def x(self, value):`:** Este é o *setter* para o atributo `x`.  Quando você tenta atribuir um valor a `foo.x`, este método é executado.
      - Ele adiciona o valor passado (`value`) ao atributo `_x`.

   - **`@x.deleter`  `def x(self):`:** Este é o *deleter* para o atributo `x`. Quando você utiliza `del foo.x`, este método é executado.
      - Ele redefine o valor de `_x` para 0.

**2. Execução do Código**

   - **`foo = Foo(10)`:**  Cria uma instância da classe `Foo` chamada `foo`, inicializando `_x` com 10.

   - **`print(foo.x)`:**  Imprime o valor de `foo.x`, que é 10 (retornado pelo *getter*).

   - **`del foo.x`:**  Deleta o atributo `x` da instância `foo`. Isso chama o *deleter*, definindo `_x` para 0.

   - **`print(foo.x)`:** Imprime o valor de `foo.x`, que agora é 0.

   - **`foo.x = 10`:**  Atribui o valor 10 a `foo.x`. Isso chama o *setter*, que adiciona 10 ao valor atual de `_x`, resultando em `_x = 10`.

   - **`print(foo.x)`:** Imprime o valor de `foo.x`, que agora é 10 (retornado pelo *getter*).

**Por que usar *property decorators*?**

- **Encapsulamento:** O uso de *property decorators* torna o acesso ao atributo `x` mais controlado. O código que usa a classe `Foo` não precisa saber que o atributo real é `_x` e como ele é manipulado.
- **Flexibilidade:** Você pode adicionar lógica adicional nos *getters*, *setters* e *deleters* para validar dados, realizar cálculos ou controlar o acesso.
- **Legibilidade:**  O código fica mais limpo e fácil de entender porque o acesso ao atributo `x` se comporta como um atributo normal.

Este exemplo ilustra uma implementação comum e eficiente de encapsulamento em Python. Ele demonstra como *property decorators* podem ser usados para criar getters, setters e deleters, garantindo um controle preciso sobre o acesso aos dados dentro da classe.

'''