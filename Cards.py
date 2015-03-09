import random
from Characters import *
from Weapons import *

class Deck():

    @staticmethod
    def create_random_deck(size):
        cards = []
        characters = [Orc, Dwarf, Dragon, Wizard, Elf]
        weapons = [Sword, Bow, Axe, Wand, Dagger, Spear]
        for i in range(size):
            character = characters[random.randint(0, len(characters)-1)](0, 0, 0)
            weapon1 = weapons[random.randint(0, len(weapons)-1)]()
            weapon2 = weapons[random.randint(0, len(weapons)-1)]()
            cards.append(Card(character, [weapon1, weapon2]))
        return Deck(cards)

    def __init__(self, cards):
        self._cards = cards
        self._deck_pointer = 0

    def next_card(self):
        card = self._cards[self._deck_pointer]
        if self._deck_pointer < len(self._cards) - 1:
            self._deck_pointer = self._deck_pointer + 1
        else:
            self._deck_pointer = 0
        return card

    def __str__(self):
        s = ""
        for i in range(len(self._cards)):
            s = s + str(i+1) + ".\n--------------------\n"
            s = s + str(self._cards[i]) + "--------------------\n\n"
        return s
    
class Card():

    def __init__(self, character, weapons):
        self._character = character
        self._weapons = weapons

    def attack(self, card, weapon_index):
        weapon = self._weapons[weapon_index - 1]
        card._character.reduce_hp(weapon.get_dp())

    def __str__(self):
        s = "%s\nHP: %d\nWaffen:\n" %(self._character.__class__.__name__, self._character.get_hp())
        for i in range(len(self._weapons)):
            s = s + str(i+1) + ". " + self._weapons[i].__class__.__name__ + "\n"
        return s
