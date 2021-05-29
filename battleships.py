import random

def is_sunk(ship):
    """
    returns Boolean value, which is True if ship is sunk and False otherwise
    """

    if ship[3] == len(ship[4]):
        return True
    else:
        return False

def ship_type(ship):
    """
    returns one of the strings
    "battleship", "cruiser", "destroyer", or "submarine"
    identifying the type of ship
    """

    if ship[3] == 1:
        return "Submarine"
    elif ship[3] == 2:
        return "Destroyer"
    elif ship[3] == 3:
        return "Cruisers"
    elif ship[3] == 4:
        return "Battleship"

def is_open_sea(row,column,fleet):
    """
    checks if the square given by row and column neither contains nor is adjacent (horizontally, vertically, or diagonally) to some ship in fleet.
    Returns Boolean True if so and False otherwise
    """

    for s in fleet:
        if column >= 10 or column <= -1 or row >= 10 or row <= -1: return False
        elif s[2] == True:
            if row in range((s[0] - 1), (s[0] + 2)):
                if column in range((s[1] - 1), (s[1] + s[3]+1)):
                    return False

        elif s[2] == False:
            if column in range((s[1] - 1), (s[1] + 2)):
                if row in range((s[0]-1),(s[0]+s[3]+1)):
                    return False
    else:
        return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """
    checks if addition of a ship, specified by row, column, horizontal, and length as in ship representation above,
    to the fleet results in a legal arrangement (see the figure above). If so, the function returns Boolean True and it returns False otherwise.
    This function makes use of the function is_open_sea
    """

    if horizontal == True:
        if column >= (10 - (length - 1)):
            return False
        for c in (column, (column + length-1)):
            if is_open_sea(row, c ,fleet) == False:
                return False
    elif horizontal == False:
        if row >= (10 - (length - 1)):
            return False
        for r in (row, (row+length-1)):
            if is_open_sea(r, column ,fleet) == False:
                return False
    return True

def place_ship_at(row, column, horizontal, length, fleet):
    """
    returns a new fleet that is the result of adding a ship, specified by row, column, horizontal, and length as in ship representation above, to fleet.
    It may be assumed that the resulting arrangement of the new fleet is legal
    """
    ship = (row, column, horizontal, length, set())
    fleet1 = fleet
    fleet1.append(ship)
    return fleet1

def randomly_place_all_ships():
    """
    returns a fleet that is a result of a random legal arrangement of the 10 ships in the ocean.
    This function makes use of the functions ok_to_place_ship_at and place_ship_at
    """
    fleet = []
    #battleship
    row1 = random.randint(0, 9)
    column1 = random.randint(0, 9)
    horizontal1 = random.choice([True, False])
    ship = (row1, column1, horizontal1, 4,())
    while ok_to_place_ship_at(row1,column1,horizontal1,4,fleet) != True:
        row1 = random.randint(0, 9)
        column1 = random.randint(0, 9)
        horizontal1 = random.choice([True, False])
        ship = (row1, column1, horizontal1, 4, set())
    else: place_ship_at(row1,column1,horizontal1,4,fleet)
    #cruisers
    for i in range(0, 2):
        row1 = random.randint(0,9)
        column1 = random.randint(0,9)
        horizontal1 = random.choice([True,False])
        ship = (row1,column1,horizontal1,3,set())
        while ok_to_place_ship_at(row1,column1,horizontal1,3,fleet) != True:
            row1 = random.randint(0, 9)
            column1 = random.randint(0, 9)
            horizontal1 = random.choice([True, False])
            ship = (row1, column1, horizontal1,3,set())
        else: place_ship_at(row1,column1,horizontal1,3,fleet)
    #destroyers
    for i in range(0,3):
        row1 = random.randint(0, 9)
        column1 = random.randint(0, 9)
        horizontal1 = random.choice([True, False])
        ship = (row1, column1, horizontal1, 2, set())
        while ok_to_place_ship_at(row1, column1, horizontal1, 2, fleet) != True:
            row1 = random.randint(0, 9)
            column1 = random.randint(0, 9)
            horizontal1 = random.choice([True, False])
            ship = (row1, column1, horizontal1, 2, set())
        else:
            place_ship_at(row1, column1, horizontal1, 2, fleet)
    #submarines
    for i in range(0,4):
        row1 = random.randint(0, 9)
        column1 = random.randint(0, 9)
        horizontal1 = random.choice([True, False])
        ship = (row1, column1, horizontal1, 1, set())
        while ok_to_place_ship_at(row1, column1, horizontal1, 1, fleet) != True:
            row1 = random.randint(0, 9)
            column1 = random.randint(0, 9)
            horizontal1 = random.choice([True, False])
            ship = (row1, column1, horizontal1, 1, set())
        else:
            place_ship_at(row1, column1, horizontal1, 1, fleet)

    return fleet

def check_if_hits(row, column, fleet):
    """
    returns Boolean value, which is True if the shot of the human player at the square represented by row and column hits any of the ships of fleet,
    and False otherwise
    """
    for ship in fleet:
        if ship[2] == True:
            if ship[0] == row and column in range(ship[1],ship[1]+ship[3]):
                return True
        elif ship[2] == False:
            if ship[1] == column and row in range(ship[0],ship[0]+ship[3]):
                return True
    return False


def hit(row, column, fleet):
    """
    returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that receives a hit by the shot at the square represented by row and column,
    and fleet1 is the fleet resulting from this hit. It may be assumed that shooting at the square row, column results in hitting of some ship in fleet.
    Note that ship must represent the ship after the hit.
    """
    ship = None
    fleet1 = fleet
    for current_ship in fleet:
        if current_ship[2] == True:
            if current_ship[0] == row and column in range(current_ship[1],current_ship[1]+current_ship[3]):
                hit_variable = list(current_ship[4])
                fleet1.remove(current_ship)
                current_hit = (row,column)
                hit_variable.append(current_hit)
                hit_variable = set(hit_variable)
                ship = (current_ship[0], current_ship[1], current_ship[2],current_ship[3], hit_variable)
                fleet1.append(ship)
                break
        elif current_ship[2] == False:
            if current_ship[1] == column and row in range(current_ship[0],current_ship[0]+current_ship[3]):
                hit_variable = list(current_ship[4])
                fleet1.remove(current_ship)
                current_hit = (row, column)
                hit_variable.append(current_hit)
                hit_variable = set(hit_variable)
                ship = (current_ship[0], current_ship[1], current_ship[2], current_ship[3], hit_variable)
                fleet1.append(ship)
                break
    fleet1.sort()
    return (fleet1,ship)

def are_unsunk_ships_left(fleet):
    """
    returns Boolean value, which is True if there are ships in the fleet that are still not sunk, and False otherwise
    """
    total_sunk = 0
    for current_ship in fleet:
        if current_ship[3] == len(current_ship[4]):
            total_sunk += 1

    if total_sunk == len(fleet):
        return False
    else:
        return True

def duplicate_hit(row,column,fleet):
    """
    Returns True if ship within fleet if (row,column) has already been used to hit
    """
    for ship in fleet:
        if (row, column) in ship[4]:
            return True

    return False

def main():
    """
    returns nothing. It prompts the user to call out rows and columns
    of shots and outputs the responses of the computer iteratively until the game stops
    """
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and column co-ordinates seperated by a space to shoot (e.g X Y). Enter EXIT to stop game: ").split()


        if loc_str == []:
            print("No value inputted, try again. No shot added to total")

        elif loc_str[0] == "EXIT" or loc_str[0]== "Exit" or loc_str[0] == "exit":
            game_over = True
        else:
            try:
                current_row = int(loc_str[0])
                current_column = int(loc_str[1])
                shots += 1


                if current_row <=-1 or current_row >= 10 or current_column <=-1 or current_column >= 10:
                    print("Entry is off the board, try again. One shot added to your total.")

                elif check_if_hits(current_row, current_column, current_fleet) == True:
                    if duplicate_hit(current_row, current_column, current_fleet) == True:
                        print("You missed! Ship hit here earlier.")
                    else:
                        print("You have a hit!")
                        (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                        if is_sunk(ship_hit) == True:
                            print("You sank a " + ship_type(ship_hit) + "!")
                else:
                    print("You missed!")

                if not are_unsunk_ships_left(current_fleet): game_over = True
            except:
                print("Entry is not available on the board, try again. One shot added to your total.")
                shots += 1

    print("Game over! You required", shots, "shots.")

if __name__ == '__main__': #keep this in
   main()
