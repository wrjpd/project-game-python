"""
Projeto 1 - Game

Ordem de execução:

1 - Perguntar ao usuário o nível de dificuldade;
2 - Chama a classe que consiste em : 
    dificuldade
    valor1
    valor2
    operacao
    resultado

A dificuldade consiste no número de algarismos

"""

from models.calcular import Calcular


def main():
    """ Main function """
    pontos_game = 0
    jogar(pontos_game)


def jogar(pontos_game: int) -> None:
    """ Funcao que faz o usuário jogar"""

    while (dificuldade := int(
            input("Informe o nível de dificuldade desejado [1,2,3 ou 4]: "))) not in [1, 2, 3, 4]:
        dificuldade = int(input("Por favor, digite um número de 1 a 4"))
    print(dificuldade)

    calc: Calcular = Calcular(dificuldade)
    answer = int(input(
        f"Informe o resultado para a seguinte operação: \n{calc.mostrar_operacao()} = "))

    if calc.checar_resultado(answer):
        print("Resposta correta!")
        pontos_game += 1
        print(f'Você tem {pontos_game} pontos(s).')
    else:
        print("Resposta Errada!")
        print(f'Você tem {pontos_game} pontos(s).')

    if int(input("Deseja continuar no jogo? [1 - sim,0 - não]")):
        jogar(pontos_game)
    else:
        print(f"Você finalizou com {pontos_game} pontos. \nAté a próxima")


if __name__ == "__main__":
    main()
