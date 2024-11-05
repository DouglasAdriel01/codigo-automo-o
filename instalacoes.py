import subprocess
import os
def atualizar_linux():
    subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')
def instalar_pip():
    subprocess.run(f'''sudo apt install python3-pip''', shell=True, check=True, executable='/bin/bash')
def instalar_venv():
    subprocess.run(f'''sudo apt install python3-venv''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''python3 -m venv .venv''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''source .venv/bin/activate''', shell=True, check=True, executable='/bin/bash')
def criar_pasta(path_full_novo_projeto):
    if os.path.exists(path_full_novo_projeto) == False:
        os.mkdir(path_full_novo_projeto)
def entrar_na_pasta(path_full_novo_projeto):
    os.chdir(path_full_novo_projeto)
def ativar_pasta():
    subprocess.run(f'''source .venv/bin/activate''', shell=True, check=True, executable='/bin/bash')
def abrir_projeto(path_full_novo_projeto):
    subprocess.run(f'''code {path_full_novo_projeto}''', shell=True, check=True, executable='/bin/bash')
def instalar_kivy():
    subprocess.run(f'''sudo apt-get update && sudo apt-get install libgl1''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''python3 -m pip install --upgrade pip setuptools virtualenv''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''python3 -m pip install "kivy[base]" kivy_examples''', shell=True, check=True, executable='/bin/bash')
def instalar_tkinter():
    subprocess.run(f'''sudo apt-get install python3-tk''', shell=True, check=True, executable='/bin/bash')
def instalar_node():
    subprocess.run(f'''curl -sL https://deb.nodesource.com/setup_20.x -o /tmp/nodesource_setup.sh''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''sudo bash /tmp/nodesource_setup.sh''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''sudo apt install nodejs -y''', shell=True, check=True, executable='/bin/bash')
def criar_projeto_react(path_full_novo_projeto):
    subprocess.run(f'''npx create-react-app {path_full_novo_projeto} --template typescript''', shell=True, check=True, executable='/bin/bash')
