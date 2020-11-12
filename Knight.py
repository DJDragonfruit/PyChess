
def knight(num1, num2):
    print("You have selected a knight")

    move1 = [num1 - 2, num2 + 1]
    move2 = [num1 - 1, num2 + 2]
    move3 = [num1 + 1, num2 + 2]
    move4 = [num1 + 2, num2 + 1]
    move5 = [num1 + 2, num2 - 1]
    move6 = [num1 + 1, num2 - 2]
    move7 = [num1 - 1, num2 - 2]
    move8 = [num1 - 2, num2 - 1]

    movelist = [move1, move2, move3, move4, move5, move6, move7, move8]

    possible_moves_u = []

    for move in movelist:
        # print(move)
        if move[0] > 7 or move[0] < 0 or move[1] > 7 or move[1] < 0:
            pass
        else:
            possible_moves_u = possible_moves_u + [move]

    possible_moves = []

    for move in possible_moves_u:
        res = [x + 1 for x in move]
        possible_moves = possible_moves + [res]

    # print(possible_moves)

    # for move in possible_moves:
        # print(move)

    i = len(possible_moves)

    if i == 8:
        move_choice = int(input(f"Which move would you like to make?:\n1. {possible_moves[0]}\n2. {possible_moves[1]}\n3. {possible_moves[2]}\n4. {possible_moves[3]}\n5. {possible_moves[4]}\n6. {possible_moves[5]}\n7. {possible_moves[6]}\n8. {possible_moves[7]}\n: "))
    elif i == 7:
        move_choice = int(input(f"Which move would you like to make?:\n1. {possible_moves[0]}\n2. {possible_moves[1]}\n3. {possible_moves[2]}\n4. {possible_moves[3]}\n5. {possible_moves[4]}\n6. {possible_moves[5]}\n7. {possible_moves[6]}\n: "))
    elif i == 6:
        move_choice = int(input(f"Which move would you like to make?:\n1. {possible_moves[0]}\n2. {possible_moves[1]}\n3. {possible_moves[2]}\n4. {possible_moves[3]}\n5. {possible_moves[4]}\n6. {possible_moves[5]}\n: "))
    elif i == 5:
        move_choice = int(input(f"Which move would you like to make?:\n1. {possible_moves[0]}\n2. {possible_moves[1]}\n3. {possible_moves[2]}\n4. {possible_moves[3]}\n5. {possible_moves[4]}\n: "))
    elif i == 4:
        move_choice = int(input(f"Which move would you like to make?:\n1. {possible_moves[0]}\n2. {possible_moves[1]}\n3. {possible_moves[2]}\n4. {possible_moves[3]}\n: "))
    elif i == 3:
        move_choice = int(input(f"Which move would you like to make?:\n1. {possible_moves[0]}\n2. {possible_moves[1]}\n3. {possible_moves[2]}\n: "))
    else:
        move_choice = int(input(f"Which move would you like to make?:\n1. {possible_moves[0]}\n2. {possible_moves[1]}\n: "))

    # print(move_choice)

    m = 0

    z = len(possible_moves)

    while m <= z:
        if move_choice == m:
            new_coord = possible_moves[m-1]
            break
        else:
            m += 1

    if move_choice > z:
        retry_num = int(input(f"{move_choice} is not a valid choice.\nPlease pick a valid number between 1 and {z}: "))
        coord_found = False
        while not coord_found:
            if 1 <= retry_num <= z:
                coord_found = True
                new_coord = possible_moves[retry_num-1]
            else:
                retry_num = int(input(f"{retry_num} is not a valid choice.\nPlease pick a valid number between 1 and {z}: "))

    new_coord_u = []

    for coord in new_coord:
        coord = coord - 1
        new_coord_u = new_coord_u + [coord]


    # print(new_coord_u)

    return new_coord_u
