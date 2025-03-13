from os import makedirs, getcwd, listdir
from os.path import join, exists

class VerificacaoPasta:
    def __init__(self, path: str=getcwd()):
        self.path = path
        self.criar_pastas()
    def criar_pastas(self):
        caminho = join(self.path, 'formulas-temporarias')
        if not exists(caminho):
            makedirs(caminho)

class FormatacaoTexto:
    def __init__(self, path: str, file: str=None):
        self.path = path
        self.file = file

    def show(self, n: tuple=(0, None)):
        with open(join(self.path, self.file), 'r') as arq:
            conteudo = arq.readlines()
            formatado = []
            for l in conteudo:
                formatado.append([l])
            return formatado[n[0]:n[1]]

    @staticmethod
    def formatacao(text: str, title: str=''):
        if text in '\n':
            lows = text.splitlines()
            print(f'\033[32;1m{title:^{len(lows[0])}}\033[m')
        else:
            print(f'\033[32;1m{title:^{len(text)}}\033[m')
        return text

    @staticmethod
    def tabela(*args_colums, title: str='', subtitles: tuple=()):
        m = 0
        n_colums = 0
        for args in args_colums:
            if args_colums.index(args) == 0:
                n_colums  = len(args)
            elif n_colums < len(args):
                n_colums = len(args)
            for arg in args:
                if args_colums.index(args) == 0 and args.index(arg) == 0:
                    m = len(str(arg))
                elif len(str(arg)) > m:
                    m = len(str(arg))

        print(f'\033[97;1m{title:^{round(n_colums * m + 5 * n_colums)}}\033[m\n')
        for args in args_colums:
            for arg in args:
                if subtitles != ():
                    if args.index(arg) == 0 and args_colums.index(args) == 0:
                        for e, s in enumerate(args):
                            print(f'\033[32;1m{subtitles[args.index(arg)+e]:^{m + 5}}\033[m', end='' if e < len(subtitles)-1 else None)
                        print()
                print(f'{"\033[37m" if args_colums.index(args) % 2 != 0 else ""}{"| " if args.index(arg) == 0 else ""} {arg.strip():^{m}} | \033[m', end='')
            print()

class GerenciamentoArquivo:
    def __init__(self, path: str, file: str=None):
        self.path = path
        self.file = file

    def get_arq_initial(self):
        if self.file is None:
            for a in listdir(self.path):
                if a.endswith('.txt'):
                    return a
        return self.file

    def psc(self, text: str='*every*'):
        file = GerenciamentoArquivo(self.path, self.file).get_arq_initial()
        with open(join(self.path, file), 'r+') as arq:
            if text == '*every*':
                print(arq.read())
            else:
                conteudo = arq.readlines()
                lista_psc = []
                index = 0
                for l in conteudo:
                    if text.strip().lower() in l.strip().lower():
                        lista_psc.append([l, f'{conteudo.index(l, index)+1}° Linha'])
                        index = conteudo.index(l, index)
                FormatacaoTexto.tabela(*lista_psc, title='Resultados da Pesquisa:', subtitles=('Informação', 'Linha'))
                return lista_psc

class Inputs:
    def __init__(self, text: str):
        self.text = text

    def str(self):
        npt = str(input(self.text))
        return npt

    def int(self):
        pass

    def protecao(self, npt, loop: bool=False):
        pass



