import tkinter as tk
import time
import winsound


def iniciar_pomodoro(foco, pausa):
    contagem_regressiva(foco * 60)
    contagem_regressiva(pausa * 60)

def contagem_regressiva(segundos):
    while segundos >= 0:
        minutos = segundos // 60
        seg = segundos % 60
        tempo_formatado = f"{minutos:02d}:{seg:02d}"
        label.config(text=tempo_formatado)
        janela.update()
        time.sleep(1)
        segundos -= 1
    som()

def editar_tempos():
    foco_texto = entry_foco.get()
    pausa_texto = entry_pausa.get()

    if foco_texto.isdigit() and pausa_texto.isdigit():
        foco = int(foco_texto)
        pausa = int(pausa_texto)
        iniciar_pomodoro(foco, pausa)
    else:
        label.config(text="Apenas números, por favor!")

def mostrar_campos():
    label_foco.place(relx=0.5, rely=0.65, anchor="center")
    entry_foco.place(relx=0.5, rely=0.7, anchor="center")
    label_pausa.place(relx=0.5, rely=0.75, anchor="center")
    entry_pausa.place(relx=0.5, rely=0.8, anchor="center")
    btn_confirmar.place(relx=0.5, rely=0.88, anchor="center")


#Aqui é o som emitido
def som():
    for _ in range (5):
        winsound.Beep(1000,500)
        time.sleep(0.0001)

### Interface:
janela = tk.Tk()
janela.title("Interface")
janela.geometry("600x400")
janela.configure(bg="lightpink")

entry_foco = tk.Entry(janela)
entry_pausa = tk.Entry(janela)
label_foco = tk.Label(janela, text="Minutos de foco:", bg="lightpink")
label_pausa = tk.Label(janela, text="Minutos de pausa:", bg="lightpink")
btn_confirmar = tk.Button(janela, text="Confirmar", command=editar_tempos)

label = tk.Label(janela, text="Escolha a duração desejada:", font=("Comic Sans MS", 15, "bold"), bg="lightpink")
label.place(relx=0.5, rely=0.35, anchor="center")

def clicar():
    label.config()

frame_botoes = tk.Frame(janela, bg="lightpink")
frame_botoes.place(relx=0.5, rely=0.55, anchor="center")

btn1 = tk.Button(frame_botoes, text="25 x 5",command=lambda: iniciar_pomodoro(25, 5))
btn1.pack(side="left", padx=10)
btn2 = tk.Button(frame_botoes, text="30 x 10", command=lambda: iniciar_pomodoro(30, 10))
btn2.pack(side="left", padx=10)
btn3 = tk.Button(frame_botoes, text="EDITAR", command=mostrar_campos)
btn3.pack(side="left", padx=10)

janela.mainloop()