import os
from abc import ABC, abstractmethod
from Programa_0.funcoes_main import VerificacaoPasta, FormatacaoTexto, GerenciamentoArquivo, Inputs


class Interface(ABC):
    def __init__(self, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        self.path = VerificacaoPasta(path).criar_pastas()
        self.file = GerenciamentoArquivo(self.path, file).get_arq_initial('formulas')

class ManipulacaoFormulas(Interface):
    def add(self, text: str):
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
    lis_liker = {}
    sequence_index = -1
    def __init__(self, question_file: str=None, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        super().__init__(path, file)
        self.question_file = GerenciamentoArquivo(path, question_file).get_arq_initial('argumentos')
        self.liker = GerenciamentoArquivo(self.path, self.file).file_liker(self.question_file)

    def random(self):
        from random import choice
        dic_i = {}
        if not GerenciamentoFormulas.lis_liker:
            GerenciamentoFormulas.lis_liker = self.liker
            GerenciamentoFormulas.lis_liker = list(GerenciamentoFormulas.lis_liker.items())
        i = GerenciamentoFormulas.lis_liker.pop(GerenciamentoFormulas.lis_liker.index(choice(GerenciamentoFormulas.lis_liker)))
        dic_i[i[0]] = i[1]
        return dic_i

    def sequence(self):
        if self.sequence_index+2 <= len(self.liker.items()):
            self.sequence_index += 1
        else:
            self.sequence_index = 0
        return list(self.liker.items())[self.sequence_index]



if __name__ == '__main__':
    pass

