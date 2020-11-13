
def king(num2, num1):
    print("You have selected a king!")

    move1 = [num2 - 1, num1]
    move2 = [num2 - 1, num1 + 1]
    move3 = [num2, num1 + 1]
    move4 = [num2 + 1, num1 + 1]
    move5 = [num2 + 1, num1]
    move6 = [num2 + 1, num1 - 1]
    move7 = [num2, num1 - 1]
    move8 = [num2 - 1, num1 - 1]

    movelist = [move1, move2, move3, move4, move5, move6, move7, move8]

    machine_y_flip = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7: 0}

    possible_moves_u = []

    for move in movelist:
        if move[0] > 7 or move[0] < 0 or move[1] > 7 or move[1] < 0:
            pass
        else:
            possible_moves_u = possible_moves_u + [move]

    possible_moves = []

    for move in possible_moves_u:
        flip_y = machine_y_flip[move[0]]
        coord = [move[1], flip_y]
        res = [x + 1 for x in coord]
        possible_moves = possible_moves + [res]

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

    m = 1

    z = len(possible_moves_u)

    while m <= z:
        if move_choice == m:
            new_coord = possible_moves_u[m - 1]
            break
        else:
            m += 1

    if move_choice > z:
        retry_num = int(input(f"{move_choice} is not a valid choice.\nPlease pick a valid number between 1 and {z}: "))
        coord_found = False
        while not coord_found:
            if 1 <= retry_num <= z:
                coord_found = True
                new_coord = possible_moves_u[retry_num - 1]
            else:
                retry_num = int(
                    input(f"{retry_num} is not a valid choice.\nPlease pick a valid number between 1 and {z}: "))

    return new_coord
