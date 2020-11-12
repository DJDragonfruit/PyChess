from Knight import knight
from CoordFlip import coord_flip

chess = [
    [1, 2, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 6, 1, 2, 1],

]

machine_y_flip = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7: 0}

def piece_position(pos):

    num1d = False
    num2d = False

    while not num1d or not num2d:
        for char in pos:
            if not num1d:
                if char.isdigit():
                    while not num1d:
                        num1 = int(char) - 1
                        if 0 <= num1 <= 7:
                            num1d = True
                        else:
                            char = input("Your first number is outside the expected range, please enter a number between 1 and 8: ")
                else:
                    pass

            elif not num2d:
                if char.isdigit():
                    while not num2d:
                        char_minus = int(char) - 1
                        num2 = machine_y_flip[char_minus]
                        if 0 <= num2 <= 7:
                            num2d = True
                        else:
                            char = input("Your second number is outside the expected range, please enter a number between 1 and 8: ")
                else:
                    pass

        if not num1d or not num2d:
            num1d = False
            num2d = False
            pos = input("No digits or not enough digits found, please try again: ")
        else:
            print(num2, num1)
            result = [chess[num2][num1], num2, num1]
            print(result)
            return result


# This will probably have to play out as a global function that takes the input and calls the class beneath it.
# On a side note, the piece class 100% needs the ability to know its own position, either just so it always knows,
# or so it can be passed through by this function.
def play_piece(piece_num, num2, num1):
    if piece_num == 6:
        return knight(num2, num1)
    else:
        print(piece_num)


# This is temporary, I'm not sure if I'm going to move it into the piece class
# with adjustments to let it pick up diagonals,
# or just skip it and write into the piece class its ability to store the value of the square it was on.
def move_piece(newx, newy):
    chess[newx][newy] = piece_number
    if chess[y-1][x] == 1 or chess[y+1][x] == 1 or chess[y][x-1] == 1 or chess[y][x+1] == 1:
        chess[position[1]][position[2]] = 2
    elif chess[y-1][x] == 2 or chess[y+1][x] == 2 or chess[y][x-1] == 2 or chess[y][x+1] == 2:
        chess[position[1]][position[2]] = 1
    else:
        print("No reference square available")


for row in chess:
    print(row)

posit = input("Choose your piece\nEnter coordinates: ")

position = piece_position(posit)

# print(position)

piece_number = position[0]

print(piece_number)

y = position[1]

x = position[2]

new_coordinates = play_piece(piece_number, y, x)

move_piece(new_coordinates[0], new_coordinates[1])

for row in chess:
    print(row)
