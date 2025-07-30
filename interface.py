import tkinter as tk
from gacha import pull, ten_pull
from wallet import get_balance, spend_coins
from inventory import load_inventory, trade_up, sell_item
from history import load_history
from bonus import claim_bonus
from lang import t, toggle_lang

# --- Funções auxiliares ---
def mostrar_resultados_pull(resultados):
    janela_resultados = tk.Toplevel(janela)
    janela_resultados.title("🎁 Resultados da Pull")
    janela_resultados.geometry("300x300")

    tk.Label(janela_resultados, text="Resultados:", font=("Arial", 14)).pack(pady=10)

    if isinstance(resultados, list):
        for r in resultados:
            tk.Label(janela_resultados, text=r, font=("Arial", 11)).pack()
    else:
        tk.Label(janela_resultados, text=resultados, font=("Arial", 11)).pack()

def realizar_pull():
    if spend_coins(100):
        resultado = pull()
        mostrar_resultados_pull(resultado)
        atualizar_saldo()
    else:
        resultado_label.config(text="❌ Saldo insuficiente.")

def realizar_10_pulls():
    if spend_coins(1000):
        resultados = ten_pull()
        mostrar_resultados_pull(resultados)
        atualizar_saldo()
    else:
        resultado_label.config(text="❌ Saldo insuficiente.")

def atualizar_saldo():
    saldo_label.config(text=t("saldo", moedas=get_balance()))

def abrir_inventario():
    inventario = load_inventory()
    inv_janela = tk.Toplevel(janela)
    inv_janela.title(t("inventario_titulo"))

    tk.Label(inv_janela, text=t("inventario_label"), font=("Arial", 14)).pack(pady=5)

    for item, quantidade in inventario.items():
        if quantidade > 0:
            frame = tk.Frame(inv_janela)
            frame.pack(pady=2, fill="x", padx=10)

            tk.Label(frame, text=f"{item}: x{quantidade}", width=25, anchor="w").pack(side="left")

            def vender_item(i=item):
                sucesso, valor = sell_item(i, 1)
                if sucesso:
                    inv_janela.destroy()
                    abrir_inventario()
                    atualizar_saldo()

            tk.Button(frame, text=t("vender_1"), command=vender_item).pack(side="right")

    def fazer_tradeup_3():
        trade_up("3")
        inv_janela.destroy()
        abrir_inventario()

    def fazer_tradeup_4():
        trade_up("4")
        inv_janela.destroy()
        abrir_inventario()

    tk.Button(inv_janela, text=t("tradeup_3"), command=fazer_tradeup_3).pack(pady=5)
    tk.Button(inv_janela, text=t("tradeup_4"), command=fazer_tradeup_4).pack(pady=5)

def abrir_historico():
    historico = load_history()
    hist_janela = tk.Toplevel(janela)
    hist_janela.title(t("historico_titulo"))
    hist_janela.geometry("400x400")

    canvas = tk.Canvas(hist_janela)
    scrollbar = tk.Scrollbar(hist_janela, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scroll_frame, text=t("historico_label"), font=("Arial", 14)).pack(pady=5)

    for entry in reversed(historico):
        texto = f"{entry['timestamp']} - {entry['rarity']}★ {entry['item']}"
        tk.Label(scroll_frame, text=texto, font=("Arial", 10), anchor="w").pack(fill="x", padx=10)

def tentar_claim(tipo):
    sucesso, recompensa = claim_bonus(tipo)
    if sucesso:
        resultado_label.config(text=t("bonus_recebido", tipo=tipo.title(), recompensa=recompensa))
        atualizar_saldo()
    else:
        resultado_label.config(text=t("bonus_ja_recebido", tipo=tipo.title()))


def alternar_idioma():
    toggle_lang()
    atualizar_textos()

def atualizar_textos():
    saldo_label.config(text=t("saldo", moedas=get_balance()))
    botao_idioma.config(text=t("trocar_idioma"))
    botao_pull1.config(text=t("pull_1"))
    botao_pull10.config(text=t("pull_10"))
    botao_inv.config(text=t("ver_inventario"))
    botao_hist.config(text=t("ver_historico"))
    bonus_label.config(text=t("bonus_label"))
    botao_daily.config(text=t("daily"))
    botao_weekly.config(text=t("weekly"))
    botao_monthly.config(text=t("monthly"))
    botao_hourly.config(text=t("hourly"))

# --- Interface principal ---
janela = tk.Tk()
janela.title("Gacha Simulator: Star Wish")
janela.geometry("400x550")
janela.resizable(False, False)

canvas = tk.Canvas(janela)
scrollbar = tk.Scrollbar(janela, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

conteudo = tk.Frame(canvas, width=350)
conteudo.pack_propagate(False)
canvas.create_window((200, 0), window=conteudo, anchor="n")
conteudo.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Widgets
row = 0

titulo = tk.Label(conteudo, text=t("titulo_principal"), font=("Arial", 16, "bold"))
titulo.grid(row=row, column=0, pady=10); row += 1

botao_pull1 = tk.Button(conteudo, text=t("pull_1"), width=25, command=realizar_pull)
botao_pull1.grid(row=row, column=0, pady=5); row += 1

botao_pull10 = tk.Button(conteudo, text=t("pull_10"), width=25, command=realizar_10_pulls)
botao_pull10.grid(row=row, column=0, pady=5); row += 1

botao_inv = tk.Button(conteudo, text=t("ver_inventario"), width=25, command=abrir_inventario)
botao_inv.grid(row=row, column=0, pady=5); row += 1

botao_hist = tk.Button(conteudo, text=t("ver_historico"), width=25, command=abrir_historico)
botao_hist.grid(row=row, column=0, pady=5); row += 1

resultado_label = tk.Label(conteudo, text="", font=("Arial", 12), justify="center", wraplength=330)
resultado_label.grid(row=row, column=0, pady=10); row += 1

saldo_label = tk.Label(conteudo, text=t("saldo", moedas=get_balance()), font=("Arial", 12))
saldo_label.grid(row=row, column=0, pady=5); row += 1

botao_idioma = tk.Button(conteudo, text=t("trocar_idioma"), width=25, command=alternar_idioma)
botao_idioma.grid(row=row, column=0, pady=(0, 10)); row += 1

bonus_label = tk.Label(conteudo, text=t("bonus_label"), font=("Arial", 12, "bold"))
bonus_label.grid(row=row, column=0, pady=(10, 0)); row += 1

botao_daily = tk.Button(conteudo, text=t("daily"), width=20, command=lambda: tentar_claim("daily"))
botao_daily.grid(row=row, column=0, pady=2); row += 1

botao_weekly = tk.Button(conteudo, text=t("weekly"), width=20, command=lambda: tentar_claim("weekly"))
botao_weekly.grid(row=row, column=0, pady=2); row += 1

botao_monthly = tk.Button(conteudo, text=t("monthly"), width=20, command=lambda: tentar_claim("monthly"))
botao_monthly.grid(row=row, column=0, pady=2); row += 1

botao_hourly = tk.Button(conteudo, text=t("hourly"), width=20, command=lambda: tentar_claim("hourly"))
botao_hourly.grid(row=row, column=0, pady=2); row += 1

conteudo.grid_columnconfigure(0, weight=1)

janela.mainloop()
