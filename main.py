row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
game_matrix = [row1, row2, row3]
game_on = True
user1_mark = "O"
user2_mark = "X"


def print_game():
    print(f"{row1[0]}|{row1[1]}|{row1[2]}|")
    print("------")
    print(f"{row2[0]}|{row2[1]}|{row2[2]}|")
    print("------")
    print(f"{row3[0]}|{row3[1]}|{row3[2]}|")


row_status = False
column_status = False
diagonal_status = False
user1_turn = True
empty_status = False
game_won = False


def check_row():
    global row_status, game_on, game_won
    for row in game_matrix:
        for element in row:
            if element == row[0] and element != " ":
                row_status = True
            else:
                row_status = False
        if row_status:
           # print("Game Won")
            game_won = True
            game_on = False


def check_column():
    global column_status, game_on, game_won
    for i in range(0, 3):
        if row1[i] == row2[i] and row1[i] == row3[i] and row1[i] != " ":
            column_status = True
    if column_status:
        # print("Game Won")
        game_won = True
        game_on = False


def check_diagonal():
    global diagonal_status, game_on, game_won
    if row1[0] == row2[1] and row1[0] == row3[2] and row1[0] != " ":
        diagonal_status = True
    if row1[2] == row2[1] and row2[2] == row3[0] and row1[2] != " ":
        diagonal_status = True
    if diagonal_status:
        # print("Game Won")
        game_won = True
        game_on = False


def check_empty():
    global empty_status, game_on, game_won
    for row in game_matrix:
        if " " not in row:
            empty_status = True
        if " " in row:
            empty_status = False
    if empty_status:
        game_on = False
        if not game_won:
            print("Tie!")


def check_game_win():
    check_row()
    check_column()
    check_diagonal()
    check_empty()
    if not game_on:
        if not game_won:
            print("Tie!")
        else:
            print("Game Won")


while game_on:
    if user1_turn:
        user_mark = user1_mark
        user1_turn = False
    else:
        user_mark = user2_mark
        user1_turn = True
    user_input = input(f"Enter where you want to place {user_mark}:")
    if game_matrix[int(user_input[0])-1][int(user_input[1])-1] == " ":
        game_matrix[int(user_input[0])-1][int(user_input[1])-1] = user_mark
    print_game()
    check_game_win()
