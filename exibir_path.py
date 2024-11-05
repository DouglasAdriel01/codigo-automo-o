import os
def exibir_path(diretorio_projetos):
    # VERIFICA SE NA RAIZ DO PROJETO EXISTE UM ARQUIVO MAIN
    # CASO NÃO ELE É CRIADO 
    if os.path.isfile(f'{diretorio_projetos}/main.py') == False:
        os.mknod('main.py')
    # EXIBE O CAMINHO COMPLET DO NOVO PROJETO CRIADO
    print(f'{diretorio_projetos}/main.py')