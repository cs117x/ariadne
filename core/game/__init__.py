from random import choice
pieces = ["p1","p2","p3","p4","p5","p6","p7"]
queue = []


def new_game(c, r):
	for i in range(1,3):
		queue += choice(pieces)

		
def next_piece():
	queue.pop(0)
	queue.append(choice(pieces))
	return queue