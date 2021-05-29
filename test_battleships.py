import pytest
from battleships import *

#all test 5 examples minimum

fleet = [(6,4,False,3,set()),(2,6,False,3,set()),(6,6,True,4,set()), (9,9,True,1,set())]
sunk_fleet = [(6,4,False,3,{(8,4),(7,4),(6,4)}),(2,6,False,3,{(4,6),(3,6),(2,6)}),(6,6,True,4,{(6,6),(6,7),(6,8),(6,9)})]

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True

def test_is_sunk2():
    s = (2, 3, False, 3, {(2, 3), (4, 3)})
    assert is_sunk(s) == False

def test_is_sunk3():
    s = sunk_fleet[1]
    assert is_sunk(s) == True

def test_is_sunk4():
    s = sunk_fleet[2]
    assert is_sunk(s) == True

def test_is_sunk5():
    s = fleet[0]
    assert is_sunk(s) == False

def test_is_sunk6():
    s = fleet[1]
    assert is_sunk(s) == False

def test_ship_type_is_cruisers1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert ship_type(s) == "Cruisers"

def test_ship_type_is_destroyer():
    s = s = (2, 3, False, 2, {(2,3), (3,3)})
    assert ship_type(s) == "Destroyer"

def test_ship_type_is_cruisers2():
    s = sunk_fleet[0]
    assert ship_type(s) == "Cruisers"

def test_ship_type_is_battleship():
    s = fleet[2]
    assert ship_type(s) == "Battleship"

def test_ship_type_is_submarine():
    s = fleet[3]
    assert ship_type(s) == "Submarine"

def test_is_open_sea1():
    assert is_open_sea(6, 4, fleet) == False

def test_is_open_sea2():
    assert is_open_sea(4, 4, fleet) == True

def test_is_open_sea3():
    assert is_open_sea(4, 9, fleet) == True

def test_is_open_sea4():
    assert is_open_sea(5, 6, fleet) == False

def test_is_open_sea5():
    assert is_open_sea(6, 7, fleet) == False

def test_is_open_sea6():
    assert is_open_sea(0, 1, fleet) == True

def test_is_open_sea7():
    assert is_open_sea(2,10, fleet) == False

def test_is_open_sea8():
    assert is_open_sea(-1, 1, fleet) == False

def test_is_open_sea9():
    assert is_open_sea(9, 0, fleet) == True

def test_is_open_sea10():
    assert is_open_sea(1, 5, fleet) == False

def test_is_open_sea11():
    assert is_open_sea(9, 3, fleet) == False

def test_is_open_sea12():
    assert is_open_sea(1, 8, fleet) == True

s1 = (6, 1, True, 3, set())
s2 = (2, 6, False, 3, set())
fleet1 = [s1,s2]

def test_is_open_sea_1():
    assert is_open_sea(5, 0, fleet1) == False

def test_is_open_sea_2():
    assert is_open_sea(6, 0, fleet1) == False

def test_is_open_sea_3():
    assert is_open_sea(7, 0, fleet1) == False

def test_is_open_sea_4():
    assert is_open_sea(5, 2, fleet1) == False

def test_is_open_sea_5():
    assert is_open_sea(6, 2, fleet1) == False

def test_is_open_sea_6():
    assert is_open_sea(7, 2, fleet1) == False

def test_is_open_sea_7():
    assert is_open_sea(5, 4, fleet1) == False

def test_is_open_sea_8():
    assert is_open_sea(6, 4, fleet1) == False

def test_is_open_sea_9():
    assert is_open_sea(7, 4, fleet1) == False

def test_is_open_sea_10():
    assert is_open_sea(1, 5, fleet1) == False

def test_is_open_sea_11():
    assert is_open_sea(1, 6, fleet1) == False

def test_is_open_sea_12():
    assert is_open_sea(1, 7, fleet1) == False

def test_is_open_sea_13():
    assert is_open_sea(3, 5, fleet1) == False

def test_is_open_sea_14():
    assert is_open_sea(3, 6, fleet1) == False

def test_is_open_sea_15():
    assert is_open_sea(3, 7, fleet1) == False

def test_is_open_sea_16():
    assert is_open_sea(5, 5, fleet1) == False

def test_is_open_sea_17():
    assert is_open_sea(5, 6, fleet1) == False

def test_is_open_sea_18():
    assert is_open_sea(5, 7, fleet1) == False

def test_ok_to_place_ship_at1(): #adjacent to ship
    assert ok_to_place_ship_at(4,5,False,2,fleet) == False

def test_ok_to_place_ship_at2(): #on top of ship
    assert ok_to_place_ship_at(9, 9, True, 1, fleet) == False

def test_ok_to_place_ship_at3(): #open sea on edge
    assert ok_to_place_ship_at(0, 0, True, 3, fleet) == True

def test_ok_to_place_ship_at4(): #open sea
    assert ok_to_place_ship_at(0, 9, False, 2, fleet) == True

def test_ok_to_place_ship_at5(): #directly on top of ship
    assert ok_to_place_ship_at(5, 4, True, 1, fleet) == False

def test_ok_to_place_ship_at6(): #open sea 1 square seperate
    assert ok_to_place_ship_at(8,1,True,2,fleet) == True

def test_ok_to_place_ship_at7(): #final square in an illegal area
    assert ok_to_place_ship_at(8,1,True,3,fleet) == False

def test_ok_to_place_ship_at8(): #off board horizontally
    assert ok_to_place_ship_at(2, 8, True, 3, fleet) == False

def test_ok_to_place_ship_at9(): #off board vertically
    assert ok_to_place_ship_at(9, 0, False, 3, fleet) == False

def test_ok_to_place_ship_at10(): #final square in an illegal area
    assert ok_to_place_ship_at(9,1,True,3,fleet) == False


def test_place_ship_at1():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set())]
    fleet1 = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set()), (1, 1, True, 1, set())]
    assert place_ship_at(1,1,True,1,fleet) == fleet1

def test_place_ship_at2():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set())]
    fleet2 = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set()), (3, 2, True, 3, set())]
    assert place_ship_at(3,2,True,3,fleet) == fleet2

def test_place_ship_at3():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set())]
    fleet3 = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set()),(5, 2, False, 3, set())]
    assert place_ship_at(5,2,False,3,fleet) == fleet3

def test_place_ship_at4():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set())]
    fleet4 = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set()),(0, 4, False, 2, set())]
    assert place_ship_at(0,4,False,2,fleet) == fleet4

def test_place_ship_at5():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set())]
    fleet5 = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set()), (0, 1, False, 1, set())]
    assert place_ship_at(0,1,False,1,fleet) == fleet5

def test_check_if_hits1():
    assert check_if_hits(9,9,fleet) == True

def test_check_if_hits2():
    assert check_if_hits(9,4, fleet) == False

def test_check_if_hits3():
    assert check_if_hits(6,4,fleet) == True

def test_check_if_hits4():
    assert check_if_hits(5,4,fleet) == False

def test_check_if_hits5():
    assert check_if_hits(6,5,fleet) == False

def test_check_if_hits6():
    assert check_if_hits(4,6,fleet) == True


def test_hit1():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, set()), (9, 9, True, 1, set())]
    fleet.sort()
    ship = (6,6,True,4,{(6,8)})
    fleet1 = [(6,4,False,3,set()), (2,6,False,3,set()), (6, 6, True, 4, {(6, 8)}), (9, 9, True, 1, set())]
    fleet1.sort()
    assert hit(6,8,fleet) == (fleet1,ship)

def test_hit2():
    fleet2 = [(6,4,False,3,set()), (2,6,False,3,set()), (6, 6, True, 4, {(6, 8)}), (9, 9, True, 1, set())]
    fleet2.sort()
    ship = (6,6,True,4,{(6,8), (6,7)})
    fleet1 = [(6,4,False,3,set()), (2,6,False,3,set()), (6, 6, True, 4, {(6, 8), (6,7)}), (9, 9, True, 1, set())]
    fleet1.sort()
    assert hit(6,7,fleet2) == (fleet1,ship)

def test_hit3():
    fleet2 = [(6,4,False,3,set()), (2,6,False,3,set()), (6, 6, True, 4, {(6, 8)}), (9, 9, True, 1, set())]
    fleet2.sort()
    ship = (6,4,False,3,{(6,4)})
    fleet1 = [(6,4,False,3,{(6,4)}), (2,6,False,3,set()), (6, 6, True, 4, {(6, 8)}), (9, 9, True, 1, set())]
    fleet1.sort()
    assert hit(6,4,fleet2) == (fleet1,ship)

def test_hit4():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, {(6,8)}), (9, 9, True, 1, set())]
    fleet.sort()
    ship = (6,6,True,4,{(6,8),(6,6)})
    fleet1 = [(6,4,False,3,set()), (2,6,False,3,set()), (6, 6, True, 4, {(6,8),(6,6)}), (9, 9, True, 1, set())]
    fleet1.sort()
    assert hit(6,6,fleet) == (fleet1,ship)

def test_hit5():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, {(6,8),(6,6)}), (9, 9, True, 1, set())]
    fleet.sort()
    ship = (6,6,True,4,{(6,8),(6,6)})
    fleet1 = [(6,4,False,3,set()), (2,6,False,3,set()), (6, 6, True, 4, {(6,8),(6,6)}), (9, 9, True, 1, set())]
    fleet1.sort()
    assert hit(6,6,fleet) == (fleet1,ship)

def test_hit6():
    fleet = [(6, 4, False, 3, set()), (2, 6, False, 3, set()), (6, 6, True, 4, {(6,8),(6,6)}), (9, 9, True, 1, set())]
    fleet.sort()
    ship = (6,6,True,4,{(6,8),(6,6),(6,7)})
    fleet1 = [(6,4,False,3,set()), (2,6,False,3,set()), (6, 6, True, 4, {(6,8),(6,6),(6,7)}), (9, 9, True, 1, set())]
    fleet1.sort()
    assert hit(6,7,fleet) == (fleet1,ship)

def test_hit7():
    fleet = [(6, 4, True, 1, set()), (2, 6, False, 3, set()), (6, 6, True, 4, {(6,8),(6,6)}), (9, 9, True, 1, set())]
    fleet.sort()
    ship = (6,4,True,1,{(6,4)})
    fleet1 = [(6,4,True,1,{(6,4)}), (2,6,False,3,set()), (6, 6, True, 4, {(6,8),(6,6),}), (9, 9, True, 1, set())]
    fleet1.sort()
    assert hit(6,4,fleet) == (fleet1,ship)

fleet = [(6,4,False,3,set()),(2,6,False,3,set()),(6,6,True,4,set()), (9,9,True,1,set())]
sunk_fleet = [(6,4,False,3,{(8,4),(7,4),(6,4)}),(2,6,False,3,{(4,6),(3,6),(2,6)}),(6,6,True,4,{(6,6),(6,7),(6,8),(6,9)})]

s1 = (6, 1, True, 3, set())
s2 = (2, 6, False, 3, set())
fleet1 = [s1,s2]
s3 = (6,6,True,4,{(6,6),(6,7),(6,8)})
fleet2 = [s1, s2, s3]
sunk1  = (6, 1, True, 3, {(6,1), (6,2), (6,3)})
sunk2 = (2, 6, False, 3, {(3,6),(2,6), (4,6)})
sunk_fleet1 = [sunk1, sunk2]

def test_are_unsunk_ships_left1():
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left2():
        assert are_unsunk_ships_left(sunk_fleet) == False

def test_are_unsunk_ships_left3():
    assert are_unsunk_ships_left(fleet1) == True

def test_are_unsunk_ships_left4():
    assert are_unsunk_ships_left(sunk_fleet1) == False

def test_are_unsunk_ships_left5():
    assert are_unsunk_ships_left(fleet2) == True


s1 = (6, 1, True, 3, set())
s2 = (2, 6, False, 3, set())
fleet1 = [s1,s2]
s3 = (6,6,True,4,{(6,7),(6,8)})
fleet2 = [s1, s2, s3]
sunk1  = (6, 1, True, 3, {(6,1), (6,2), (6,3)})
sunk2 = (2, 6, False, 3, {(3,6),(2,6), (4,6)})
sunk_fleet1 = [sunk1, sunk2]
def test_duplicate_hit1():
    assert duplicate_hit (6,1,fleet2) == False
def test_duplicate_hit2():
    assert duplicate_hit (6,8,fleet2) == True
def test_duplicate_hit3():
    assert duplicate_hit (6,6,fleet2) == False
def test_duplicate_hit4():
    assert duplicate_hit (6,1,sunk_fleet1) == True
def test_duplicate_hit5():
    assert duplicate_hit (4,6,sunk_fleet1) == True


