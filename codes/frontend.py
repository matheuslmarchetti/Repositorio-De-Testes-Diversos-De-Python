import tkinter as tk
from tkinter import ttk
import subprocess

def execute_script(script_name, client_name, base_name, inclusion_emails, removal_emails=None):
    # Função para executar o script com os parâmetros fornecidos
    cmd = ['python', script_name, client_name, base_name, inclusion_emails]
    if removal_emails:
        cmd.append(removal_emails)
    subprocess.run(cmd)

def submit_inputs():
    # Função para processar os inputs do usuário e executar o script apropriado
    selected_option = option_var.get()
    client_name = client_name_entry.get()
    base_name = base_name_entry.get()
    inclusion_emails = inclusion_emails_entry.get()
    removal_emails = removal_emails_entry.get() if selected_option == "Inclusão de E-mail com remoção parcial" else None
    
    if selected_option == "Inclusão de E-mail":
        execute_script("_main_inclusao_de_email.py", client_name, base_name, inclusion_emails)
    elif selected_option == "Inclusão de E-mail com remoção parcial":
        execute_script("_main_inclusao_de_email_com_remocao_parcial.py", client_name, base_name, inclusion_emails, removal_emails)

# Criar a janela principal
root = tk.Tk()
root.title("RPA SHAKA")
root.configure(bg='#2b2b2b')  # Cor de fundo escura

# Criar a opção de escolha
option_label = ttk.Label(root, text="Escolha uma opção:", foreground='white', background='#2b2b2b')
option_label.grid(row=0, column=0, padx=10, pady=10)
option_var = tk.StringVar()
option_combobox = ttk.Combobox(root, textvariable=option_var, values=["Inclusão de E-mail", "Inclusão de E-mail com remoção parcial"])
option_combobox.grid(row=0, column=1, padx=10, pady=10)

# Criar os inputs
client_name_label = ttk.Label(root, text="Nome do Cliente da Base:", foreground='white', background='#2b2b2b')
client_name_label.grid(row=1, column=0, padx=10, pady=10)
client_name_entry = ttk.Entry(root)
client_name_entry.grid(row=1, column=1, padx=10, pady=10)

base_name_label = ttk.Label(root, text="Nome da Base:", foreground='white', background='#2b2b2b')
base_name_label.grid(row=2, column=0, padx=10, pady=10)
base_name_entry = ttk.Entry(root)
base_name_entry.grid(row=2, column=1, padx=10, pady=10)

inclusion_emails_label = ttk.Label(root, text="E-mails de inclusão (separados por vírgula):", foreground='white', background='#2b2b2b')
inclusion_emails_label.grid(row=3, column=0, padx=10, pady=10)
inclusion_emails_entry = ttk.Entry(root)
inclusion_emails_entry.grid(row=3, column=1, padx=10, pady=10)

removal_emails_label = ttk.Label(root, text="E-mails de remoção (separados por vírgula):", foreground='white', background='#2b2b2b')
removal_emails_label.grid(row=4, column=0, padx=10, pady=10)
removal_emails_entry = ttk.Entry(root)
removal_emails_entry.grid(row=4, column=1, padx=10, pady=10)

# Botão de enviar
submit_button = ttk.Button(root, text="Executar", command=submit_inputs)
submit_button.grid(row=5, columnspan=2, padx=10, pady=10)

# Executar a aplicação
root.mainloop()
