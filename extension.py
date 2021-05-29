from tkinter import *
from battleships import *
from tkinter import messagebox

#setting up window and title of window
root = Tk()
root.title("Battleship!")
root.geometry("1250x650")

game_over = False
shots = 0
current_fleet = randomly_place_all_ships()

def enter_button():
    """
    function for the shoot button. Has game code and updates grid colour dependant on results
    shoot button disabled once all ships are sunk
    """

    global current_fleet, game_over, shots
    try:
        if entry_r.get() == "" or entry_c.get() == "":
            print("No value inputted, try again. No shot added to total"), display_currentinfo.config(text= "No value inputted, try again. No shot added to total")
        else:
            current_row = int(entry_r.get())
            current_column = int(entry_c.get())
            shots += 1
            display_shotcount.config(text=shots)

            if current_row <= -1 or current_row >= 10 or current_column <= -1 or current_column >= 10:
                return print("Entry is off the board, try again. One shot added to your total."), display_currentinfo.config(text= "Entry is off the board, try again. One shot added to your total." + "\nCurrent shot count:" + str(shots))
            elif check_if_hits(current_row, current_column, current_fleet) == True:
                if duplicate_hit(current_row, current_column, current_fleet) == True:
                    return print("You missed! Ship hit here earlier."), display_currentinfo.config(
                        text="You missed! Ship hit here earlier.")
                else:
                    (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                    if is_sunk(ship_hit) == True:
                        sunken_ship = ship_type(ship_hit)
                        BoardButton = Label(root, text=sunken_ship[0], padx=20, pady=20, bd=1, borderwidth=2, relief="groove", bg="red")
                        BoardButton.grid(row=(current_row + 2), column=(current_column + 2))
                        if not are_unsunk_ships_left(current_fleet):
                            game_over = True
                            label_shoot.config(command=DISABLED)
                            print("Game over! Congratulations you sank all ships. You required " + str(shots) + " shots.")
                            display_currentinfo.config(text="Game over! Congratulations you sank all ships. You required " + str(shots) + " shots.")
                        else: return print("You have a hit! You sank a " + ship_type(ship_hit) + "!"), display_currentinfo.config(text="You have a hit! You sank a " + sunken_ship  + "!")

                    else:
                        BoardButton = Label(root, padx=20, pady=20, bd=1, borderwidth=2, relief="groove",
                                    bg="orange")
                        BoardButton.grid(row=(current_row + 2), column=(current_column + 2))
                        print("You have a hit!"), display_currentinfo.config(text="You have a hit!")
            else:
                BoardButton = Label(root, padx=20, pady=20, bd=1, borderwidth=2, relief="groove",
                            bg="light blue")
                BoardButton.grid(row=(current_row + 2), column=(current_column + 2))
                return print("You missed!"), display_currentinfo.config(text="You missed!")

    except:
        print("Entry is not available on the board, try again. One shot added to your total."), display_currentinfo.config(text="Entry is not available on the board, try again. One shot added to your total.")
        shots += 1
        display_shotcount.config(text=shots)

def exit_button():
    """
    closes window at any point for player
    """

    global shots
    e = messagebox.askokcancel("Exit?", "Are you sure you want to Exit")
    if e == 1:
        if game_over == True:
            root.quit()
        else:
            print("Game over! You had", shots, "shots.")
            display_currentinfo.config(text="Game over! You had" + str(shots) + "shots.")
            root.quit()


for i in range(0,10):
    BoardRow = Label(root, text=i)
    BoardRow.grid(row=1, column=(i+2))
    BoardColumn = Label(root, text=i)
    BoardColumn.grid(row=(i+2), column=1)

for row in range(0,10):
    for column in range(0,10):
        BoardButton = Label(root, text=" ", padx=20, pady=20, bd=1, borderwidth=2, relief="groove", bg="light grey")
        BoardButton.grid(row=(row + 2), column=(column + 2))

entry_r = Entry(root)
entry_c = Entry(root)
display_shotcount = Label(root, text= shots)
entry_r.grid(row=7, column=14)
entry_c.grid(row=8, column=14)
display_shotcount.grid(row=6, column=14)
display_currentinfo = Label(root,)
display_currentinfo.grid(row=5, column=13)

label_r = Label(root, text="Row")
label_c = Label(root, text="Column")
label_shotcount = Label(root, text="Current shot count")
label_shoot = Button(root, text="SHOOT!", fg="red", command=enter_button)
label_exit = Button(root, text="EXIT", fg="red", bg="white", command=exit_button)
label_r.grid(row=7, column=13)
label_c.grid(row=8, column=13)
label_shotcount.grid(row=6, column=13)
label_shoot.grid(row=9, column=14, columnspan=3, padx=10, pady=10)
label_exit.grid(row=9, column=13, columnspan=3, padx=10, pady=10)

if game_over == True:
    print("Game over! Congratulations you sank all ships. You required" + str(shots) + "shots.")
    display_currentinfo.config(text="Game over! Congratulations you sank all ships. You required" + str(shots) + "shots.")

root.mainloop()


