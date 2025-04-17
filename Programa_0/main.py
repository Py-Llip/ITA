import Programa_0.edfrml as frml
import Programa_0.funcoes_main as fc
from functools import partial

#linha
def l(char: str='-', length: int=1, align_format: tuple=('*', '^', 0)):
    return f'{char*(length//len(char) if length // len(char) > 0 else 1):{align_format[0]}{align_format[1]}{align_format[2]}}'

#escolher opções
def op(**option_func):
    opcao = fc.Inputs('Digite a \033[97;1mOPÇÃO\033[m que deseja: ').str()
    return option_func.get(opcao, None)

#Mensagem de boas-vindas
l1 = l('*', 26, ('', '^', 150))
print(l1)
print(f'{'Olá, Seja muito bem-vindo!':^150}')
print(l1)

#Funções das Opções
# Sistema de respostas
def answer(sequence: bool=False):
    resp = None
    while not resp:
        print(l('¨', 20))
        if not sequence:
            resp = fc.Inputs('Responda: ').question(**s.random())
        else:
            resp = fc.Inputs('Responda: ').question(**s.sequence())

# Sistema de escrever num arquivo
def add_dlt(tp: str=False):
    print(l('¨', 20))
    if tp:
        partial(r.add, file=s.file, text=fc.Inputs('Texto para adicionar: ').str())()
    else:
        partial(r.dlt, file=s.file, low=fc.Inputs('Linha para apagar: ').int())()

# Mostrar arquivo
def file_show():
    copia = r.file
    r.file = s.question_file
    r.show()
    r.file = copia

#opções de arquivo
def file_op():
    arqs = [[e + 1, i[0]] for e, i in enumerate(fc.GerenciamentoArquivo(s.path, s.file).file_show())]
    print(arqs)
    fc.FormatacaoTexto.tabela(*arqs, title='OPÇÕES', subtitles=('N°', 'ARQUIVOS'))
    while True:
        np = fc.Inputs('Número do arquivo de \033[97;1mARGUMENTOS\033[m: ').int()
        nr = fc.Inputs('Número do arquivo de \033[97;1mFÓRMULAS\033[m: ').int()
        if 1 <= np <= len(arqs) and 1 <= nr <= len(arqs):
            return arqs[np-1][1], arqs[nr-1][1]
        print('\033[31;1mIndexError! os números colocados não correspondem a nenhum arquivo!\033[m')

#Arquivo que deseja usar
s = frml.GerenciamentoFormulas()
r = frml.ManipulacaoFormulas()
while True:
    s.question_file, s.file = file_op()
    r.file = s.file

    #Questões
    menu = False
    while not menu:
        print(l(length=100))
        fc.FormatacaoTexto.tabela((1, 'Responder'), (2, 'Gabarito'), (3, 'Adicionar'), (4, 'Apagar'),(5, 'Questões'), (6, 'Finalizar'), title='MENU', subtitles=('Opções', 'Descrição'))
        print(l(length=100))
        op(**{'1': lambda: answer(sequence=True if fc.Inputs('Em \033[97;1mSEQUÊNCIA?\033[m (s/n): ').str().strip().lower()[0] in 's' else False),
              '2': partial(fc.FormatacaoTexto.tabela,*fc.GerenciamentoArquivo(s.path, s.file).file_liker(s.question_file).items(), title='GABARITO', subtitles=('Questão', 'Resposta')),
              '3': partial(add_dlt, tp=True),
              '4': add_dlt,
              '5': file_show,
              '6': exit})()
        menu = True if fc.Inputs('Deseja \033[97;1mCONTINUAR?\033[m (s/n): ').str()[0].strip().lower() in 'n' else False



