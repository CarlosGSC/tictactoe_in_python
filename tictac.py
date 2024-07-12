#TIC TAC TOE GAME

gameboard_line1=[' ',' ',' ']
gameboard_line2=[' ',' ',' ']
gameboard_line3=[' ',' ',' ']

round_count=0
choiced_numbers=[]

result=0 

#CLEAR SCREEN
def clear_screen():
	import os
	os.system('cls') or None

#COUNT THE NUMBER OF ROUNDS
def round_count_inc():
	global round_count
	round_count+=1

#PRINT THE BOARD ON THE SCREEN
def displayboard():
	clear_screen()
	print('----------------TIC TAC TOE GAME---------------\n\n')
	print('                    |     |')
	print('                 '+gameboard_line1[0]+'  |  '+gameboard_line1[1]+'  |  '+gameboard_line1[2])
	print('               _____|_____|_____')
	print('                    |     |')
	print('                 '+gameboard_line2[0]+'  |  '+gameboard_line2[1]+'  |  '+gameboard_line2[2])
	print('               _____|_____|_____')
	print('                    |     |')
	print('                 '+gameboard_line3[0]+'  |  '+gameboard_line3[1]+'  |  '+gameboard_line3[2])
	print('                    |     |\n\n')
	return

#VALIDATING OF USER INPUT
def userinput():
	choice='empty'
	acceptable_number=['1','2','3','4','5','6','7','8','9']

	while choice not in acceptable_number or choice  in choiced_numbers:
		choice=input('Chose a number(1-9):')
		if choice not in acceptable_number:
			print('Sorry, write a number in the range (1-9)')
		elif choice  in choiced_numbers:
			print('Sorry, this number has already been chosen')
	
	choiced_numbers.append(choice)
	print(choiced_numbers)

	result=int(choice)

	return result

#CHECK IF THE GAME HAS FINISHED
def check_victory():
	if gameboard_line1 == ['O','O','O'] or gameboard_line2 == ['O','O','O'] or gameboard_line3 == ['O','O','O']:
		displayboard()
		print('Player O is the winner')
		exit()
	elif gameboard_line1[0]==gameboard_line2[0]==gameboard_line3[0]=='O':
		displayboard()
		print('Player O is the winner')
		exit()	
	elif gameboard_line1[1]==gameboard_line2[1]==gameboard_line3[1]=='O':
		displayboard()
		print('Player O is the winner')
		exit()
	elif gameboard_line1[2]==gameboard_line2[2]==gameboard_line3[2]=='O':
		displayboard()
		print('Player O is the winner')
		exit()	
	elif gameboard_line1[0]==gameboard_line2[1]==gameboard_line3[2]=='O':
		displayboard()
		print('Player O is the winner')
		exit()	
	elif gameboard_line1[2]==gameboard_line2[1]==gameboard_line3[0]=='O':
		displayboard()
		print('Player O is the winner')
		exit()

	elif gameboard_line1 == ['X','X','X'] or gameboard_line2 == ['X','X','X'] or gameboard_line3 == ['X','X','X']:
		displayboard()
		print('Player X is the winner')
		exit()
	elif gameboard_line1[0]==gameboard_line2[0]==gameboard_line3[0]=='X':
		displayboard()
		print('Player X is the winner')
		exit()	
	elif gameboard_line1[1]==gameboard_line2[1]==gameboard_line3[1]=='X':
		displayboard()
		print('Player X is the winner')
		exit()
	elif gameboard_line1[2]==gameboard_line2[2]==gameboard_line3[2]=='X':
		displayboard()
		print('Player X is the winner')
		exit()	
	elif gameboard_line1[0]==gameboard_line2[1]==gameboard_line3[2]=='X':
		displayboard()
		print('Player X is the winner')
		exit()	
	elif gameboard_line1[2]==gameboard_line2[1]==gameboard_line3[0]=='X':
		displayboard()
		print('Player X is the winner')
		exit()
	elif round_count==9:
		displayboard()
		print('The game ended in a draw')
		exit()


#PLAYER X TURN
def player_X():
	round_count_inc()
	displayboard()
	print('PLAYER "X" TURN')
	result=userinput()
	
	if result in [1,2,3]:
		gameboard_line1[result-1]='X'
	elif result in [4,5,6]:	
		gameboard_line2[result-4]='X'
	elif result in [7,8,9]:	
		gameboard_line3[result-7]='X'

	check_victory()

	player_O()		

#PLAYER O TURN
def player_O():
	round_count_inc()
	displayboard()
	print('PLAYER "O" TURN')
	result=userinput()
	
	if result in [1,2,3]:
		gameboard_line1[result-1]='O'
	elif result in [4,5,6]:	
		gameboard_line2[result-4]='O'
	elif result in [7,8,9]:	
		gameboard_line3[result-7]='O'

	check_victory()

	player_X()		

#MAKES THE GAME INITIALIZE
def initialization():
	displayboard()
	acceptable_characters=['x','X','o','O']
	player_1=''

	while player_1 not in acceptable_characters:
		player_1=input("TO START THE GAME\nPlease, select X or O:")


	if player_1=='X' or player_1=='x':
		player_X()
	elif player_1=='O' or player_1=='o':
		player_O()

initialization()

