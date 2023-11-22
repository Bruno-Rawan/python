import tkinter as tk
from tkinter import messagebox

class CadastroUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuários")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.label_nome = tk.Label(self.frame, text="Nome:")
        self.label_nome.grid(row=0, column=0, sticky="e", pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        self.label_email = tk.Label(self.frame, text="E-mail:")
        self.label_email.grid(row=1, column=0, sticky="e", pady=5)
        self.entry_email = tk.Entry(self.frame)
        self.entry_email.grid(row=1, column=1, pady=5)

        self.label_telefone = tk.Label(self.frame, text="Telefone:")
        self.label_telefone.grid(row=2, column=0, sticky="e", pady=5)
        self.entry_telefone = tk.Entry(self.frame)
        self.entry_telefone.grid(row=2, column=1, pady=5)

        self.button_cadastrar = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar_usuario)
        self.button_cadastrar.grid(row=3, columnspan=2, pady=10)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        telefone = self.entry_telefone.get()

        if nome and email and telefone:
            # Aqui você pode adicionar o código para salvar os dados em algum lugar (por exemplo, um banco de dados)
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Cadastro", "Por favor, preencha todos os campos.")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroUsuarios(root)
    root.mainloop()