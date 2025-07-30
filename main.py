from gacha import pull, ten_pull, get_pity_status
from inventory import show_inventory, trade_up
from wallet import get_balance, spend_coins, add_coins


def main():
    print("🎮 Bem-vindo ao Gacha Simulator: Star Wish!")

    while True:
        pity_5, pity_4 = get_pity_status()
        print(f"\n📊 Pity 5★: {pity_5}/90 | Pity 4★: {pity_4}/10 | 🪙 Saldo: {get_balance()} moedas")

        print("\nMenu:")
        print("1. 1 Pull")
        print("2. 10 Pulls")
        print("3. Ver Inventário")
        print("4. Trade-Up")
        print("5. Sair")
        print("6. Ver Histórico de Pulls")

        choice = input("> ")

        if choice == "1":
            if spend_coins(100):
                print(pull())
            else:
                print("❌ Saldo insuficiente. Precisas de 100 moedas.")
        elif choice == "2":
            if spend_coins(1000):
                results = ten_pull()
                for result in results:
                    print(result)
            else:
                print("❌ Saldo insuficiente. Precisas de 1000 moedas.")
        elif choice == "3":
            show_inventory()
        elif choice == "4":
            rarity = input("Trade-up de que raridade? (3 ou 4): ")
            trade_up(rarity)
        elif choice == "5":
            print("A guardar progresso... Até logo!")
            break
        elif choice == "6":
            from history import show_history
            show_history()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

