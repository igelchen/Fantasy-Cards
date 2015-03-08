from Tkinter import *
from thread import start_new_thread
import Queue

class GUI():

    def __init__(self):
        self._actions = Queue.Queue()
        
        root = Tk()
        root.geometry("650x400") 

        self._deck = StringVar()
        deck_lbl = Label(root, textvariable=self._deck, anchor=NW, bg="red")
        deck_lbl.place(x = 0, y = 0, width=200, height=400)

        self._lbl_init = Label(text = "tausche          mit")
        self._lbl_init.place(x = 250, y = 0)

        self._txt_swap_1 = Text(root, width=2, height=1)
        self._txt_swap_1.place(x = 300, y = 0)

        self._txt_swap_2 = Text(root, width=2, height=1)
        self._txt_swap_2.place(x = 350, y = 0)

        self._btn_swap = Button(root, text="OK", command=self._on_swap)
        self._btn_swap.place(x = 380, y = 0)

        self._btn_ready = Button(root, text="Fertig", command=self._on_ready)
        self._btn_ready.place(x = 250, y = 40)

        self._lbl_weapon = Label(text = "Angriff:")
        self._lbl_weapon.place(x = 250, y = 100)

        self._txt_weapon = Text(root, width=2, height=1)
        self._txt_weapon.place(x = 300, y = 100)

        self._btn_attack = Button(root, text="Angriff!", command=self._on_attack)
        self._btn_attack.place(x = 340, y = 100)

        self._enemy_card = StringVar()
        enemy_lbl = Label(root, textvariable=self._enemy_card, anchor=NW, bg="red")
        enemy_lbl.place(x = 450, y = 0, width=200, height=400)
               
        start_new_thread(mainloop, ())

    def get_action(self):
        return self._actions.get()

    def show_deck(self, deck):
        self._deck.set(str(deck))

    def show_enemy_card(self, card):
        self._enemy_card.set(str(card))

    def _on_swap(self):
        i1 = int(self._txt_swap_1.get("1.0",'end-1c'))
        i2 = int(self._txt_swap_2.get("1.0",'end-1c'))
        self._actions.put(SwapAction(i1, i2))

    def _on_ready(self):
        self._actions.put(ReadyAction())

    def _on_attack(self):
        weapon = int(self._txt_weapon.get("1.0",'end-1c'))
        self._actions.put(AttackAction(weapon))

    
class Action():

    def __init__(self, type):
        self._type = type

    def get_type(self):
          return self._type

class SwapAction(Action):

    def __init__(self, i1, i2):
        Action.__init__(self, "swap")
        self._i1 = i1
        self._i2 = i2

    def get_index1(self):
        return self._i1

    def get_index2(self):
        return self._i2


class ReadyAction(Action):

    def __init__(self):
        Action.__init__(self, "ready")


class AttackAction(Action):

    def __init__(self, weapon):
        Action.__init__(self, "attack")
        self._weapon = weapon

    def get_weapon(self):
        return self._weapon
        
