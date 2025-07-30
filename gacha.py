import random
import json
import os
from datetime import datetime
from items import items_by_rarity, rarity_probabilities
from inventory import add_item
from wallet import add_coins
from history import save_history

STATE_FILE = "pity_state.json"

def load_pity_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
            return data.get("since_5", 0), data.get("since_4", 0)
    else:
        return 0, 0

def save_pity_state(since_5, since_4):
    with open(STATE_FILE, "w") as f:
        json.dump({"since_5": since_5, "since_4": since_4}, f)

pulls_since_last_5, pulls_since_last_4 = load_pity_state()

def get_pity_status():
    return pulls_since_last_5, pulls_since_last_4

def pull():
    global pulls_since_last_5, pulls_since_last_4

    if pulls_since_last_5 >= 89:
        rarity = "5"
    elif pulls_since_last_4 >= 9:
        rarity = "4"
    else:
        roll = random.random()
        if roll <= rarity_probabilities["5"]:
            rarity = "5"
        elif roll <= rarity_probabilities["5"] + rarity_probabilities["4"]:
            rarity = "4"
        else:
            rarity = "3"

    item = random.choice(items_by_rarity[rarity])

    if rarity == "5":
        pulls_since_last_5 = 0
        pulls_since_last_4 = 0
    elif rarity == "4":
        pulls_since_last_4 = 0
        pulls_since_last_5 += 1
    else:
        pulls_since_last_5 += 1
        pulls_since_last_4 += 1

    save_pity_state(pulls_since_last_5, pulls_since_last_4)

    add_item(item)
    save_history({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rarity": rarity,
        "item": item
    })

    if random.random() < 0.1:
        bonus = random.randint(50, 200)
        add_coins(bonus)
        print(f"💰 Bónus: Ganhaste {bonus} moedas!")

    return f"{rarity}★ - {item}"

def ten_pull():
    return [pull() for _ in range(10)]
