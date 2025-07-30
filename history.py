import json
import os

HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("❌ Erro no histórico. Recriando...")
            return []
    return []


def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def show_history():
    history = load_history()
    if not history:
        print("\n📜 Ainda não tens histórico.")
        return

    print("\n📜 Histórico de Pulls:")
    for entry in history[-20:]:  
        print(f"{entry['timestamp']} - {entry['rarity']}★ {entry['item']}")
