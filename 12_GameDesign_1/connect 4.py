grid = [
    ["1", "2", "3", "4", "5", "6", "7"],    # [R0C0, ..., R0C6]
    ["8", "9", "10", "11", "12", "13", "14"],    # [R1C0, R1C1, R1C2]
    ["15", "16", "17", "18", "19", "20", "21"],  
    ["22", "23", "24", "25", "26", "27", "28"],
    ["29", "30", "31", "32", "33", "34", "35"],
    ["36", "37", "38", "39", "40", "41", "42"],   # [R5C0, ..., R5C6]
]

current_piece = "R"
last_row = -1
last_col = -1
left_diag = +1
right_diag = +1
remaining_spots = 42

def print_grid():
    for I in range (7):
        print(I, end=" ")

    print()   

    for row in range(6):
        for col in range(7):
            if col != 6:
                print(grid[row][col], end="  ")            
            else:
                print(grid[row][col])
                print()

def is_bad_num_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 0 and int(choice) <= 6):
        return False
    return True
                
def is_bad_choice(choice : str):
    if(choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)

    
def place_piece(col : int):
     global last_row
     global last_col
     global remaining_spots
     while(True):
        row = 5
        while(row >= 0):
            if grid[row][col].__eq__("-"):
                grid[row][col] = current_piece
                last_row = row
                last_col = col
                remaining_spots -=1
                break
            else:
                row -= 1
        if row != -1:
            break
        else:
            user_choice = ""
            while ( is_bad_num_string(user_choice)):
                user_choice = input("Enter a number (0-6) where to drop the piece:")
                col = int(user_choice)


def check_row():
    first_list = [last_col, last_col + 1, last_col + 2, last_col + 3]
    second_list = [last_col - 1, last_col, last_col , last_col + 2]
    third_list = [last_col - 2, last_col - 1, last_col , last_col + 1]
    fourth_list = [last_col - 3, last_col - 2, last_col - 1 , last_col]
    if(first_list[ 0] >=0 and first_list[0] <7 and first_list[3] >= 0 and first_list[3 < 7]):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        four = grid[last_row][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(second_list[ 0] >=0 and first_list[0] <7 and first_list[3] >= 0 and first_list[3 < 7]):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        four = grid[last_row][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(third_list[ 0] >=0 and first_list[0] <7 and first_list[3] >= 0 and first_list[3 < 7]):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        four = grid[last_row][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True 

    if(fourth_list[ 0] >=0 and first_list[0] <7 and first_list[3] >= 0 and first_list[3 < 7]):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        four = grid[last_row][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True               

def check_col():
    first_list = [last_col, last_col + 1, last_col + 2, last_col + 3]
    second_list = [last_col - 1, last_col, last_col , last_col + 2]
    third_list = [last_col - 2, last_col - 1, last_col , last_col + 1]
    fourth_list = [last_col - 3, last_col - 2, last_col - 1 , last_col]
    if(first_list[ 0] >=0 and first_list[0] <6 and first_list[3] >= 0 and first_list[3 < 6]):
        one = grid[last_col][first_list[0]]
        two = grid[last_col][first_list[1]]
        three = grid[last_col][first_list[2]]
        four = grid[last_col][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(second_list[ 0] >=0 and first_list[0] <6 and first_list[3] >= 0 and first_list[3 < 6]):
        one = grid[last_col][first_list[0]]
        two = grid[last_col][first_list[1]]
        three = grid[last_col][first_list[2]]
        four = grid[last_col][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(third_list[ 0] >=0 and first_list[0] <6 and first_list[3] >= 0 and first_list[3 < 6]):
        one = grid[last_col][first_list[0]]
        two = grid[last_col][first_list[1]]
        three = grid[last_col][first_list[2]]
        four = grid[last_col][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True 

    if(fourth_list[ 0] >=0 and first_list[0] <6 and first_list[3] >= 0 and first_list[3 < 6]):
        one = grid[last_col][first_list[0]]
        two = grid[last_col][first_list[1]]
        three = grid[last_col][first_list[2]]
        four = grid[last_col][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):

def check_left_diag():
    check_row()
    first_list = [last_col, last_col + 1, last_col + 2, last_col + 3]
    second_list = [last_col - 1, last_col, last_col + 1, last_col + 2]
    third_list = [last_col - 2, last_col - 1, last_col, last_col + 1]
    fourth_list = [last_col - 3, last_col - 2, last_col - 1, last_col]
    if(first_list[0] >= 0 and first_list[0] < 6 and first_list[3] >= 0 and first_list[3] < 6):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        four = grid[last_row][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (second_list[0] >= 0 and second_list[0] < 6 and second_list[3] >= 0 and second_list[3] < 6):
        one = grid[last_row][second_list[0]]
        two = grid[last_row][second_list[1]]
        three = grid[last_row][second_list[2]]
        four = grid[last_row][second_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (third_list[0] >= 0 and third_list[0] < 6 and third_list[3] >= 0 and third_list[3] < 6):
        one = grid[last_row][third_list[0]]
        two = grid[last_row][third_list[1]]
        three = grid[last_row][third_list[2]]
        four = grid[last_row][third_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (fourth_list[0] >= 0 and fourth_list[0] < 6 and fourth_list[3] >= 0 and fourth_list[3] < 6):
        one = grid[last_row][fourth_list[0]]
        two = grid[last_row][fourth_list[1]]
        three = grid[last_row][fourth_list[2]]
        four = grid[last_row][fourth_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    check_col()
    first_list = [last_col, last_col + 1, last_col + 2, last_col + 3]
    second_list = [last_col - 1, last_col, last_col , last_col + 2]
    third_list = [last_col - 2, last_col - 1, last_col , last_col + 1]
    fourth_list = [last_col - 3, last_col - 2, last_col - 1 , last_col]
    if(first_list[ 0] >=0 and first_list[0] <6 and first_list[3] >= 0 and first_list[3 < 6]):
        one = grid[last_col][first_list[0]]
        two = grid[last_col][first_list[1]]
        three = grid[last_col][first_list[2]]
        four = grid[last_col][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(second_list[ 0] >=0 and first_list[0] <6 and first_list[3] >= 0 and first_list[3 < 6]):
        one = grid[last_col][first_list[0]]
        two = grid[last_col][first_list[1]]
        three = grid[last_col][first_list[2]]
        four = grid[last_col][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
        return False

    if(third_list[ 0] >=0 and first_list[0] <6 and first_list[3] >= 0 and first_list[3 < 6]):
        one = grid[last_col][first_list[0]]
        two = grid[last_col][first_list[1]]
        three = grid[last_col][first_list[2]]
        four = grid[last_col][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True 

    if(fourth_list[ 0] >=0 and first_list[0] <6 and first_list[3] >= 0 and first_list[3 < 6]):
        one = grid[last_col][first_list[0]]
        two = grid[last_col][first_list[1]]
        three = grid[last_col][first_list[2]]
        four = grid[last_col][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):

def check_right_diag():
    return grid[0][2].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][0])

def check_draw():
    for row in range(6):
        for col in range(6):
            if grid[row][col].isnumeric():
                return False  
    return True

def check_game_over():
    if check_row():
        print(current_piece + " wins!")
        return True
    elif check_col():
        print(current_piece + " wins!")
        return True
    elif check_left_diag():
        print(current_piece + " wins!")
        return True
    elif check_right_diag():
        print(current_piece + " wins!")
        return True
    elif check_draw():
        print("The Game Ends in a Draw!")
        return True
    else:
        return False

def game_loop():
    global current_piece
    print("Welcome to Connect 4!")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (0-6) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        column = int(user_choice)
        place_piece(column)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print("GAME OVER")
        
game_loop()