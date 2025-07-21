
"""
Tic Tac Toe game with GUI using tkinter.

This script allows two players to play Tic Tac Toe on a 3x3 grid.
It features a graphical interface, win/tie detection, and 
displays the winner or tie using message boxes.

Functions:
	clicked(r, c): Handle a player's move and update the board.
	check_if_win(): Check for a win or tie after each move.
"""

# Importing Packages from tkinter
from tkinter import *
from tkinter import messagebox 

Player1 = 'X'
stop_game = False

def clicked(r, c):
	"""
	Handle a player's move, update the board, and check for a win or tie.

	Args:
		r (int): Row index.
		c (int): Column index (unused in this implementation).
	"""
	global Player1
	# global stop_game

	if Player1 == "X" and states[r] == 0 and stop_game == False:
		b[r].configure(text="X")
		states[r] = 'X'
		Player1 = 'O'

	if Player1 == 'O' and states[r] == 0 and stop_game == False:
		b[r].configure(text='O')
		states[r] = "O"
		Player1 = "X"

	check_if_win()
	# check_if_tie()
	# if check_if_win() == False:
	#     tie = messagebox.showinfo("tie","its tie")
	#     return tie
def check_if_win():
	"""
	Check for a win or tie after each move and display a message box if the game ends.
	"""
	global stop_game
	# count = 0

	for i in range(3):
		if states[i][0] == states[i][1] == states[i][2] != 0:
			stop_game = True
			messagebox.showinfo("Winner", states[i][0] + " Won")
			# disableAllButton()
			break
		if states[0][i] == states[1][i] == states[2][i] != 0:
			stop_game = True
			messagebox.showinfo("Winner", states[0][i] + " Won!")
			break

	if states[0][0] == states[1][1] == states[2][2] != 0:
		stop_game = True
		messagebox.showinfo("Winner", states[0][0] + " Won!")

	elif states[0][2] == states[1][1] == states[2][0] != 0:
		stop_game = True
		messagebox.showinfo("Winner", states[0][2] + " Won!")

	elif all(states[i][j] != 0 for i in range(3) for j in range(3)):
		stop_game = True
		messagebox.showinfo("tie", "Tie")

# Design window
#Creating the Canvas 
root = Tk()
# Title of the window			 
root.title("GeeksForGeeks-:Tic Tac Toe") 
root.resizable(0,0)

#Button
b = [
	[0,0,0],
	[0,0,0],
	[0,0,0]]

#text for buttons
states = [
	[0,0,0],
	[0,0,0],
	[0,0,0]]




for i in range(3):
	for j in range(3):
		b[i][j] = Button(
			height=4, width=8,
			font=("Helvetica", "20"),
			command=lambda r=i, c=j: clicked(r, c)
		)
		b[i][j].grid(row=i, column=j)


mainloop()		 
