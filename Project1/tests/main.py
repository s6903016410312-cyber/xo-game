from src.calpkg.calculater import run_calculator
from src.gamepkg.game import run_game


def main():

    while True:

        print("\n========== MENU ==========")
        print("1. Calculator")
        print("2. Tic Tac Toe")
        print("3. Exit")

        choice = input("เลือกเมนู : ")

        if choice == "1":
            run_calculator()

        elif choice == "2":
            run_game()

        elif choice == "3":
            print("ลาก่อน")
            break

        else:
            print("กรุณาเลือกใหม่")


if __name__ == "__main__":
    main()