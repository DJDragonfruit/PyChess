from Knight import knight

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
                        num2 = int(char) - 1
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
            print(num1, num2)
            result = [chess[num1][num2], num1, num2]
            print(result)
            return result


# This will probably have to play out as a global function that takes the input and calls the class beneath it.
# On a side note, the piece class 100% needs the ability to know its own position, either just so it always knows,
# or so it can be passed through by this function.
def play_piece(piece_num, num1, num2):
    if piece_num == 6:
        return knight(num1, num2)
    else:
        print(piece_num)


# This is temporary, I'm not sure if I'm going to move it into the piece class
# with adjustments to let it pick up diagonals,
# or just skip it and write into the piece class its ability to store the value of the square it was on.
def move_piece(newy, newx):
    chess[newy][newx] = piece_number
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

y = position[1]

x = position[2]

new_coordinates = play_piece(piece_number, y, x)

move_piece(new_coordinates[0], new_coordinates[1])

for row in chess:
    print(row)

# CHECK IF ENTERED COORDS ARE VALID COORDS
# CHECK SQUARE IDENTITY BASED ON BACKGROUND COLOR, or invis identifier number, added through class
# Check piece identity based on color, or check based on an invisible identifier number
# USE %s to fill a print about their movement, possibly color moved piece bright yellow
# ADD ERROR COLOR CODES
# Check if piece found is a valid piece or a space
# Piece class
# Store a value in piece class that can check the identity of the space it's moving to, store that identity,
# and either pass it to the piece that takes it, or pass it back to the space when it moves.
# Piece class needs to hold the basic functions that are the same for every piece,
# and smaller classes for each piece will inherit the values of the main piece class.
# Possibly need a game function for initializing a game, keeping track of killed units maybe?
# Maybe have a secondary array that prints alongside the first that can show all the killed units.
# Flip things around so it takes input as (x, y) not (y, x) because the game is supposed to be played by HUMANS
#
# NEW ORGANIZATION: So we probably aren't going to be using a class for a piece or whatever. We don't need it,
# and each piece on the board can't represent an instance of a class. So what we're going to start with is having
# the play_piece function run down the list of possible piece names, check hey is this a 6 or whatnot.
# If it is a 6 it will call the knight function. The knight function just accepts the coordinates it is given
# and based on those, calculates all of its possible moves, before removing the moves that would place it outside
# of the board, and printing all the moves. At this point I think the knight function should continue
# to handle the input, execute the actual move, and then I'm still thinking about the best way to determine
# the original identity of a square, as that was supposed to be a feature of my class setup.
# Right now it's looking like the best course of action for figuring out square identity is likely just using the
# current method, but if it can't find a reference square adjacent to it, checking two squares out, and maybe one more.
# However I do feel that the likelihood of two thirds of the pieces on the board directly surrounding one piece that
# needs to move is insanely unlikely, and honestly probably impossible. But I think one of my biggest goals with this
# project is making it positively idiot proof. Unless someone inputs an incorrect value 1000 times and causes a stack
# overflow like the kind gentleman on stack overflow noted.
#
# Turn Order:
# 1. Player enters coordinates of piece they want to play.
# 2. Code checks the identity of the piece they picked, and uses it to determine which function to run.
# 3. Code gives all available options for movement, possibly give the outcome of the move,
# such as taking a piece and or final square(Don't forget to translate from array coords to human coords).
# 4. Player chooses the option they want, code moves the piece and deletes the piece it lands on,
# while checking for the original identity of the piece it moved from.
# 5. Not sure if this is needed depending on how I set up the classes or functions,
# but variables like num1, num2, newx, newy, etc. need to be purged,
# unless they aren't referenced before their assignment.
# (num1 and num2 are both possibly referenced before their assignment.
