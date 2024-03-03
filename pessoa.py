import random

from pokemon import *


NOMES = [
    "Lucas",
    "Sofia",
    "Gabriel",
    "Isabella",
    "Mateus",
    "Laura",
    "Enzo",
    "Giovanna",
    "Pedro",
    "Valentina",
    "Miguel",
    "Maria Eduarda",
    "Arthur",
    "Alice",
    "João",
    "lara",
    "Davi",
    "Manuela",
    "Matheus",
    "Helena",
]
POKEMONS = [
    PokemonEletrico("pikachu"),
    PokemonAgua("Squirtle"),
    PokemonFogo("Charizard"),
    PokemonLutador("Machamp"),
    PokemonPlanta("Bulbasaur"),
    PokemonPsiquico("Alakazam"),
    # Adicione mais Pokémons conforme necessário
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"pokemons de {self}:")
            for index, pokemon in enumerate(self.pokemons):
                print(f"{index} - {pokemon}")
        else:
            print(f"{self} não tem nenhum  pokemon")

    def escolher_pokemon(self):
        if self.pokemons:
            pokem_escolhido = random.choice(self.pokemons)
            print(f"{self} escolheu {pokem_escolhido}")
            return pokem_escolhido
        else:
            print("ERRO: esse jogado não possui nenhum pokemon para ser escolhido")

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f"voce ganhou $: {quantidade}")
        self.mostrar_dinheiro()

    def mostrar_dinheiro(self):
        print(f"voce possui $: {self.dinheiro} em sua conta")

    def batalhar(self, pessoa):
        print(f"{self} iniciou uma batalha com {pessoa}")

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f"{self} ganhou a batalha")
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f"{pessoa} ganhou a batalha")
                    break
        else:
            print("essa batalha não pode ocorrer")
            
class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self} capturou {pokemon}")

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("escolha o seu pokemon: ")
                try:
                    escolha = int(escolha)
                    pokem_escolhido = self.pokemons[escolha]
                    print(f"{pokem_escolhido} eu escolho você!!")
                    return pokem_escolhido
                except:
                    print("escolha invalida")
        else:
            print("ERRO: esse jogado não possui nenhum pokemon para ser escolhido")

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f"um pokemon selvagem apareceu: {pokemon}")

            escolha = input("deseja capturar o pokemon? S/N ").upper()
            if escolha == "S":
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f"{pokemon} fugiu")
            else:
                print("ok boa viajem")
        else:
            print("essa exploração não deu em nada")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome, pokemons=pokemons)
