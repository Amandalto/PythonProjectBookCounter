import tkinter as tk
from unittest.mock import DEFAULT

# Criar a janela
app = tk.Tk()
app.title("Contador de Livros")
app.geometry("600x650")

#Label Título
rotulo = tk.Label(app, text = "Bem-Vindo(a) ao Memórias de um Leitor", font=("Arial",14, "bold"), fg="white", bg="purple")
rotulo.pack(pady=20)

# ---------- Variável Contador de Livros ----------

quantidade_livros = 0
contador_var = tk.StringVar()
contador_var.set(f"Livros cadastrados: {quantidade_livros}")

# ---------- CAMPOS E RÓTULOS ----------
tk.Label(app, text="Título do Livro:").pack()
entry_titulo = tk.Entry(app, width=40)
entry_titulo.pack(pady=5)

tk.Label(app, text="Autor:").pack()
entry_autor = tk.Entry(app, width=40)
entry_autor.pack(pady=5)

tk.Label(app, text="Ano:").pack()
entry_ano = tk.Entry(app, width=40)
entry_ano.pack(pady=5)

# ---------- CAIXA DE EXIBIÇÃO ----------
caixa_resultado = tk.Text(app, height=15, width=45, font=("Arial", 12), bg="#f0f0f0", fg="black")
caixa_resultado.pack(pady=10)

# ---------- CONTADOR VISUAL ----------
tk.Label(app, textvariable=contador_var,font=("Arial", 11, "bold"), fg="darkblue").pack(pady=5)

# ---------- FUNÇÃO EXIBIR LIVRO ----------
def exibir_livro():
    global quantidade_livros
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()

    if titulo and autor and ano:
        livro_formatado = f"Título: {titulo}\nAutor: {autor}\nAno: {ano}\n---\n"
        caixa_resultado.insert(tk.END, livro_formatado)
        quantidade_livros += 1
        contador_var.set(f"Livros cadastrados: {quantidade_livros}")
        limpar_campos()
    else:
        caixa_resultado.insert(tk.END, "⚠️ Preencha todos os campos!\n\n")

def limpar_campos():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_ano.delete(0, tk.END)


# ---------- FUNÇÃO EXCLUIR LIVRO ----------
def limpar_lista ():
    caixa_resultado.delete("1.0", tk.END) #apaga a lista completa


# ---------- BOTÕES ----------
# Frame para alinhar os botões lado a lado
frame_botoes = tk.Frame(app)
frame_botoes.pack(pady=5)

tk.Button(frame_botoes, text="Cadastrar Livro", command=exibir_livro, width=18).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Limpar Lista", command=limpar_lista, width=18).pack(side="left", padx=5)

# ---------- EXECUTAR ----------
app.mainloop()
