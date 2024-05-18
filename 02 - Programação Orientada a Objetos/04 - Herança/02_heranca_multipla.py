class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)

# Explicação como funciona o código

'''
O código define uma hierarquia de classes para representar animais, usando conceitos como herança, polimorfismo e multiderivação (herança múltipla). Vamos analisar passo a passo:
1. Classe Base Animal:
__init__(self, nro_patas):
O método construtor recebe o número de patas como parâmetro e o armazena no atributo self.nro_patas.
__str__(self):
Define a representação em string de um objeto Animal, mostrando o nome da classe e os valores de seus atributos.
2. Classes Filhas Mamifero e Ave:
Mamifero(Animal):
Herda da classe Animal e adiciona o atributo cor_pelo.
O construtor recebe a cor_pelo e passa os demais parâmetros para o construtor da classe pai (super().__init__(**kw)) usando um dicionário **kw.
Ave(Animal):
Semelhante a Mamifero, herda de Animal e adiciona o atributo cor_bico.
3. Classes Filhas Gato e Ornitorrinco:
Gato(Mamifero):
Herda da classe Mamifero, não adicionando atributos ou métodos próprios.
Ornitorrinco(Mamifero, Ave):
Herda de ambas as classes Mamifero e Ave, demonstrando herança múltipla.
O construtor recebe todos os atributos (cor_bico, cor_pelo, nro_patas) e os passa para o construtor da classe pai usando super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas). Note que essa forma de chamar super() é específica para herança múltipla.
4. Criação de Objetos:
gato = Gato(nro_patas=4, cor_pelo="Preto"):
Cria um objeto gato da classe Gato, definindo o número de patas e a cor do pelo.
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja"):
Cria um objeto ornitorrinco da classe Ornitorrinco, definindo todas as características.
5. Saída:
print(gato): Imprime a representação em string do objeto gato, mostrando o nome da classe e seus atributos.
print(ornitorrinco): Imprime a representação em string do objeto ornitorrinco, mostrando seus atributos herdados de Mamifero e Ave.
Em resumo, o código demonstra a utilização de herança, polimorfismo e herança múltipla para modelar diferentes tipos de animais, com características específicas.
Pontos importantes:
Herança: permite reutilizar código e criar classes mais específicas com base em uma classe base.
Polimorfismo: a função print(gato) e print(ornitorrinco) chama o mesmo método __str__, mas o comportamento é adaptado para cada classe.
Herança Múltipla: permite que uma classe herde características de múltiplas classes, tornando-a uma combinação de características.
Considerações:
A implementação do Ornitorrinco pode ser um pouco artificial, já que, na vida real, um ornitorrinco não é ao mesmo tempo um mamífero e uma ave. No entanto, este é um exemplo didático para ilustrar a herança múltipla.
O uso de **kw no construtor de Mamifero e Ave permite que classes filhas definam atributos adicionais sem precisar redefinir o construtor completo.
'''