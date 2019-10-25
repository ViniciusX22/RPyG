from random import randint


class GameObject:
    class_name = ''
    name = ''
    desc = ''
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.name] = self

    def attack(self, foe):
        damage = self.damage
        esquived = False
        msg = ""
        if damage == 0:
            msg = "    {} esquived!\n".format(foe.name)
            esquived = True
        else:
            msg = "    {0} hits {1} and caused {2} of damage!\n".format(
                self.name, foe.name, str(damage))
        foe.health -= damage
        exp = 0
        if foe.health == 0:
            msg += "\n\n {0} killed {1}!\n\n".format(
                self.name, foe.name)
            del(GameObject.objects[foe.name])
            exp += int(damage * 0.60) or 1
        else:
            exp += int(damage * 0.45) or 1
            if not esquived:
                msg += "\n {0} has {1} health points left. \n\n".format(
                    foe.name, str(foe.health))
            else:
                msg += "\n {0} still has {1} health points. \n\n".format(
                    foe.name, str(foe.health))
        self.exp += exp
        if not esquived:
            msg += " {1} gained {0} experience points!\n".format(
                exp, self.name)
        else:
            msg += " {0} gained no experience.\n".format(self.name)
        return msg


class Goblin(GameObject):
    class_name = "Goblin"
    desc = "A foul creature"
    __health = 40
    __exp = 0
    max_damage = 12

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        if health < 0:
            self.__health = 0
        else:
            self.__health = health

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        if exp < 0:
            self.__exp = 0
        else:
            self.__exp = exp

    @property
    def status(self):
        return "Health: {0} | Experience: {1}".format(self.health, self.exp)

    @property
    def damage(self):
        return randint(0, self.max_damage)


class Wizard(GameObject):
    class_name = "Wizard"
    desc = "The master of magic"
    __health = 65
    __exp = 0
    max_damage = 18

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        if health < 0:
            self.__health = 0
        else:
            self.__health = health

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        if exp < 0:
            self.__exp = 0
        else:
            self.__exp = exp

    @property
    def status(self):
        return "Health: {0} | Experience: {1}".format(self.health, self.exp)

    @property
    def damage(self):
        return randint(0, self.max_damage)
