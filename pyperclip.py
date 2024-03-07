import tkinter as tk
from tkinter import ttk

def copy_text(text):
    root.clipboard_clear()
    root.clipboard_append(text)

root = tk.Tk()
root.title("copiar.py")

# Função para copiar o texto de cada caixa
def copy_text_box1():
    copy_text(text_box1.get("1.0", "end-1c"))

def copy_text_box2():
    copy_text(text_box2.get("1.0", "end-1c"))

def copy_text_box3():
    copy_text(text_box3.get("1.0", "end-1c"))

def copy_text_box4():
    copy_text(text_box4.get("1.0", "end-1c"))

def copy_text_box5():
    copy_text(text_box5.get("1.0", "end-1c"))

def copy_text_box6():
    copy_text(text_box6.get("1.0", "end-1c"))

def copy_text_box7():
    copy_text(text_box7.get("1.0", "end-1c"))

def copy_text_box8():
    copy_text(text_box8.get("1.0", "end-1c"))

# Criando as caixas de texto
text_box1 = tk.Text(root, height=3, width=20)
text_box1.grid(row=0, column=0, padx=5, pady=5)

text_box2 = tk.Text(root, height=3, width=20)
text_box2.grid(row=1, column=0, padx=5, pady=5)

text_box3 = tk.Text(root, height=3, width=20)
text_box3.grid(row=2, column=0, padx=5, pady=5)

text_box4 = tk.Text(root, height=3, width=20)
text_box4.grid(row=3, column=0, padx=5, pady=5)

text_box5 = tk.Text(root, height=3, width=20)
text_box5.grid(row=4, column=0, padx=5, pady=5)

text_box6 = tk.Text(root, height=3, width=20)
text_box6.grid(row=5, column=0, padx=5, pady=5)

text_box7 = tk.Text(root, height=3, width=20)
text_box7.grid(row=6, column=0, padx=5, pady=5)

text_box8 = tk.Text(root, height=3, width=20)
text_box8.grid(row=7, column=0, padx=5, pady=5)

# Criando os botões de cópia
copy_button1 = ttk.Button(root, text="Copiar", command=copy_text_box1)
copy_button1.grid(row=0, column=1, padx=5, pady=5)

copy_button2 = ttk.Button(root, text="Copiar", command=copy_text_box2)
copy_button2.grid(row=1, column=1, padx=5, pady=5)

copy_button3 = ttk.Button(root, text="Copiar", command=copy_text_box3)
copy_button3.grid(row=2, column=1, padx=5, pady=5)

copy_button4 = ttk.Button(root, text="Copiar", command=copy_text_box4)
copy_button4.grid(row=3, column=1, padx=5, pady=5)

copy_button5 = ttk.Button(root, text="Copiar", command=copy_text_box5)
copy_button5.grid(row=4, column=1, padx=5, pady=5)

copy_button6 = ttk.Button(root, text="Copiar", command=copy_text_box6)
copy_button6.grid(row=5, column=1, padx=5, pady=5)

copy_button7 = ttk.Button(root, text="Copiar", command=copy_text_box7)
copy_button7.grid(row=6, column=1, padx=5, pady=5)

copy_button8 = ttk.Button(root, text="Copiar", command=copy_text_box8)
copy_button8.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()
