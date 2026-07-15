board = [" " for _ in range(9)]


def show_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_win(player):
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for w in win:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False


def board_full():
    return " " not in board


player = "X"

while True:
    show_board()

    try:
        pos = int(input(f"Player {player} เลือกตำแหน่ง (1-9): ")) - 1
    except ValueError:
        print("กรุณาใส่ตัวเลข")
        continue

    if pos < 0 or pos > 8:
        print("เลือก 1-9 เท่านั้น")
        continue

    if board[pos] != " ":
        print("ช่องนี้ถูกเลือกแล้ว")
        continue

    board[pos] = player

    if check_win(player):
        show_board()
        print(f"🎉 Player {player} ชนะ!")
        break

    if board_full():
        show_board()
        print("เสมอ!")
        break

    player = "O" if player == "X" else "X"
    