from pokemon import *
from pessoa import *
from time import sleep
from pickle import dump, load


def escolher_poke_inicial(player):
    print("escolha um pokemon")
    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print(
        f"ola {player} voce tem 3 pokemons para a sua escolha\n1 -- {pikachu}\n2 -- {charmander}\n3 -- {squirtle}"
    )
    while True:
        escolha = input("escolha o seu pokemon: ")
        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("escolha invaldia")


def salvar_jogo(player):
    try:
        with open("pokemon game/database.db", "wb") as arquivo:
            dump(player, arquivo)
            print("jogo salvo com sucesso")
    except Exception as e:
        print("erro ao salvar jogo")
        print(e)


def carregar_jogo():
    try:
        with open("pokemon game/database.db", "rb") as arquivo:
            player = load(arquivo)
            print("loading feito com sucesso")
            return player
    except Exception as e:
        print("save não encontrado")


def pause():
    for _ in range(3):
        sleep(1)
        print("'")


if __name__ == "__main__":
    print("-" * 20)
    print("bem vindo ao game pokemon RPG de terminal!!!")
    print("-" * 20)

    player = carregar_jogo()

    if not player:

        pause()
        nome = input("olá qual é seu nome: ").strip()
        player = Player(nome)
        pause()
        print(
            f"olá {player} esse é uma mundo abitado por pokemons, sua missão é ser o maior mestre pokemon\ncapture o maximo de pokemons que você conseguir e lute contra seus inimigos"
        )

        player.mostrar_dinheiro()
        pause()

        if player.pokemons:
            print("já vi que você tem alguns pokemons")
            player.mostrar_pokemons()
        else:
            print(
                "você não tem nenhum pokemon, por favor escolha um de nossos pokemons"
            )
            escolher_poke_inicial(player)

        pause()

        print(
            "Pronto, agora que você Já possui um pokemon enfrete seu primeiro inimigo"
        )
        hudson = Inimigo(nome="Hudson", pokemons=[PokemonEletrico("pikachu", level=1)])
        player.batalhar(hudson)
        salvar_jogo(player)

    pause()

    while True:
        print(
            """
        -------------------------------------
        |   O'que deseja fazer?             |
        |   1 - Explorar pelo mundo a fora  |
        |   2 - Lutar com um inimigo        |
        |   3 - Ver Pokeagenda              |
        |   0 - Sair do jogo                |
        -------------------------------------
           """
        )
        escolha = str(input("sua escolha: "))
        if escolha == "0":
            print("fechando o jogo...")
            pause()
            break

        elif escolha == "1":
            pause()
            player.explorar()
            salvar_jogo(player)

        elif escolha == "2":
            pause()
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
            pause()
        elif escolha == "3":
            pause()
            player.mostrar_pokemons()

        else:
            print("escolha invalida")
