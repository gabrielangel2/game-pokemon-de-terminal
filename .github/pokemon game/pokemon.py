import random as r


class Pokemon:
    def __init__(self, especie, level=None, nome=None):

        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = r.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return f"{self.nome} lv: {self.level}"

    def atacar(self, pokemon):
        
        ataque_efetivo = int((self.ataque * r.random() * 1.3))
        pokemon.vida -= ataque_efetivo

        print(f"{pokemon} perdeu {ataque_efetivo} pontos de vida")
        print(f'{pokemon} possui {pokemon.vida} pontos de vida')

        if pokemon.vida <= 0:
            print(f"{pokemon} foi derrotado")
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print(f"{self} laçou um raio do trovão em {pokemon}")
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print(f"{self} laçou uma rajada de fogo em {pokemon}")
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon):
        print(f"{self} laçou um jato d'agua em {pokemon}")
        return super().atacar(pokemon)


class PokemonPlanta(Pokemon):
    tipo = "planta"

    def atacar(self, pokemon):
        print(f"{self} lançou Ataque Poison Powder em {pokemon}")
        return super().atacar(pokemon)


class PokemonPsiquico(Pokemon):
    tipo = "psiquico"

    def atacar(self, pokemon):
        print(f"{self} laçou Ataque Psychic em {pokemon}")
        return super().atacar(pokemon)


class PokemonLutador(Pokemon):
    tipo = "lutado"

    def atacar(self, pokemon):
        print(f"{self} laçou Ataque Cross Chop em {pokemon}")
        return super().atacar(pokemon)
