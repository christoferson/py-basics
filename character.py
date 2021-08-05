import monster

class Character:
  def __init__(self, name):
    self.name = name

  def attack(self):
    print(self.name + " attacking...")

  def attackMonster(self, m : monster.Monster):
    print("%s attacking %s ..." %(self.name, m.name))
    m.damage(5)