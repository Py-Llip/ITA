import os
from abc import ABC, abstractmethod
from Programa_0.funcoes_main import VerificacaoPasta, FormatacaoTexto, GerenciamentoArquivo, Inputs


class Interface(ABC):
    def __init__(self, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        self._path = VerificacaoPasta(path).criar_pastas()
        self._file = GerenciamentoArquivo(self._path, file).get_arq_initial('formulas')

class ManipulacaoFormulas(Interface):
    def add(self, text: str):
        with open(os.path.join(self._path, self._file), 'a+', encoding='utf-8') as arq:
            arq.write(text+'\n')
            arq.seek(0)
        FormatacaoTexto.tabela(*FormatacaoTexto(self._path, self._file).show((-4, None)), title='Adicionado neste arquivo')

    def dlt(self, low: int):
        with open(os.path.join(self._path, self._file), 'r+', encoding='utf-8') as arq:
            conteudo = arq.readlines()
            print(f'\033[31m{FormatacaoTexto(self._path, self._file).formatacao(text=conteudo[low - 1], title='Conteúdo apagado:')}')
            del conteudo[low-1]
            arq.seek(0)
            arq.truncate()
            arq.writelines(conteudo)

    def show(self, n: tuple=(0, None)):
        fortext = FormatacaoTexto(self._path, self._file)
        arq = fortext.show(n)
        for _ in range(len(arq)):
            arq[_].append(_+1+n[0])
        fortext.tabela(*arq, title=f'ARQUIVO: {self._file}', subtitles=('Conteúdos', 'Linhas°'))

class GerenciamentoFormulas(Interface):
    __lis_liker = {}
    __sequence_index = -1
    def __init__(self, question_file: str=None, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        super().__init__(path, file)
        self._question_file = GerenciamentoArquivo(self._path, question_file).get_arq_initial('argumentos')
        self._liker = GerenciamentoArquivo(self._path, self._file).file_liker(self._question_file)

    def random(self):
        from random import choice
        dic_i = {}
        if not GerenciamentoFormulas.__lis_liker:
            GerenciamentoFormulas.__lis_liker = self._liker
            GerenciamentoFormulas.__lis_liker = list(GerenciamentoFormulas.__lis_liker.items())
        i = GerenciamentoFormulas.__lis_liker.pop(GerenciamentoFormulas.__lis_liker.index(choice(GerenciamentoFormulas.__lis_liker)))
        dic_i[i[0]] = i[1]
        return dic_i

    def sequence(self):
        if self.__sequence_index+2 <= len(self._liker.items()):
            self.__sequence_index += 1
        else:
            self.__sequence_index = 0
        return list(self._liker.items())[self.__sequence_index]



if __name__ == '__main__':
    pass


