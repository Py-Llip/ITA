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

#sistema da resposta
def answer():
    resp = None
    while not resp:
        resp = fc.Inputs('Responda: ').question(**s.random())

#Questões
menu = False
while not menu:
    fc.FormatacaoTexto.tabela((1, 'Responder'), (2, 'Gabarito'), (3, 'Adicionar'), (4, 'Apagar'), (5, 'Finalizar'), title='MENU', subtitles=('Opções', 'Descrição'))
    op(**{'1': answer,
          '2': partial(fc.FormatacaoTexto.tabela,*fc.GerenciamentoArquivo(s.path, s.file).file_liker(s.question_file).items(), title='GABARITO', subtitles=('Questão', 'Resposta')),
          '3': lambda:fc.FormatacaoTexto.tabela(*fc.GerenciamentoArquivo(s.path, s.file).file_show(), title='OPÇÕES') or frml.ManipulacaoFormulas().add(text=fc.Inputs('Digite o texto que você deseja adicionar: '), file=fc.Inputs('Qual o nome do arquivo que deseja adicionar? ').str()).str()})()

    menu = True if fc.Inputs('Deseja continuar? (s/n): ').str()[0].strip().lower() in 'n' else False



