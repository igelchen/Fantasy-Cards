from Cards import *
from Characters import *
from GUI import *
from Weapons import *
from Network import *

#orc = Orc(3,4,6)
#orc.reduce_hp(50)
#print orc.get_hp()
#print orc.is_alive()
#orc.reduce_hp(50)
#print orc.get_hp()
#print orc.is_alive()

server = Connection()
client = Connection("127.0.0.1")
client.send("hallo")
action = server.get_action()
print action.get_message()
server.send("hi")
action = client.get_action()
print action.get_message()
server.close()
client.close()


deck = Deck.create_random_deck(10)

gui = GUI()
gui.show_deck(deck)

while True:
    action = gui.get_action()

    if action.get_type() == "ready":
        print "Das Spiel beginnt"

    elif action.get_type() == "swap":
        deck.swap(action.get_index1(), action.get_index2())
        gui.show_deck(deck)

    elif action.get_type() == "attack":
        print "Greife an mit %d" % action.get_weapon()

    elif action.get_type() == "close":
        print "Spiel beendet"
        break

