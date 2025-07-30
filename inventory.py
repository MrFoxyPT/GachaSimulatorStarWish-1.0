import json
import os
from items import items_by_rarity
from wallet import add_coins

INVENTORY_FILE = "inventory.json"

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as f:
            return json.load(f)
    else:
        return {item: 0 for rarity in items_by_rarity for item in items_by_rarity[rarity]}

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=2)

def add_item(item):
    inventory = load_inventory()
    inventory[item] += 1
    save_inventory(inventory)

def show_inventory():
    inventory = load_inventory()
    print("\n🎒 Teu Inventário:")
    for item, count in inventory.items():
        if count > 0:
            print(f"{item}: x{count}")

def trade_up(rarity):
    if rarity not in ["3", "4"]:
        print("Só é possível fazer trade-up de 3★ para 4★ ou 4★ para 5★.")
        return

    inventory = load_inventory()
    lower_items = items_by_rarity[rarity]
    next_rarity = str(int(rarity) + 1)
    higher_items = items_by_rarity[next_rarity]

    total = sum(inventory[item] for item in lower_items)

    if total < 10:
        print(f"❌ Precisas de pelo menos 10 itens {rarity}★ para fazer trade-up.")
        return

    to_remove = 10
    for item in lower_items:
        while inventory[item] > 0 and to_remove > 0:
            inventory[item] -= 1
            to_remove -= 1

    from random import choice
    result = choice(higher_items)
    inventory[result] += 1
    save_inventory(inventory)
    print(f"✅ Fizeste trade-up com sucesso! Obtiveste: {next_rarity}★ - {result}")

sell_values = {
    "3": 25,
    "4": 100,
    "5": 1000
}

def sell_item(item, quantity):
    inventory = load_inventory()

    if item not in inventory or inventory[item] < quantity:
        print(f"❌ Não tens {quantity}x {item} para vender.")
        return False, 0

    # Descobrir raridade
    rarity = None
    for r, items in items_by_rarity.items():
        if item in items:
            rarity = r
            break

    if rarity is None:
        print("❌ Raridade não encontrada.")
        return False, 0

    value = sell_values[rarity] * quantity
    inventory[item] -= quantity
    save_inventory(inventory)
    add_coins(value)
    print(f"✅ Vendeste {quantity}x {item} por {value} moedas.")
    return True, value
