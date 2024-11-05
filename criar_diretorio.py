from pathlib import Path
import os


def criar_projetos (diretorio_projetos):
    # VERIFICA SE EXISTE O DIRETÓRIO PADRÃO CASO NÃO ELE O CRIA
    if os.path.exists(diretorio_projetos) == False:
        os.mkdir(diretorio_projetos)
    # ENTRA NO DIRETÓRIO PADRÃO
    os.chdir(diretorio_projetos)
    
def path_projeto(diretorio_projetos):
    # SOLICITA AO USUÁRIO UM NOME PARA O PROJETO A SER CRIADO
    dir_novo_projeto = input('Digite o nome do Projeto a ser criado: ')
    # VARIÁVEL COM O CAMINHO COMPLETO DO PROJETO A SER CRIADO
    return f'{diretorio_projetos}/{dir_novo_projeto}' 

def verifica_pasta(diretorio_projetos):
    if os.path.exists(diretorio_projetos) == False:
        os.mkdir(diretorio_projetos)
