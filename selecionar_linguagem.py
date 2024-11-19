from exibir_path import exibir_path
from path_home import path_home
from criar_diretorio import criar_projetos
from criar_diretorio import path_projeto, verifica_pasta
from instalacoes import atualizar_linux, instalar_pip, instalar_venv, ativar_pasta, criar_pasta, abrir_projeto, entrar_na_pasta, instalar_kivy, instalar_tkinter, instalar_node,criar_projeto_react

diretorio_projetos = path_home("Projetos")
criar_projetos(diretorio_projetos)
path_full_novo_projeto =  path_projeto(diretorio_projetos)
verifica_pasta(diretorio_projetos)
lingua_instalar = input(" quer instalar python ou node?\n")


path_full_novo_projeto =  path_projeto(diretorio_projetos)

def selecionar_tipo_projeto():
    atualizar_linux()
    lingua_instalar = input(" quer instalar python ou node?\n")
    if lingua_instalar == "python":
        instalar_pip()
        instalar_venv()
        exibir_path(path_full_novo_projeto)
    quero_instalar = input("quer instalar tkinter ou kivy?\n")
    if quero_instalar == "tkinter":
        print("instalando tkinter")
        instalar_tkinter()
    elif quero_instalar =="kivy":
        instalar_kivy()
    elif lingua_instalar == "node":
        instalar_node()
    quero_instalar_react = input("quer instalar o react?\n")
    if quero_instalar_react == "ss" or quero_instalar_react == "sim":
        criar_projeto_react(path_full_novo_projeto)