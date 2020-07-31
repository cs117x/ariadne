from core.game import new_game, next_piece

global queue
queue = []

if __name__ == '__main__':
	new_game(7, 40)
	print(next_piece())