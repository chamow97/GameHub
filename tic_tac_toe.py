#!/usr/bin/env python

import random
import os

class Tic_Tac_Toe(object):
	#used to print the status of the game
	def PrintTable(self, position, turn):
		print("\n")
		print("\n")
		#position tells whose turn currently is
		position -= 1
		if turn == 1:
			self.table[position] = "X"
		elif turn == -1:
			self.table[position] = "O"
		#formatting the table
		for i in range(0,(self.no_of_rows)):
			print('\t\t\t', end='')
			for j in range(0,(self.no_of_rows)):
				if self.table[(i*self.no_of_rows)+j] == "X" or \
				self.table[(i*self.no_of_rows)+j] == "O":
					print(" |  ", end='')
					print(self.table[(i*(self.no_of_rows))+j], end = '')
				else:	
					print(" | ", end='')
					print(self.table[(i*(self.no_of_rows))+j], end = '')
			print(" |\n")
		#checking for winner
		self.game_over = self.CheckWinner()
		

	def Play(self):
		#to avoid problems in formatting eg. 9 requires 1 space but 12 requires 2 spaces
		#table looks hapazard so adding a 0 before numbers from 1 - 9
		self.table = []
		for i in range (0,(self.no_of_rows)*(self.no_of_rows)):
			if i <= 8:
				self.table.append("0" + str(i+1))
			else:
				self.table.append(i+1)
		position = 0
		turn = 0
		self.PrintTable(position, turn)

		#to make player1's symbol as "X" always
		if self.player2_symbol == "X":
			self.player1_symbol, self.player2_symbol = self.player2_symbol, self.player1_symbol
			self.player1_name, self.player2_name = self.player2_name, self.player1_name
		counter = 0
		turn = int(1)
		while(counter < (self.no_of_rows)*(self.no_of_rows)):
			counter += 1
			if turn == 1:
				print("\n\t\t{0} it's your turn. Enter any position (1-{1}): " .format(self.player1_name, self.no_of_rows * self.no_of_rows), end = '')
			else:
				print("\n\t\t{0} it's your turn. Enter any position (1-{1}): " .format(self.player2_name, self.no_of_rows * self.no_of_rows), end = '')
 
			position = int(input())
			

			#checking for correct input
			if (position >= 1 and
				position <= ((self.no_of_rows)*(self.no_of_rows))):
				if(self.table[position-1] != "X" and
					self.table[position-1] != "O"):
					self.PrintTable(position, turn)
					if self.game_over == "X":
						print("\n\n\t\t\tGame Over! {0} wins!!!". format(self.player1_name))
						break
					elif self.game_over == "O":
						print("\n\n\t\t\tGame Over! {0} wins!!!". format(self.player2_name))
						break
					
				else:
					counter -= 1
					print("\n\t\tPosition you entered is already filled!")
					continue
			else:
				counter -= 1
				print("\n\t\tPlease enter a position in the range (1-{0})!".format(self.no_of_rows * self.no_of_rows))
				continue
			turn *= (-1)
		if self.game_over == "-1":
			print("\n\n\t\t\tMatch ends in a Draw!!")

	
	def New_Game(self):
		print("\033[1;31m\n\n\t\t\t TIC-TAC-TOE !!\n\t\t\t --- --- ---")
		while(1):
			self.no_of_rows = int(input("\n\t\tEnter number of rows(2 - 9): "))
			if self.no_of_rows > 9 or self.no_of_rows < 2:
				print("\n\t\t Row number is restricted to range [2,9]!")
			else:
				break
		self.player1_name = input("\n\n\t\tEnter the name of Player1: ")
		if self.player1_name == "":
			self.player1_name = "Player1"
		self.player2_name = input("\n\n\t\tEnter the name of Player2: ")
		if self.player2_name == "":
			self.player2_name = "Player2"
		print("\n\n\t\t\t\t Toss-Time!")
		while(1):
			player_toss = input("\n\n\t\t\t {0} it's your call(H or T): " .format(self.player1_name));
			if (player_toss == "H" or
				player_toss == "h" or
				player_toss == "T" or
				player_toss == "t"):
				break
			else:
				print("\n\t\t\tYou have to call either H or T")

		if player_toss == "H" or player_toss == "T":
			player_toss = player_toss.lower()
		toss = random.randint(0,1)
		if ((player_toss == 'h' and toss == 0) or (player_toss == 't' and toss == 1)):
			print("\n\n\t\t\t{0} takes X and plays first." .format(self.player1_name))
			self.player1_symbol = "X"
			self.player2_symbol = "O"
		else:
			print("\n\n\t\t\t{0} takes X and plays first." .format(self.player2_name))
			self.player2_symbol = "X"
			self.player1_symbol = "O"
		self.Play()

	#to check whether game has ended or not
	def CheckWinner(self):
		is_game_over = True
		#checking primary diagonal
		for i in range (1, self.no_of_rows):
			if self.table[(i*self.no_of_rows)+i] != self.table[((i-1)*self.no_of_rows)+(i-1)]:
				is_game_over = False
				break
		if is_game_over == True:
			return self.table[0]
			

		is_game_over = True
		#checking secondary diagonal
		for i in range (1, self.no_of_rows):
			if self.table[(i*self.no_of_rows)+((self.no_of_rows-1)-i)] != self.table[((i-1)*(self.no_of_rows))+((self.no_of_rows-1)-(i-1))]:
				is_game_over = False
				break
		if is_game_over == True:
			return self.table[(self.no_of_rows-1)]

		is_game_over = True
		#checking rows
		for i in range (0, self.no_of_rows):
			is_game_over = True
			for j in range (1, self.no_of_rows):
				if self.table[(i*(self.no_of_rows))+j] != self.table[(i*(self.no_of_rows))+j-1]:
					is_game_over = False
					break
			if is_game_over == True:
				return self.table[(i*(self.no_of_rows))]
		#checking columns
		for i in range (0, (self.no_of_rows)):
			is_game_over = True
			for j in range (1, (self.no_of_rows)):
				if self.table[(j*(self.no_of_rows))+i] != self.table[((j-1)*(self.no_of_rows))+i]:
					is_game_over = False
					break
			if is_game_over == True:
				return self.table[(i)]
		#if winner cannot be decided at this stage
		return "-1"

while(1):
	T = Tic_Tac_Toe()
	T.New_Game()
	play_again = input("\n\n\t\t\t Want to play again?(y/n): ")
	if play_again == 'y' or play_again == 'Y':
		os.system("clear")
		continue
	else:
		print("\n\n\t\t\t\t GoodBye :)")
		break
