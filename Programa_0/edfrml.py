import os
from abc import ABC, abstractmethod
from Programa_0.funcoes_main import VerificacaoPasta, FormatacaoTexto, GerenciamentoArquivo, Inputs
from random import shuffle


class Interface(ABC):
    def __init__(self, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        self.path = VerificacaoPasta(path).criar_pastas()
        self.file = GerenciamentoArquivo(self.path, file).get_arq_initial('formulas')


class ManipulacaoFormulas(Interface):
    def add(self, text: str, file: str=None):
        file = self.file if file is None else file
        with open(os.path.join(self.path, file), 'a+', encoding='utf-8') as arq:
            arq.write(text+'\n')
            arq.seek(0)
        FormatacaoTexto.tabela(*FormatacaoTexto(self.path, file).show((-4, None)), title='Adicionado neste arquivo')

    def dlt(self, low: int, file: str=None):
        file = self.file if file is None else file
        with open(os.path.join(self.path, file), 'r+', encoding='utf-8') as arq:
            conteudo = arq.readlines()
            print(f'\033[31m{FormatacaoTexto(self.path, self.file).formatacao(text=conteudo[low - 1], title='Conteúdo apagado:')}\033[m')
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
    def __init__(self, question_file: str=None, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        super().__init__(path, file)
        self.question_file = GerenciamentoArquivo(self.path, question_file).get_arq_initial('argumentos')
        self.__sequence_index = 0
        self._liker = list(GerenciamentoArquivo(self.path, self.file).file_liker(self.question_file).items())
        if not self._liker:
            raise ValueError('_liker está vazio, Verifique os arquivos de entrada.')
        self.__lis_liker = self._liker[:]
        shuffle(self.__lis_liker)



    def random(self):
        if not self.__lis_liker:
            self.__lis_liker = self._liker[:]
            shuffle(self.__lis_liker)
        i = self.__lis_liker.pop()
        return {i[0]: i[1]}

    def sequence(self):
        i = self._liker[self.__sequence_index]
        self.__sequence_index = (self.__sequence_index+1) % len(self._liker)
        return {i[0]: i[1]}



if __name__ == '__main__':
    pass


