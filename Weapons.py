class Weapon():

	def __init__(self, damage_points):
                self._damage_points = damage_points

        def get_dp(self):
                return self._damage_points


class Sword(Weapon):

        def __init__(self):
                Weapon.__init__(self, 7)

class Bow(Weapon):

        def __init__(self):
                Weapon.__init__(self, 12)

class Axe(Weapon):

         def __init__(self):
                Weapon.__init__(self, 4)

class Wand(Weapon):

         def __init__(self):
                Weapon.__init__(self, 10)

class Dagger(Weapon):

         def __init__(self):
                Weapon.__init__(self, 5)

class Spear(Weapon):

         def __init__(self):
                Weapon.__init__(self, 6)
