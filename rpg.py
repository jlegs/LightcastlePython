#!/usr/bin/env python
import random
import string

class Die:
	def __init__(self):
		myclass='this is the die roll class'
		self.myrolls=[]
	def __str__(self):
		return 'Dieroll'
	def __repr__(self):
		return 'Dieroll'
#	@staticmethod
	def roll(self, dice, sides):
		for x in self.myrolls:
			self.myrolls.remove(x)
		self.total=0
		for x in range(1, dice+1):
			self.myrolls.append(random.randrange(1, sides))
		for x in self.myrolls:
			self.total+=x
			print x,
#		print "This is the total for the die roll"
#		print self.total
		return


class Player:
	def __init__(self):
		Name = ""
		die=Die()
		print "this is the die roll"
		self.hproll=die.roll(15, 6)
		self.hpmax=die.total
#		for x in self.hproll:
#			self.hpmax += x
		self.base_attack=3
		self.base_defense=2
		self.equipment=[]
		self.equipped_items=[]

	def attack(self):
		attack_value=self.base_attack
		for item in self.equipped_items:
			attack_value+=item.attack_value
		return attack_value

	def defend(self):
		defense_value=self.base_defense
		for item in self.equipped_items:
			defense_value+=item.defense_value
		return defense_value

	def add(self, item):
		self.equipment.append(item)

	def drop(self, weapon):
		self.equipment.remove(item)

	def equip(self, item):
#		if len(self.equipped_items)>3:
#			self.equipped_items.remove()#ITEMNUMBERONE
		self.equipped_items.append(item)
#		if self.equipment.index(item):
#			self.equipped_items.append(item)

	def display_inventory(self):
		for item in self.equipment:
			print item
		return

	def display_equipped(self):
		print "These are your equipped items"
		for item in self.equipped_items:
			print item
		return

playerone=Player()
print "This is the player's max HP"
print playerone.hpmax
print "This is the player's base attack value"
print playerone.base_attack
print "This is the player's base defense value"
print playerone.base_defense
print "This is the player's attack value"
print playerone.attack()#THIS WILL RETURN ATTACK VALUE 
print "This is the player's defense value"
print playerone.defend()#RETURNS DEFENSE VALUE

#FUNCTION FOR ACTUAL COMBAT


class Equipment:
	def __init__(self, attack_value, defense_value, name, description):
		self.name=name
		self.description=description
		self.attack_value=attack_value
		self.defense_value=defense_value

	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name

	def to_string(self):
		return self.name.join(self.attack_value)

	def attack(self):
		return str(self.attack_value)
	def defend(self):
		return str(self.defend_value)


#======================ESTABLISHING WEAPONS AND ARMOR================================

longsword=Equipment(10, 0, "long sword", "A bad-ass slayer of women and small men")
print "This is the longsword's attack value"
print longsword.attack()
shortsword=Equipment(7, 0, "short sword", "A not-so-bad-ass slayer of women and small men")
print "this is the short sword's attack value"
print shortsword.attack()

lightarmor=Equipment(0, 5, "light armor", "A simple piece of armor that barely protects you. It is very simple looking.")

heavyarmor=Equipment(0,15, "heavy armor", "A complex piece of armor that protects you strongly.")









playerone.add(longsword)
playerone.add(shortsword)
playerone.add(lightarmor)
playerone.add(heavyarmor)
playerone.equip(shortsword)
playerone.equip(lightarmor)
playerone.display_inventory()
playerone.display_equipped()

print "NOW, this is the player's attack value, because we equipped a short sword"
print playerone.attack()

playerone.equip(longsword)
playerone.display_equipped()
print "NOW, this is the player's attack value, because we equipped a Long sword"
print playerone.attack()
print playerone.defend()




