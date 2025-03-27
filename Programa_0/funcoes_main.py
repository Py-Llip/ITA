from os import makedirs, getcwd, listdir
from os.path import join, exists

class VerificacaoPasta:
    def __init__(self, path: str=getcwd()):
        self.path = path

    def criar_pastas(self, pasts: tuple=('formulas', 'argumentos', 'formulas-temporarias')):
        for n in pasts:
            caminho = join(self.path, str(n))
            if not exists(caminho):
                makedirs(caminho)
        return self.path

class FormatacaoTexto:
    def __init__(self, path: str, file: str=None):
        self.path = path
        self.file = file

    def show(self, n: tuple=(0, None)):
        with open(join(self.path, self.file), 'r', encoding='utf-8') as arq:
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

        for s in subtitles:
            if len(str(s)) > m:
                m = len(s)

        print(f'\033[97;1m{title:^{round(n_colums * m + 5 * n_colums)}}\033[m\n')
        for args in args_colums:
            for arg in args:
                if subtitles != ():
                    if args.index(arg) == 0 and args_colums.index(args) == 0:
                        for e, s in enumerate(args):
                            print(f'\033[32;1m{subtitles[args.index(arg)+e]:^{m + 5}}\033[m', end='' if e < len(subtitles)-1 else None)
                        print()
                print(f'{"\033[37m" if args_colums.index(args) % 2 != 0 else ""}{"| " if args.index(arg) == 0 else ""} {str(arg).strip():^{m}} | \033[m', end='')
            print()

class GerenciamentoArquivo:
    def __init__(self, path: str, file: str=None):
        self.path = path
        self.file = file

    def get_arq_initial(self, path: str=''):
        if self.file is None:
            for a in listdir(join(self.path, path)):
                if a.endswith('.txt'):
                    return join(path, a)
        return join(path, self.file)

    def psc(self, text: str=''):
        with open(join(self.path, self.file), 'r+', encoding='utf-8') as arq:
            conteudo = arq.readlines()
            lista_psc = []
            index = 0
            for l in conteudo:
                if text.strip().lower() in l.strip().lower():
                    lista_psc.append([l, f'{conteudo.index(l, index)+1}° Linha'])
                    index = conteudo.index(l, index)
                FormatacaoTexto.tabela(*lista_psc, title='Resultados da Pesquisa:', subtitles=('Informação', 'Linha'))
                return lista_psc

    def file_liker(self, file2: str):
        dic = {}
        for n in [self.file, file2]:
            with open(join(self.path, n), 'r', encoding='utf-8') as arq:
                if n == self.file:
                    formula = arq.readlines()
                else:
                    enunciado = arq.readlines()
                    for i in range(len(enunciado)):
                        try:
                            dic[enunciado[i]] = formula[i]
                        except IndexError:
                            break
        return dic

class Inputs:
    def __init__(self, text: str=None):
        self.text = text

    @staticmethod
    def _protegido(func):
        def wrapper(self, *args, **kwargs):
            cont_erro = 0
            resultado = None
            while cont_erro < 30:
                try:
                    resultado = func(self, *args, **kwargs)
                except Exception:
                    print('\033[31;1mErro!\033[m')
                    cont_erro +=1
                else:
                    break
            return resultado
        return wrapper

    @_protegido
    def str(self):
        return str(input(self.text))

    @_protegido
    def int(self):
        return int(input(self.text))

    @_protegido
    def question(self, question:str=None, answer: str=None, **full):
        question = list(full.keys())[0] if question is None else question
        answer = list(full.values())[0] if answer is None else answer
        print(self.text) if self.text is not None else None
        a = str(input(question))
        if a.strip().lower() in answer.strip().lower():
            if a.strip().lower() == answer.strip().lower():
                print(f'\033[32;1mVocê acertou! dada: {a} = certa: {answer}\033[m')
                return True
            else:
                print(f'\033[33;1mVocê quase acertou. dada: {a} <-- quase isso\033[m')
                return None
        else:
            print('\033[31;1mResposta errada!\033[m')
            return False





if __name__ == '__main__':
    g = GerenciamentoArquivo(join(getcwd(), 'armazenamento-formulas'), join('formulas', 'formula_01.txt'))
    g.file_liker(join('argumentos', 'argumento_01.txt'))




