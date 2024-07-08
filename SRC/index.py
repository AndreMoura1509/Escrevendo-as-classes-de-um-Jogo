# Definindo a classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'realizou um ataque'
        
        print(f"O {self.tipo} atacou usando {ataque}")

# Criando instâncias da classe Heroi
heroi1 = Heroi('Aragorn', 30, 'guerreiro')
heroi2 = Heroi('Gandalf', 1000, 'mago')
heroi3 = Heroi('Bruce Lee', 32, 'monge')
heroi4 = Heroi('Hattori Hanzo', 25, 'ninja')

# Chamando o método atacar para cada herói
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
