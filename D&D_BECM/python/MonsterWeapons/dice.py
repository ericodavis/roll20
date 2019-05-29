import random


def roll_dice(DieImport):
	# Die Import should be in the format 3d8 or 1d6
	a, b = DieImport.split('d')
	roll = 0
	a = int(a)
	b = int(b)
	for i in range(a):
		roll += random.randint(1,b)
	# print(roll)
	return roll
