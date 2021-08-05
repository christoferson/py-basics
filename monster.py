class Monster:
  def __init__(self, name, vitality):
    self.name = name
    self.life = vitality
    self.vitality = vitality

  def __str__(self):
     return "Monster({} {}/{})".format(self.name, self.life, self.vitality)

  def damage(self, amount):
     self.life = self.life - amount