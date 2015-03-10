from Cards import *
from Characters import *
from GUI import *
from Weapons import *
from Network import *

deck = Deck.create_random_deck(10)

is_server = False
if raw_input("als Server starten? (j/n):") == "j":
    is_server = True

if is_server:
    connection = Connection()
else:
    connection = Connection("127.0.0.1")

if is_server:
    action = connection.get_action()
    if action.get_type() == "attack":
        enemy_card = action.get_card()
        enemy_card.attack()
