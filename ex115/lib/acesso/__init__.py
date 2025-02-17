import os.path
from ex115.lib.interface import *


def arquivoExiste(nome):
    return os.path.exists(nome)


def criarTxt(nome):
    try:
        a=open(nome, 'wt+')
        a.close()
    except:
        print('Não foi possivel Criar o arquivo')
    else:
        print(f'Arquivo{nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi Possível Ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado= linha.split(';')
            dado[1]= dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastraPessoa(arq, nome='desconhecido', idade = 0):
    try:
        a = open(arq , 'at')
    except:
        print('falha na abertura para cadastrar')
    else:
        try:
            a.write(f'\n{nome};{idade}')
        except:
            print('Falha na hora de escrever dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()