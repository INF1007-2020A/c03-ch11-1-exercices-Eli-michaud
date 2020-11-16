"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min()

	@property
	def name(self):
		return self.__name

class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.hp = self.max_hp

	@property
	def name(self):
		return self.__name

	@property
	def hp(self):
		return  self.__hp

	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)

	def compute_damage(self, other):
		level_factor = (2 * self.level) / 5 + 2
		weapon_factor = self.weapon.power
		atk_def_factor = self.attack / other.defense
		critical = random.random() <= 1/16
		modifier = (2 if critical else 1) * random.uniform(0.85, 1.0)
		damage = ((level_factor * weapon_factor * atk_def_factor) / 50 + 2) * modifier
		return damage

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	damage, critical = attacker.computer_damage(defender)
	defender.hp -= damage
	print(f"{attacker.name} used {attacker.weapon.name}")
	if critical:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	defender = c2
	turn  = 1
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort
		deal_damage(attacker, defender)
		if defender.hp <= 0:
			print(f"{defender.name } is sleeping with the fishes.")
			break

		attacker, defender = defender, attacker
		turn += 1
	return turn
		# Échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués

c1 = Character("Apik", 200, 150, 70, 70)
c2 = Character("gammor", 250, 100, 120, 60)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)

turns = run_battle(c1, c2)
print(f"The battle ended in {turns} turns.")