from tkinter import *

root = Tk()

grid_color = "#003AFF"
red_color = "#FF1800"
yellow_color = "#FFF600"
grid_width = 420
grid_height = grid_width
diameter = grid_width / 7
col_width = diameter
total_rows = 6
total_cols = 7
is_game_over = False
current_col_choice = -1
piece_placed = False

screen = Canvas(root, width=grid_width, height=grid_height, bg=grid_color)
screen.pack()


grid = [
    ["-", "-", "-", "-", "-", "-", "-"],     # [R0C0, ..., R0C6]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R1C0, ..., R1C6]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R2C0, ..., R2C6]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R3C0, ..., R3C6]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R4C0, ..., R4C6]
    ["-", "-", "-", "-", "-", "-", "-"]      # [R5C0, ..., R5C6]
]

current_piece = "R"

last_row = -1
last_col = -1
remaining_spots = 42

def draw_circle(row, col, color):
    x_start = col * diameter
    y_start = row * diameter
    x_end = x_start + diameter
    y_end = y_start + diameter
    screen.create_oval(x_start, y_start, x_end, y_end, fill=color)
    pass


def draw_grid():
    for row in range(total_rows):
        for col in range(total_cols):
            draw_circle(row, col, "#FFFFFF")  

def is_bad_num_string(choice: str):
    if (choice.isnumeric() and int(choice) >= 0 and int(choice) <= 6):
        return False
    return True


def is_bad_choice(choice: str):
    if (choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)


def place_piece():
    global last_row
    global last_col
    global remaining_spots
    global current_col_choice
    global piece_placed
    while (True):
        row = 5
        while (row >= 0):
            if grid[row][current_col_choice].__eq__("-"):
                grid[row][current_col_choice] = current_piece
                last_row = row
                last_col = current_col_choice
                remaining_spots -= 1
                piece_placed = True
                if current_piece.__eq__("R"):
                    draw_circle(row, current_col_choice, red_color)
                else:
                    draw_circle(row, current_col_choice, yellow_color)
                break
            else:
                row -= 1
        if row != -1:
            break
        else:
            piece_placed = False
            break



def check_row():
    first_list = [last_col, last_col + 1, last_col + 2, last_col + 3]
    second_list = [last_col - 1, last_col, last_col + 1, last_col + 2]
    third_list = [last_col - 2, last_col - 1, last_col, last_col + 1]
    fourth_list = [last_col - 3, last_col - 2, last_col - 1, last_col]
    if(first_list[0] >= 0 and first_list[0] < 7 and first_list[3] >= 0 and first_list[3] < 7):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        four = grid[last_row][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (second_list[0] >= 0 and second_list[0] < 7 and second_list[3] >= 0 and second_list[3] < 7):
        one = grid[last_row][second_list[0]]
        two = grid[last_row][second_list[1]]
        three = grid[last_row][second_list[2]]
        four = grid[last_row][second_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (third_list[0] >= 0 and third_list[0] < 7 and third_list[3] >= 0 and third_list[3] < 7):
        one = grid[last_row][third_list[0]]
        two = grid[last_row][third_list[1]]
        three = grid[last_row][third_list[2]]
        four = grid[last_row][third_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (fourth_list[0] >= 0 and fourth_list[0] < 7 and fourth_list[3] >= 0 and fourth_list[3] < 7):
        one = grid[last_row][fourth_list[0]]
        two = grid[last_row][fourth_list[1]]
        three = grid[last_row][fourth_list[2]]
        four = grid[last_row][fourth_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    return False
        
def check_col():
    first_list = [last_row, last_row + 1, last_row + 2, last_row + 3]
    second_list = [last_row - 1, last_row, last_row , last_row + 2]
    third_list = [last_row - 2, last_row - 1, last_row , last_row + 1]
    fourth_list = [last_row - 3, last_row - 2, last_row - 1 , last_row]
    if(first_list[0] >= 0 and first_list[0] < 6 and first_list[3] >= 0 and first_list[3] < 6):
        one = grid[first_list[0]][last_col]
        two = grid[first_list[1]][last_col]
        three = grid[first_list[2]][last_col]
        four = grid[first_list[3]][last_col]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(second_list[ 0] >=0 and second_list[0] <6 and second_list[3] >= 0 and second_list[3] < 6):
        one = grid[second_list[0]][last_col]
        two = grid[second_list[1]][last_col]
        three = grid[second_list[2]][last_col]
        four = grid[second_list[3]][last_col]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True

    if(third_list[ 0] >=0 and third_list[0] <6 and third_list[3] >= 0 and third_list[3] < 6):
        one = grid[third_list[0]][last_col]
        two = grid[third_list[1]][last_col]
        three = grid[third_list[2]][last_col]
        four = grid[third_list[3]][last_col]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True 
  
    if(fourth_list[ 0] >=0 and fourth_list[0] <6 and fourth_list[3] >= 0 and fourth_list[3] < 6):
        one = grid[fourth_list[0]][last_col]
        two = grid[fourth_list[1]][last_col]
        three = grid[fourth_list[2]][last_col]
        four = grid[fourth_list[3]][last_col]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    return False

def check_left_diag():
    first_list_row = [last_col, last_col + 1, last_col + 2, last_col + 3]
    first_list_col = [last_row, last_row + 1, last_row + 2, last_row + 3]
    second_list_row = [last_col - 1, last_col, last_col + 1, last_col + 2]
    second_list_col = [last_row - 1, last_row, last_row + 1, last_row + 2]
    third_list_row = [last_col - 2, last_col - 1, last_col , last_col + 1]
    third_list_col = [last_row - 2, last_row - 1, last_row , last_row + 1]
    fourth_list_row = [last_col - 3, last_col - 2, last_col - 1 , last_col]
    fourth_list_col = [last_row - 3, last_row - 2, last_row - 1 , last_row]
    if(first_list_row[0] >= 0 and first_list_row[0] < 7 and first_list_row[3] >= 0 and first_list_row[3] < 7):
        if(first_list_col[0] >= 0 and first_list_col[0] < 6 and first_list_col[3] >= 0 and first_list_col[3] < 6):
            one = grid[first_list_col[0]][first_list_row[0]]
            two = grid[first_list_col[1]][first_list_row[1]]
            three = grid[first_list_col[2]][first_list_row[2]]
            four = grid[first_list_col[3]][first_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    if (second_list_col[0] >= 0 and second_list_col[0] < 6 and second_list_col[3] >= 6 and second_list_col[3] < 6):
        if(second_list_row[0] >= 0 and second_list_row[0] < 7 and second_list_row[3] >= 0 and second_list_row[3] < 7):
            one = grid[second_list_col[0]][second_list_row[0]]
            two = grid[second_list_col[1]][second_list_row[1]]
            three = grid[second_list_col[2]][second_list_row[2]]
            four = grid[second_list_col[3]][second_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    
    if(third_list_row[ 0] >=0 and third_list_row[0] <7 and third_list_row[3] >= 0 and third_list_row[3] < 7):
        if(third_list_col[ 0] >=0 and third_list_col[0] <6 and third_list_col[3] >= 0 and third_list_col[3] < 6):
            one = grid[third_list_col[0]][third_list_row[0]]
            two = grid[third_list_col[1]][third_list_row[1]]
            three = grid[third_list_col[2]][third_list_row[2]]
            four = grid[third_list_col[3]][third_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    if(fourth_list_row[ 0] >=0 and fourth_list_row[0] <7 and fourth_list_row[3] >= 0 and fourth_list_row[3] < 7):
        if(fourth_list_col[ 0] >=0 and fourth_list_col[0] <6 and fourth_list_col[3] >= 0 and fourth_list_col[3] < 6):
            one = grid[fourth_list_col[0]][fourth_list_row[0]]
            two = grid[fourth_list_col[1]][fourth_list_row[1]]
            three = grid[fourth_list_col[2]][fourth_list_row[2]]
            four = grid[fourth_list_col[3]][fourth_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    return False

def check_right_diag():
    first_list_row = [last_col, last_col - 1, last_col - 2, last_col - 3]
    first_list_col = [last_row, last_row + 1, last_row + 2, last_row + 3]
    second_list_row = [last_col + 1, last_col, last_col - 1, last_col - 2]
    second_list_col = [last_row - 1, last_row, last_row + 1, last_row + 2]
    third_list_row = [last_col + 2, last_col + 1, last_col , last_col - 1]
    third_list_col = [last_row - 2, last_row - 1, last_row , last_row + 1]
    fourth_list_row = [last_col + 3, last_col + 2, last_col + 1 , last_col]
    fourth_list_col = [last_row - 3, last_row - 2, last_row - 1 , last_row]
    if(first_list_row[0] >= 0 and first_list_row[0] < 7 and first_list_row[3] >= 0 and first_list_row[3] < 7):
        if(first_list_col[0] >= 0 and first_list_col[0] < 6 and first_list_col[3] >= 0 and first_list_col[3] < 6):
            one = grid[first_list_col[0]][first_list_row[0]]
            two = grid[first_list_col[1]][first_list_row[1]]
            three = grid[first_list_col[2]][first_list_row[2]]
            four = grid[first_list_col[3]][first_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    if (second_list_col[0] >= 0 and second_list_col[0] < 6 and second_list_col[3] >= 0 and second_list_col[3] < 6):
        if(second_list_row[0] >= 0 and second_list_row[0] < 7 and second_list_row[3] >= 0 and second_list_row[3] < 7):
            one = grid[second_list_col[0]][second_list_row[0]]
            two = grid[second_list_col[1]][second_list_row[1]]
            three = grid[second_list_col[2]][second_list_row[2]]
            four = grid[second_list_col[3]][second_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    
    if(third_list_row[ 0] >=0 and third_list_row[0] <7 and third_list_row[3] >= 0 and third_list_row[3] < 7):
        if(third_list_col[ 0] >=0 and third_list_col[0] <6 and third_list_col[3] >= 0 and third_list_col[3] < 6):
            one = grid[third_list_col[0]][third_list_row[0]]
            two = grid[third_list_col[1]][third_list_row[1]]
            three = grid[third_list_col[2]][third_list_row[2]]
            four = grid[third_list_col[3]][third_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    if(fourth_list_row[ 0] >=0 and fourth_list_row[0] <7 and fourth_list_row[3] >= 0 and fourth_list_row[3] < 7):
        if(fourth_list_col[ 0] >=0 and fourth_list_col[0] <6 and fourth_list_col[3] >= 0 and fourth_list_col[3] < 6):
            one = grid[fourth_list_col[0]][fourth_list_row[0]]
            two = grid[fourth_list_col[1]][fourth_list_row[1]]
            three = grid[fourth_list_col[2]][fourth_list_row[2]]
            four = grid[fourth_list_col[3]][fourth_list_row[3]]
            if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
                return True
    return False


def check_draw():
    return remaining_spots == 0


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
    
def handle_click(e):
    global is_game_over
    global current_piece
    global current_col_choice
    global piece_placed
    mouse_x = e.x
    if mouse_x >= 0 * col_width and mouse_x < 1 * col_width:
        current_col_choice = 0
    elif mouse_x >= 1 * col_width and mouse_x < 2 * col_width:
        current_col_choice = 1
    elif mouse_x >= 2 * col_width and mouse_x < 3 * col_width:
        current_col_choice = 2
    elif mouse_x >= 3 * col_width and mouse_x < 4 * col_width:
        current_col_choice = 3        
    elif mouse_x >= 4 * col_width and mouse_x < 5 * col_width:
        current_col_choice = 4
    elif mouse_x >= 5 * col_width and mouse_x < 6 * col_width:
        print(mouse_x)
        current_col_choice = 5
    elif mouse_x >= 6 * col_width and mouse_x < 7 * col_width:
        current_col_choice = 6
    if(not is_game_over):
        place_piece()
    if (not is_game_over and check_game_over()):
        is_game_over = True
    if(piece_placed):
        current_piece = "Y" if current_piece.__eq__("R") else "R"

def print_intro():
    print("Welcome to CONNECT FOUR")
    draw_grid()


screen.bind("<Button-1>", handle_click)

print_intro()

mainloop()