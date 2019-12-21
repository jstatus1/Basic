game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print(id(game))
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
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
        

print("Initial GameBoard")
game_board(game)

print("Player 2 Made A Move")
game_board(game_board, player=2, row=3, column=0)



