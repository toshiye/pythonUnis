#get_*, set_*...

"""
class Projetil(object):
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    def get_velocidade(self):
        return self.alcance / self.tempo

moab = Projetil(alcance=10000, tempo=60)
print moab.get_velocidade()
"""

class Projetil(object):
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    @property
    def velocidade(self):
        return self.alcance / self.tempo

moab = Projetil(alcance=10000, tempo=60)
print moab.velocidade