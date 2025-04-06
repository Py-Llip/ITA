import Programa_0.edfrml as frml
import Programa_0.funcoes_main as fc
from functools import partial

#linha
def l(tp: str='-', size: int=1, frmt: tuple=('*', '^', 0)):
    return f'{tp*(size//len(tp) if size // len(tp) > 0 else 1):{frmt[0]}{frmt[1]}{frmt[2]}}'

#escolher opções
def op(**option_func):
    opcao = fc.Inputs('Digite a opção que deseja: ').str()
    return option_func.get(opcao, None)

#Mensagem de boas-vindas
l1 = l('*', 26, ('', '^', 150))
print(l1)
print(f'{'Olá, Seja muito bem-vindo!':^150}')
print(l1)

#Arquivo que deseja usar
s = frml.GerenciamentoFormulas(file='formula_01.txt') #fc.Inputs(f'{'Nome do arquivo que quer acessar: ':>92}').str()

#Funções das Opções
# Sistema de respostas
def answer():
    resp = None
    while not resp:
        resp = fc.Inputs('Responda: ').question(**s.random())

# Sistema de escrever num arquivo
def add_dlt(tp: str=False):
    c = frml.ManipulacaoFormulas()
    arqs = [[e+1, i[0]] for e, i in enumerate(fc.GerenciamentoArquivo(s.path, s.file).file_show())]
    fc.FormatacaoTexto.tabela(*arqs, title='OPÇÕES', subtitles=('N°', 'ARQUIVOS'))
    na = fc.Inputs('Número do arquivo: ').int()
    if tp:
        partial(c.add, file=arqs[na-1][1], text=fc.Inputs('Texto para adicionar: ').str())()
    else:
        partial(c.dlt, file=arqs[na-1][1], low=fc.Inputs('Linha para apagar: ').int())()

#Questões
menu = False
while not menu:
    fc.FormatacaoTexto.tabela((1, 'Responder'), (2, 'Gabarito'), (3, 'Adicionar'), (4, 'Apagar'),(5, 'Mostrar'), (6, 'Finalizar'), title='MENU', subtitles=('Opções', 'Descrição'))
    op(**{'1': answer,
          '2': partial(fc.FormatacaoTexto.tabela,*fc.GerenciamentoArquivo(s.path, s.file).file_liker(s.question_file).items(), title='GABARITO', subtitles=('Questão', 'Resposta')),
          '3': partial(add_dlt, tp=True),
          '4': add_dlt,
          '5': frml.ManipulacaoFormulas().show()})()

    menu = True if fc.Inputs('Deseja continuar? (s/n): ').str()[0].strip().lower() in 'n' else False



