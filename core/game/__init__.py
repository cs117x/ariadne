from random import choice
pieces = ["p1","p2","p3","p4","p5","p6","p7"]

def new_game(c, r):
	
	# c=columns, r=rows
	# use later

	for i in range(1,3):
		queue += choice(pieces)

#queue = ["p4", "p1", "p5"]

def next_piece():
	queue.append(choice(pieces))
	return queue.pop(0)