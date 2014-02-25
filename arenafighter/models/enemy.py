'''
Created on Oct 1, 2012

@author: josh
'''
from dice import Die

class Enemy():
    def __init__(self, Name, hp_dice, base_attack, base_defense, xp_value, renown_value):
        self.Name=Name
        self.xp_value=xp_value
        self.renown_value=renown_value
        dice = Die()
        self.hpmax=dice.roll(hp_dice, 6)
        self.current_hp = self.hpmax
        self.base_attack=base_attack
        self.base_defense=base_defense
        self.equipment=[]
        self.equipped_items=[]
        self.gold=dice.roll(5, 6)
#        self.right_hand=[]
#        self.left_hand=[]
#        self.head=[]
    def __str__(self):
        return self.Name
    def __repr__(self):
        return self.Name

    class Meta:
        app_label = 'arenafighter'


    def attack(self):
        attack_value=self.base_attack
        for item in self.equipped_items:
            attack_value+=item.attack_value
        dice = Die()
        attack = dice.roll(attack_value, 6)
        return attack

    def defense_value(self):
        defense_value=self.base_defense
        for item in self.equipped_items:
            defense_value+=item.defense_value
        return defense_value

    def add(self, item):
        self.equipment.append(item)

    def drop(self, item):
        self.equipment.remove(item)

    def equip(self, item):
        weapons=0
        armors=0
        for x in self.equipped_items:
            if x.is_armor==True:
                armors+=1
            else:
                weapons+=1
        if len(self.equipped_items)>2:
            self.equipped_items.pop(0)

        if self.equipment.index(item):
            if armors<=0 and item.is_armor==True:
                self.equipped_items.append(item)
            elif weapons<=1 and item.is_armor==False:
                self.equipped_items.append(item)
        else:
            print "You have too many of that type of item equipped. Try again."

    def unequip(self, item):
        self.equipped_items.remove(item)

    def display_inventory(self):
        for item in self.equipment:
            print "\t", item
        return

    def display_equipped(self):
        print "These are your equipped items"
        for item in self.equipped_items:
            print "\t", item
        return
