from copy import deepcopy


class snake_and_ladder:
    def creating_the_table(self, player_position, snake_position, ladder_position):
        count = 100
        table_ = list()
        for row in range(0, 10):
            temp = []
            for _ in range(0, 10):
                temp.append(count)
                count -= 1
            if row % 2 != 0: temp = temp[::-1]
            table_.append(temp)
        # finding the snake and ladder position
        index_ = 1
        for ladder in ladder_position:
            l_stemp = [0, 0]
            for row in range(0, 10):
                for col in range(0, 10):
                    if table_[row][col] == ladder[0]: l_stemp[0] = [row, col]
                    if table_[row][col] == ladder[1]: l_stemp[1] = [row, col]
            ladder_position[index_ - 1] = l_stemp
            index_ += 1
        index_ = 1
        for l_temp in ladder_position:
            table_[l_temp[0][0]][l_temp[0][1]] = f"L{index_}"
            table_[l_temp[1][0]][l_temp[1][1]] = f"L{index_}"
            index_ += 1
        index_ = 1
        for snake in snake_position:
            l_stemp = [0, 0]
            for row in range(0, 10):
                for col in range(0, 10):
                    if table_[row][col] == snake[0]: l_stemp[0] = [row, col]
                    if table_[row][col] == snake[1]: l_stemp[1] = [row, col]
            snake_position[index_ - 1] = l_stemp
            index_ += 1
        index_ = 1
        for s_temp in snake_position:
            table_[s_temp[0][0]][s_temp[0][1]] = f"S{index_}"
            table_[s_temp[1][0]][s_temp[1][1]] = f"S{index_}"
            index_ += 1
        self.main_table = table_
        self.ladder_position = ladder_position
        self.snake_position = snake_position
        self.player_position = player_position

    def check_ladder(self,player_name, position):
        for ladder in self.ladder_position:
            if ladder[1] == position:
                print(f"{player_name} got a golder ladder")
                return ladder[0]
        return position

    def check_snake(self, player_name,position):
        for snake in self.snake_position:
            if snake[0] == position:
                print(f"{player_name} get a bit from snake")
                return snake[1]
        return position

    def __init__(self, player_position, snake_position, ladder_position):
        self.creating_the_table(player_position, snake_position, ladder_position)

    def printing_the_table(self):
        temp_table = deepcopy(self.main_table)
        print(temp_table)
        for player in list(self.player_position.keys()):
            pos_ = temp_table[player_position[player][0]][player_position[player][1]]
            temp_table[player_position[player][0]][player_position[player][1]] = str(temp_table[player_position[player][0]][player_position[player][1]])+" " + f"_{player[0]}_"

        for position_row in temp_table:
            for position_col in position_row: print(str(position_col).center(7), end="")
            print()

    def moving_the_position(self, player_name, move):
        player_detail = deepcopy(self.player_position[player_name])

        if (player_detail[0] == 0):
            if player_detail[1] - move == 0:
                return True
            elif((player_detail[1]-move)>0):
                player_detail[1] -= move
            else:
                print("You doesn't reach the end, Better luck in next try!!!")
                return False
        else:
            for _ in range(0, move):
                if player_detail[0] % 2 == 0:
                    if player_detail[1] == 0:
                        player_detail[0] -= 1
                    else:
                        player_detail[1] -= 1
                else:
                    if player_detail[1] == 9:
                        player_detail[0] -= 1
                    else:
                        player_detail[1] += 1
        player_posi= self.check_ladder(position=player_detail,player_name=player_name)
        player_posi = self.check_snake(position=player_posi,player_name=player_name)
        self.player_position[player_name] = player_posi

        self.printing_the_table()
        return False


if __name__ == "__main__":
    print("Hello Everyone. Are you get ready for a challenge.")
    number_of_player = int(input("Please enter the number of player max '4' min '1': "))
    player_position = {}
    snake_position = [[40, 3], [43, 18], [27, 5], [54, 31], [89, 53], [66, 45], [76, 58], [99, 41]]
    ladder_position = [[25, 4], [46, 13], [49, 33], [69, 50], [63, 42], [81, 62], [92, 74]]
    if (number_of_player < 4 and number_of_player > 0):
        for num in range(number_of_player):
            name = input(f"Enter the name for player {num + 1} : ")
            player_position[name] = [9,0]
        caller = snake_and_ladder(player_position, snake_position, ladder_position)
        caller.printing_the_table()
        while True:
            quit_check = False
            win_check = False
            for player in list(player_position.keys()):
                while True:
                    move = input(f"Currently rolling the die for {player}: ")
                    if move in "quit":
                        quit_check = True
                        break
                    try:
                        move = int(move)
                    except:
                        move=7
                    if move <= 6 and move >= 1: break
                    print("Invalid Input, Please roll the die between 1-6 or Enter 'quit' to quit the game")

                if quit_check: break
                des_ = caller.moving_the_position(player, move)
                if des_:
                    print(f"winner is {player}  ------Game Over------")
                    win_check = True
                    break
                print("-"*100)
            if win_check or quit_check: break
    else:
        print("Invalid Input, please try again!!!")
