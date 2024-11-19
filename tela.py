import tkinter as tk
from tkinter import ttk
from instalacoes import abrir_projeto
from configuração_label import validar_input, salvar_data
from subprocess import Popen, PIPE

class App():
    def __init__(self):
        self.tela_code = tk.Tk()
        self.tela_code.title("app gera code")
        
        
        self.creat_widget()

    def creat_widget(self):
        self.label = tk.Label(self.tela_code, text="Escolha o nome do seu projeto", font=("Arial", 12), bg="#f0f0f0")
        self.label.pack(pady=20)
    
        self.input = tk.Entry(self.tela_code)
        self.input.pack(pady=5)

   
        self.label = tk.Label(self.tela_code, text="Escolha qual a linguagem que deseja instalar", font=("Arial", 12), bg="#f0f0f0")
        self.label.pack(pady=20)
        
        self.caixa_selecao_linguagem = ttk.Combobox(self.tela_code, values=["Python","node"])
        self.caixa_selecao_linguagem.pack(pady=5)
        
        self.botao_enviar = tk.Button(self.tela_code, text="Enviar", command=self.enviar)
        self.botao_enviar.pack(pady=5)
        
        self.botao_gerar = tk.Button(self.tela_code, text="Gerar", command=self.gerar)
        self.botao_gerar.pack(pady=5)
        
        self.resultado_label = tk.Label(self.tela_code, text="")
        self.resultado_label.pack(pady=5)
        
        self.bash_saida = tk.Text(self.tela_code, height=10, width=80)
        self.bash_saida.pack(pady=5)
        
        
    def enviar(self):
        name = self.input.get()
        language = self.caixa_selecao_linguagem.get()

        if validar_input(name):
            self.resultado_label.config(text=f"Nome: {name}, Linguagem: {language}")
        else:
            self.resultado_label.config(text="Erro: Nome inválido")
            
    def gerar(self):
        name = self.input.get()
        language = self.caixa_selecao_linguagem.get()
        if validar_input(name):
            self.run_bash("sudo apt-get update -y && sudo apt-get upgrade -y")
            path_full_novo_projeto = salvar_data(name, language)
            message = f'Projeto Criado na pasta {path_full_novo_projeto}'
            self.resultado_label.config(text=message)
            abrir_projeto(path_full_novo_projeto)
        else:
            self.resultado_label.config(text="Erro: Nome inválido")
            
    def run_bash(self, command):
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE) 
        stdout, stderr = process.communicate() 
        self.bash_saida.delete(1.0, tk.END) 
        self.bash_saida.insert(tk.END, stdout.decode()) 
        if stderr: 
            self.bash_saida.insert(tk.END, stderr.decode())


    def run(self):
        self.tela_code.mainloop()









