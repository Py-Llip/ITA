import os
from Programa_0.funcoes_main import VerificacaoPasta, FormatacaoTexto, GerenciamentoArquivo


class GerenciamentoFormulas:
    def __init__(self):
        pass

    @classmethod
    def add(cls, text: str, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        VerificacaoPasta(path)
        file = GerenciamentoArquivo(path, file).get_arq_initial()
        with open(os.path.join(path, file), 'a+') as arq:
            arq.write(text+'\n')
            arq.seek(0)
        FormatacaoTexto.formatacao(*FormatacaoTexto(path, file).show((-4, None)), title='Adicionado neste arquivo')

    @classmethod
    def dlt(cls, text: str, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        GerenciamentoArquivo(path, file).psc(text)

    def show(self):
        pass


if __name__ == '__main__':
    meuger = GerenciamentoFormulas()
    meuger.dlt('a')
