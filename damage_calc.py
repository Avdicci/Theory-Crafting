import os
from colorama import init, Fore
from damage_functions import damage_calculators  # Import dictionary

init(autoreset=True)

def main():
    while True:
        os.system("cls")  # Clear screen
        print("Select an option:")
        print("[1] Calculate Damage of a class")
        print("[2] To be continued")
        print("[3] Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("cls")
            print("Choose a class:")
            print("[1] Assassin")
            print("[2] Bishop")
            print("[3] Dark Knight")
            print("[4] Swan")
            class_choice = input("Enter your choice: ")

            try:
                level = int(input("Enter player level: "))
                damage = int(input("Enter base damage: "))
                hp = int(input("Enter HP: "))
                energy = int(input("Enter Energy: "))
                final_damage = float(input("Enter Final Damage Multiplier (e.g., 1.05 for 5% extra): "))
                seconds_per_hit = float(input("Enter seconds per hit: "))

                if class_choice in damage_calculators:
                    final_dmg = damage_calculators[class_choice](level, damage, hp, energy, final_damage)
                else:
                    print("Invalid choice. Returning to menu.")
                    continue

                damage_per_minute = (final_dmg * 60) / seconds_per_hit
                os.system("cls")
                print(Fore.CYAN + "Final Damage: " + Fore.YELLOW + f"{final_dmg:,.2f}")
                print(Fore.CYAN + "Damage per Minute: " + Fore.YELLOW + f"{damage_per_minute:,.2f}")
                input("\nPress Enter to return to the menu...")

            except ValueError:
                print("Invalid input! Please enter numbers only.")
                input("\nPress Enter to return to the menu...")

        elif choice == "2":
            os.system("cls")
            print("Feature coming soon!")
            input("\nPress Enter to return to the menu...")
        elif choice == "3":
            os.system("cls")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
