from pathlib import Path
import os


def path_home(folder:str='projetos'):
    # BUSCAR NOME DA PASTA DE USUÁRIO
    diretorio_home = Path.home()
    # ENTRAR NA PASTA DE USUÁRIO
    os.chdir(diretorio_home)
    # VARIAVÉL PARA DIRETÓRIO PADRÃO DOS PROJETOS
    return f'{diretorio_home}/{folder}'
