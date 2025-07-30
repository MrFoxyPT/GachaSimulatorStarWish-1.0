import json
import os
from datetime import datetime, timedelta
from wallet import add_coins

BONUS_FILE = "bonus.json"

def load_bonus_data():
    if os.path.exists(BONUS_FILE):
        try:
            with open(BONUS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("❌ Erro no ficheiro de bónus. Recriando...")
            return {}
    else:
        return {}


def save_bonus_data(data):
    with open(BONUS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def claim_bonus(tipo):
    now = datetime.now()
    data = load_bonus_data()

    last_claim_str = data.get(tipo)
    if last_claim_str:
        last_claim = datetime.fromisoformat(last_claim_str)
    else:
        last_claim = None

    can_claim = False

    if tipo == "daily":
        can_claim = last_claim is None or now.date() > last_claim.date()
        recompensa = 250
    elif tipo == "weekly":
        can_claim = last_claim is None or now.isocalendar()[1] > last_claim.isocalendar()[1]
        recompensa = 1000
    elif tipo == "monthly":
        can_claim = last_claim is None or now.month > last_claim.month or now.year > last_claim.year
        recompensa = 2500
    elif tipo == "hourly":
        can_claim = last_claim is None or now - last_claim >= timedelta(hours=1)
        recompensa = 100

    if can_claim:
        data[tipo] = now.isoformat()
        save_bonus_data(data)
        add_coins(recompensa)
        return True, recompensa
    else:
        return False, 0
