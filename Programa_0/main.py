import os
from Programa_0.funcoes_main import VerificacaoPasta, FormatacaoTexto, GerenciamentoArquivo


class GerenciamentoFormulas:
    def __init__(self, path: str=os.path.join(os.getcwd(), 'armazenamento-formulas'), file: str=None):
        self.path = path
        self.file = GerenciamentoArquivo(self.path, file).get_arq_initial()

    def add(self, text: str):
        VerificacaoPasta(self.path)
        with open(os.path.join(self.path, self.file), 'a+') as arq:
            arq.write(text+'\n')
            arq.seek(0)
        FormatacaoTexto.tabela(*FormatacaoTexto(self.path, self.file).show((-4, None)), title='Adicionado neste arquivo')

    def dlt(self, low: int):
        with open(os.path.join(self.path, self.file), 'r+') as arq:
            conteudo = arq.readlines()
            print(f'\033[31m{FormatacaoTexto(self.path, self.file).formatacao(text=conteudo[low-1], title='Conteúdo apagado:')}\033[m')
            del conteudo[low-1]
            arq.seek(0)
            arq.truncate()
            arq.writelines(conteudo)


    def show(self):
        pass


if __name__ == '__main__':
    meuger = GerenciamentoFormulas()
    meuger.dlt(8)
