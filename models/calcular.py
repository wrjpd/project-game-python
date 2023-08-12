"""Classe calcular"""

from random import choice
from numpy.random import randint


class Calcular:

    """A partir de uma dificuldade entre 1 e 4, cria uma operação baseada no número de algarismos."""

    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self.gerar_valor
        self.__valor2: int = self.gerar_valor
        self.__operacao: str = self.operacao
        self.__result: str = self.result

    @property
    def gerar_valor(self) -> int:
        """Gera um valor aleatório baseado na dificuldade"""
        max = int("1"+self.__dificuldade*"0")
        min = int("1"+(self.__dificuldade-1)*"0")
        return randint(min, max)

    @property
    def operacao(self) -> str:
        """Retorna a operação +, - ou * aleatoriamente"""
        operacoes = ["+", "-", "*"]
        return choice(operacoes)

    @property
    def result(self) -> str:
        """Retorna o resultado da operação"""   
        return (eval(self.mostrar_operacao()))

    def mostrar_operacao(self) -> str:
        """Retorna a string da operação"""
        return f"{self.__valor1}{self.__operacao}{self.__valor2}"

    def checar_resultado(self, answer: int) -> bool:
        """Checa se o resultado está correto"""
        print(self.__result)
        print(answer)
        if answer == self.__result:
            return True
        return False
