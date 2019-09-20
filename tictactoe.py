from IPython.display import clear_output
import random

def display_playingboard(board):
	print('\n'*150)
	print(board[7]+ ' |'+ board[8]+ ' |'+ board[9])
	print(board[6]+ ' |'+ board[5]+ ' |'+ board[4])
	print(board[3]+ ' |'+ board[2]+ ' |'+ board[1])

test_board = ['#','X','O','X','O','X','O','X','O','X']

def player_input():
	player_marker = ''
	#Keep asking player 1 to choose X or O
	while player_marker != 'X' and player_marker != 'O':
		player_marker = input('Player 1, choose either X or O as a marker:')
	#Assign Player 2 opposite

		player1_marker = player_marker

		if player1_marker == 'X':
			player2_marker = 'O'
		else:
			player2_marker = 'X'

	return (player1_marker,player2_marker)

def marker_placement(playing_board, marker, position):
	playing_board[position] = marker

marker_placement(test_board, 'X', 3)
display_playingboard(test_board)

def check_winner(board, mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

check_winner(test_board, 'X')

def random_player_start():
	if random.randint(0, 1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

def space_verify(board, position):

	return board[position] == ' '

def full_board_check(board):
	for i in range(1,10):
		if space_verify(board, i):
			return False
	return True

def player_position(board):
	position = 0 

	while position not in [1,2,3,4,5,6,7,8,9] or not space_verify(board, position):
		position = int(input('Choose your next position: (1-9) '))

	return position

def replay_game():
	return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print ('Welcome to Tic Tac Toe!')

while True:
	mainBoard = [' '] * 10
	player1_marker, player2_marker = player_input()
	turn = random_player_start()

	print(turn + ' will begin the game.')

	play_game = input('Are you ready to play? Enter Yes or No: ')

	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player 1':

			display_playingboard(mainBoard)
			#Choose a position on the board which is now visible.
			position = player_position(mainBoard)
			#Place the marker on that position
			marker_placement(mainBoard,player1_marker,position)

			if check_winner(mainBoard, player1_marker):
				display_playingboard(mainBoard)
				print('Player 1 has won!')
				game_on = False
			else:
				if full_board_check(mainBoard):
					display_playingboard(mainBoard)
					print('The game is a TIE!')
					break
				else:
					turn = 'Player 2'

		else:
			display_playingboard(mainBoard)
			#Choose a position on the board which is now visible.
			position = player_position(mainBoard)
			#Place the marker on that position
			marker_placement(mainBoard,player2_marker,position)

			if check_winner(mainBoard, player2_marker):
				display_playingboard(mainBoard)
				print('Player 2 has won!')
				game_on = False
			else:
				if full_board_check(mainBoard):
					display_playingboard(mainBoard)
					print('The game is a TIE!')
					break
				else:
					turn = 'Player 1'

	if not replay_game():
		break