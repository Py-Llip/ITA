import Programa_0.edfrml as frml
import Programa_0.funcoes_main as fc
from math import ceil
def l(tp: str='-', size: int=1, frmt: tuple=('*', '^', 0)):
    return f'{tp*(size//len(tp) if size // len(tp) > 0 else 1):{frmt[0]}{frmt[1]}{frmt[2]}}'
while True:
    l1 = l('*', 26, ('', '^', 150))
    print(l1)
    print(f'{'Olá, Seja muito bem-vindo!':^150}')
    print(l1)
    narq = 'formula_01.txt'#fc.Inputs(f'{'Nome do arquivo que quer acessar: ':>92}').str()
    s = frml.GerenciamentoFormulas(file=narq)
    while True:
        fc.Inputs('Responda: ').question(**s.random())
        break

