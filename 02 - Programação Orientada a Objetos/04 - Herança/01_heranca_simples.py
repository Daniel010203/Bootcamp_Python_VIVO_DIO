class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)

# Explicação do código

''' Este código define uma hierarquia de classes para representar veículos, usando o conceito de herança em Python. Vamos analisar passo a passo:
1. Classe Base Veiculo:
__init__(self, cor, placa, numero_rodas):
O método construtor da classe Veiculo, responsável por inicializar os atributos de um objeto Veiculo.
Recebe os parâmetros cor, placa e numero_rodas e os atribui aos atributos do objeto (self.cor, self.placa, self.numero_rodas).
ligar_motor(self):
Imprime a mensagem "Ligando o motor".
__str__(self):
Método especial que define a representação em string de um objeto Veiculo.
Retorna uma string formatada que inclui o nome da classe e os valores de todos os atributos do objeto.
2. Classes Filhas Motocicleta, Carro e Caminhao:
Motocicleta(Veiculo):
Herda da classe Veiculo, mas não adiciona nenhum atributo ou método próprio. Isso significa que uma Motocicleta tem as mesmas características básicas de um Veiculo.
Carro(Veiculo):
Semelhante à Motocicleta, herda de Veiculo e não possui atributos ou métodos próprios.
Caminhao(Veiculo):
Herda de Veiculo e adiciona o atributo carregado no construtor.
Sobrescreve o método __init__ para receber o parâmetro adicional carregado e inicializar o atributo correspondente.
Define o método esta_carregado(self) para imprimir se o caminhão está ou não carregado.
3. Criação de Objetos:
moto = Motocicleta("preta", "abc-1234", 2):
Cria um objeto moto da classe Motocicleta, definindo sua cor, placa e número de rodas.
carro = Carro("branco", "xde-0098", 4):
Cria um objeto carro da classe Carro com seus atributos correspondentes.
caminhao = Caminhao("roxo", "gfd-8712", 8, True):
Cria um objeto caminhao da classe Caminhao com seus atributos, incluindo o estado de carregamento (True).
4. Saída:
print(moto): Imprime a representação em string do objeto moto, mostrando seu tipo, cor, placa e número de rodas.
print(carro): Imprime a representação em string do objeto carro.
print(caminhao): Imprime a representação em string do objeto caminhao, incluindo o estado de carregamento.
Em resumo, o código demonstra a utilização de classes e herança para modelar diferentes tipos de veículos com características específicas.
Pontos importantes:
Herança: permite reutilizar código e criar classes mais específicas com base em uma classe base.
Sobrescrita: possibilita modificar o comportamento de um método herdado (ex: __init__ da classe Caminhao).
Polimorfismo: a função print(moto), print(carro) e print(caminhao) chama o mesmo método __str__, mas o comportamento é adaptado para cada classe.
'''