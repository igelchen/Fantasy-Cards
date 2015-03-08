class Character():

    def __init__(self, hp, range_points, melee_points, magic_points):
        self._hp = hp
        self._range_points = range_points
        self._melee_points = melee_points
        self._magic_points = magic_points

    def get_hp(self):
        return self._hp

    def reduce_hp(self, value):
        if self._hp < value:
            self._hp = 0
        else:
            self._hp = self._hp-value

    def is_alive(self):
        return self._hp != 0

    

class Orc(Character):

    def __init__(self, range_points, melee_points, magic_points):
         Character.__init__(self, 100, range_points, melee_points, magic_points)


class Dwarf(Character):

    def __init__(self, range_points, melee_points, magic_points):
         Character.__init__(self, 100, range_points, melee_points, magic_points)
         

class Dragon(Character):

    def __init__(self, range_points, melee_points, magic_points):
         Character.__init__(self, 100, range_points, melee_points, magic_points)


class Wizard(Character):

    def __init__(self, range_points, melee_points, magic_points):
         Character.__init__(self, 100, range_points, melee_points, magic_points)


class Elf(Character):

    def __init__(self, range_points, melee_points, magic_points):
         Character.__init__(self, 100, range_points, melee_points, magic_points)
