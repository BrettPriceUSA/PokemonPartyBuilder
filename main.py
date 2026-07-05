class Pokemon:
    def __init__(self, name, type, level, hp):
        self.name = name
        self.type = type
        self.level = level
        self.hp = hp

    def DexRead(self):
        pass



pikachu = Pokemon('Pikachu', 'Electric', 5, 15)
print (pikachu.level)