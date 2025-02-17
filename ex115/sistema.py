from ex115.lib.interface import *
from ex115.lib.acesso import *
from time import sleep

arq = 'listacurso.txt'

if not arquivoExiste(arq):
    criarTxt(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastraPessoa(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)