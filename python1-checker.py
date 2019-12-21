import itertools

def win(current_game):
    # horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally!")
    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically!")

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} has won Diagonally (/)")

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} has won Diagonally (\\)")


def game_board(game_map, player=0, row=0, column=0, just_display=False):

    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Please Choose antoher")
            return False

        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return False
    
    except Exception as e:
        print(str(e))
        return False

play = True
player = itertools.cycle([1, 2])

while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game = game_board(game, just_display=True)
    while not game_won:
        current_player =next(player)

        played = False

        while not played:  
            column_choice = input("What column do you want to play? (0, 1, 2):")
            row_choice = input("What row do you want to play? (0, 1, 2): ")
            game = game_board(game, current_player, int(row_choice), int(column_choice))
            if game:
                played = True

#game = game_board(game, player=1, row=3, column=1)