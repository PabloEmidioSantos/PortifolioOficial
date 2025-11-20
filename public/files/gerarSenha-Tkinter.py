
#!/usr/bin/env python3
"""
Password Generator - Tkinter GUI version
Author: Pablo (generated)
Description: Simple GUI to generate passwords with options.
"""
import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- core logic ---
LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()_-+=<>?/|{}[]"

def gerar_senha(chars: str, tamanho: int) -> str:
    return ''.join(random.choice(chars) for _ in range(tamanho))

def gerar_segura(tamanho: int) -> str:
    if tamanho < 4:
        raise ValueError("Tamanho mínimo para modo seguro é 4.")
    senha = [random.choice(LETTERS), random.choice(NUMBERS), random.choice(SYMBOLS)]
    all_chars = LETTERS + NUMBERS + SYMBOLS
    senha += [random.choice(all_chars) for _ in range(tamanho - 3)]
    random.shuffle(senha)
    return ''.join(senha)

# --- GUI ---
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("420x320")
        self.resizable(False, False)
        self.configure(bg="#0f0f12")

        # style
        style = ttk.Style(self)
        style.theme_use('default')
        style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=6)
        style.configure('TCheckbutton', background='#0f0f12', foreground='#ffffff')
        style.configure('TLabel', background='#0f0f12', foreground='#ffffff')
        style.configure('TEntry', fieldbackground='#111', foreground='#fff')

        # frame
        frame = ttk.Frame(self, padding=12)
        frame.pack(pady=8, padx=8, fill='both', expand=True)

        title = ttk.Label(frame, text="Gerador de Senhas", font=('Segoe UI', 16, 'bold'), foreground='#9b69ff')
        title.pack(pady=(0,10))

        # tamanho
        tamanho_frame = ttk.Frame(frame)
        tamanho_frame.pack(fill='x', pady=4)
        ttk.Label(tamanho_frame, text="Tamanho:").pack(side='left')
        self.tamanho_var = tk.IntVar(value=12)
        tamanho_spin = ttk.Spinbox(tamanho_frame, from_=4, to=128, textvariable=self.tamanho_var, width=6)
        tamanho_spin.pack(side='left', padx=8)

        # options
        opts = ttk.Frame(frame)
        opts.pack(fill='x', pady=6)
        self.letras_var = tk.BooleanVar(value=True)
        self.numeros_var = tk.BooleanVar(value=True)
        self.simbolos_var = tk.BooleanVar(value=False)
        self.seguro_var = tk.BooleanVar(value=False)

        ttk.Checkbutton(opts, text="Letras", variable=self.letras_var).grid(row=0, column=0, sticky='w')
        ttk.Checkbutton(opts, text="Números", variable=self.numeros_var).grid(row=0, column=1, sticky='w', padx=6)
        ttk.Checkbutton(opts, text="Símbolos", variable=self.simbolos_var).grid(row=0, column=2, sticky='w', padx=6)
        ttk.Checkbutton(opts, text="Modo Seguro", variable=self.seguro_var).grid(row=1, column=0, columnspan=2, sticky='w', pady=6)

        # generate button
        gen_btn = ttk.Button(frame, text="Gerar Senha", command=self.on_gerar)
        gen_btn.pack(fill='x', pady=(6,4))

        # result entry
        self.result_var = tk.StringVar(value="")
        result_entry = ttk.Entry(frame, textvariable=self.result_var, font=('Consolas', 11))
        result_entry.pack(fill='x', pady=(6,0))

        # actions
        action_frame = ttk.Frame(frame)
        action_frame.pack(fill='x', pady=8)
        copy_btn = ttk.Button(action_frame, text="Copiar para área de transferência", command=self.copiar)
        copy_btn.pack(fill='x')

        # footer
        footer = ttk.Label(frame, text="Feito por Pablo — Password Generator", font=('Segoe UI', 8))
        footer.pack(pady=(10,0))

    def on_gerar(self):
        tamanho = int(self.tamanho_var.get())
        usar_letras = self.letras_var.get()
        usar_numeros = self.numeros_var.get()
        usar_simbolos = self.simbolos_var.get()
        modo_seguro = self.seguro_var.get()

        try:
            if modo_seguro:
                senha = gerar_segura(tamanho)
            else:
                chars = ''
                if usar_letras:
                    chars += LETTERS
                if usar_numeros:
                    chars += NUMBERS
                if usar_simbolos:
                    chars += SYMBOLS
                if not chars:
                    messagebox.showwarning("Atenção", "Selecione pelo menos uma categoria de caracteres.")
                    return
                senha = gerar_senha(chars, tamanho)
            self.result_var.set(senha)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def copiar(self):
        txt = self.result_var.get()
        if not txt:
            messagebox.showinfo("Info", "Nada para copiar.")
            return
        self.clipboard_clear()
        self.clipboard_append(txt)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência.")

if __name__ == '__main__':
    app = App()
    app.mainloop()
