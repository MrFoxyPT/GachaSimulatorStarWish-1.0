# lang.py

translations = {
    "pt": {
        "saldo": "🪙 Saldo: {moedas} moedas",
        "trocar_idioma": "🌐 Mudar para English",
        "titulo_principal": "🌠 Gacha Simulator",
        "ver_inventario": "🎒 Ver Inventário",
        "ver_historico": "📜 Ver Histórico",
        "pull_1": "✨ 1 Pull (100 moedas)",
        "pull_10": "💫 10 Pulls (1000 moedas)",
        "bonus_label": "🎁 Bónus:",
        "daily": "Bónus Diário",
        "weekly": "Bónus Semanal",
        "monthly": "Bónus Mensal",
        "hourly": "Bónus de Hora",
        "inventario_titulo": "🎒 Inventário",
        "inventario_label": "Teus Itens:",
        "vender_1": "💰 Vender 1",
        "tradeup_3": "🔁 Trade-up 10x 3★ ➜ 4★",
        "tradeup_4": "🔁 Trade-up 10x 4★ ➜ 5★",
        "historico_titulo": "📜 Histórico de Pulls",
        "historico_label": "Últimos Pulls:",
        "bonus_recebido": "🎁 Bónus {tipo}: +{recompensa} moedas!",
        "bonus_ja_recebido": "❌ Já recebeste o bónus {tipo}."
    },
    "en": {
        "saldo": "🪙 Balance: {moedas} coins",
        "trocar_idioma": "🌐 Switch to Portuguese",
        "titulo_principal": "🌠 Gacha Simulator",
        "ver_inventario": "🎒 View Inventory",
        "ver_historico": "📜 View History",
        "pull_1": "✨ 1 Pull (100 coins)",
        "pull_10": "💫 10 Pulls (1000 coins)",
        "bonus_label": "🎁 Bonus:",
        "daily": "Daily Bonus",
        "weekly": "Weekly Bonus",
        "monthly": "Monthly Bonus",
        "hourly": "Hourly Bonus",
        "inventario_titulo": "🎒 Inventory",
        "inventario_label": "Your Items:",
        "vender_1": "💰 Sell 1",
        "tradeup_3": "🔁 Trade-up 10x 3★ ➜ 4★",
        "tradeup_4": "🔁 Trade-up 10x 4★ ➜ 5★",
        "historico_titulo": "📜 Pull History",
        "historico_label": "Latest Pulls:",
        "bonus_recebido": "🎁 {tipo} bonus: +{recompensa} coins!",
        "bonus_ja_recebido": "❌ You already claimed the {tipo} bonus."
    }
}


current_lang = "pt"

def t(key, **kwargs):
    text = translations.get(current_lang, {}).get(key, key)
    return text.format(**kwargs)

def toggle_lang():
    global current_lang
    current_lang = "en" if current_lang == "pt" else "pt"
