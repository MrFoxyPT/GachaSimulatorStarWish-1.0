import json
import os
import random

WALLET_FILE = "wallet.json"

def load_wallet():
    if os.path.exists(WALLET_FILE):
        try:
            with open(WALLET_FILE, "r") as f:
                return json.load(f).get("balance", 0)
        except (json.JSONDecodeError, KeyError):
            return 0
    else:
        save_wallet(5000)  # cria o ficheiro com saldo inicial
        return 5000


def save_wallet(balance):
    with open(WALLET_FILE, "w") as f:
        json.dump({"balance": balance}, f, indent=2)

def get_balance():
    return load_wallet()

def add_coins(amount):
    balance = load_wallet()
    balance += amount
    save_wallet(balance)

def spend_coins(amount):
    balance = load_wallet()
    if balance >= amount:
        balance -= amount
        save_wallet(balance)
        return True
    else:
        return False
