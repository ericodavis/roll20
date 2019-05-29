from dice import roll_dice
from random import choice

Weapons = {'1d4':['Club', 'Dagger','Sling'], '1d6': ['Bow', 'Hand Axe', 'Mace', 'Crossbow', 'Short Sword', 'Spear', 'War Hammer'],
		   '1d8': ["Long Sword", 'Battle Axe'], '1d10':['Lance', 'Pole Arm', 'Two-handed Sword']}

def weapon_damage(weapon):

	if weapon in Weapons['1d4']:
		damage = '1d4'
	elif weapon in Weapons['1d6']:
		damage = '1d6'
	elif weapon in Weapons['1d8']:
		damage = '1d8'
	elif weapon in Weapons['1d10']:
		damage = '1d10'

	return damage

class Monster:
	def __init__(self):
		self.Name = 'Monster'
		self.HP = 0
		self.weapon = ''
		self.Damage = '1d4'
		self.Inventory = []
	def Simple_Print(self):
		print(self.Name)
		print('hp:',self.HP)
		print(self.Damage)
		for item in self.Inventory:
			print(item)

class Kobold(Monster):
	def __init__(self):
		super().__init__()
		self.Name = 'Kobold'
		self.HP = roll_dice('1d4')
		roll = roll_dice('1d4')
		if roll <= 2:
			self.weapon = choice(Weapons['1d4'])

		else:
			if roll == 4:
				roll2 = roll_dice('1d4')
				if roll2 >= 3:
					self.weapon = choice(Weapons['1d8'])
				else:
					self.weapon = choice(Weapons['1d6'])
			else:
				self.weapon = choice(Weapons['1d6'])
		listx = ['Sling', 'Bow']
		if self.weapon == 'Crossbow':
			self.weapon = 'Bow'


		self.Inventory = [self.weapon]
		# TODO needs a function
		if self.weapon in listx:
			self.Inventory.append('Dagger')
			if self.weapon == 'Bow':
				self.Inventory.append('5 Arrows')
			if self.weapon == 'Sling':
				self.Inventory.append('5 stones')
		self.Damage = weapon_damage(self.weapon)

	def Simple_Print(self):
		print(self.Name)
		print('hp:',self.HP)
		print(self.Damage)
		for item in self.Inventory:
			print(item)

class Skeleton(Monster):
	def __init__(self):
		super().__init__()
		self.Name = 'Skeleton'
		self.HP = roll_dice('1d8')
		roll = roll_dice('1d6')
		if roll <=  1:
			self.weapon = choice(Weapons['1d4'])
		elif roll <=  4:
			self.weapon = choice(Weapons['1d6'])
		elif roll <=  5:
			self.weapon = choice(Weapons['1d8'])
		elif roll <=  6:
			self.weapon = choice(Weapons['1d10'])
		if self.weapon == 'Sling':
			self.weapon = 'Club'
		elif self.weapon == 'Crossbow':
			self.weapon = 'Bow'
		self.Damage = weapon_damage(self.weapon)
		self.Inventory = [self.weapon]
		# TODO needs a function
		listx = ['Sling', 'Bow']
		if self.weapon in listx:
			self.Inventory.append('Dagger')
			if self.weapon == 'Bow':
				self.Inventory.append('5 Arrows')
			if self.weapon == 'Sling':
				self.Inventory.append('5 stones')



# Change the number in the range to change the number of monsters
for i in range(3):
	name = 'monster' + str(i)
	name = Skeleton()
	print('')
	name.Simple_Print()



