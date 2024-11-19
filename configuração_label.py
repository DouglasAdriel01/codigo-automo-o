from path_home import path_home
from criar_diretorio import criar_projetos
def validar_input(name):
    return name.isalnum()

def salvar_data(dir_novo_projeto, opcao_projeto):
    diretorio_projetos = init_criar_projeto()
    # return select_project_type(opcao_projeto, diretorio_projetos, dir_novo_projeto)

def init_criar_projeto():
    diretorio_home = path_home()
    diretorio_projetos = f'{diretorio_home}/Projetos'
    criar_projetos(diretorio_projetos)
    return diretorio_projetos