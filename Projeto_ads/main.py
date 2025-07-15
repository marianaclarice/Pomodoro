import tkinter as tk

#Aqui será a Lógica do Pomodoro

#Aqui será a Funçao contagem regressiva

#Aqui será a Função do Editar


### Interface:
janela = tk.Tk()
janela.title("Interface")
janela.geometry("500x300")
janela.configure(bg="lightblue")

label = tk.Label(janela, text="Escolha a duração desejada:", font=("Lucida console", 13, "bold"), bg="lightblue")
label.place(relx=0.5, rely=0.35, anchor="center")

def clicar():
    label.config(text="Você clicou!")

frame_botoes = tk.Frame(janela, bg="lightblue")
frame_botoes.place(relx=0.5, rely=0.55, anchor="center")

btn1 = tk.Button(frame_botoes, text="25 x 5")
btn1.pack(side="left", padx=10)
btn2 = tk.Button(frame_botoes, text="30 x 10")
btn2.pack(side="left", padx=10)
btn3 = tk.Button(frame_botoes, text="EDITAR")
btn3.pack(side="left", padx=10)

#Aqui será a Logica do botao 3 de editar

janela.mainloop()