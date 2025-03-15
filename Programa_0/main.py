import os
from abc import ABC, abstractmethod
from Programa_0.funcoes_main import VerificacaoPasta, FormatacaoTexto, GerenciamentoArquivo, Inputs


class Interface(ABC):
    def __init__(self, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        self.path = path
        self.file = GerenciamentoArquivo(self.path, file).get_arq_initial()

class ManipulacaoFormulas(Interface):
    def add(self, text: str):
        VerificacaoPasta(self.path)
        with open(os.path.join(self.path, self.file), 'a+', encoding='utf-8') as arq:
            arq.write(text+'\n')
            arq.seek(0)
        FormatacaoTexto.tabela(*FormatacaoTexto(self.path, self.file).show((-4, None)), title='Adicionado neste arquivo')

    def dlt(self, low: int):
        with open(os.path.join(self.path, self.file), 'r+', encoding='utf-8') as arq:
            conteudo = arq.readlines()
            print(f'\033[31m{FormatacaoTexto(self.path, self.file).formatacao(text=conteudo[low-1], title='Conteúdo apagado:')}')
            del conteudo[low-1]
            arq.seek(0)
            arq.truncate()
            arq.writelines(conteudo)

    def show(self, n: tuple=(0, None)):
        fortext = FormatacaoTexto(self.path, self.file)
        arq = fortext.show(n)
        for _ in range(len(arq)):
            arq[_].append(_+1+n[0])
        fortext.tabela(*arq, title=f'ARQUIVO: {self.file}', subtitles=('Conteúdos', 'Linhas°'))

class GerenciamentoFormulas(Interface):
    lis_randint = []
    def random(self):
        from random import randint
        with open(os.path.join(self.path, self.file), 'r', encoding='utf-8') as arq:
            t = len(arq.readlines())-1
        while not len(GerenciamentoFormulas.lis_randint)-1 >= t:
            a = randint(0, t)
            if a not in GerenciamentoFormulas.lis_randint:
                GerenciamentoFormulas.lis_randint.append(a)

        





    def sequence(self):
        pass


if __name__ == '__main__':
    meuger = GerenciamentoFormulas()
    meuger.random()

