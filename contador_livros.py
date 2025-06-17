import tkinter as tk

# Criando a janela principal
app = tk.Tk()
app.title("Contador de Livros") #Título
app.geometry("800x600")  # Largura x Altura



#Label Título
rotulo = tk.Label(app, text = "Bem-Vindo(a) ao Memórias de um Leitor", font=("Arial",14, "bold"), fg="white", bg="purple")
rotulo.pack(pady=20)

#Campo de entrada
entrada = tk.Entry(app, width=30)
entrada.pack(pady=5)

#Botão

# Executando a interface
app.mainloop()