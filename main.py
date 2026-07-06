class PokeDex:

    def __init__(self, name: str, type : str , id : int):
        self.name = name
        self.type = type
        self.id = id
        
        DexList = []


class Pokemon(PokeDex):


    def __init__(self, name: str , type: str , id : int, level: int):

        self.name = name
        self.type = type
        self.id = id
        self.level = level

    def pokeStats(self):
        print(self.name, self.type, self.level, self.hp, self.id)



DexList.append(Pokemon('Pikachu', 'Electric', 5, 15, 25))
bulbasaur = Pokemon("Bulbasaur", "Grass", 5, 20, 1)
charmander = Pokemon("Charmander", "Fire", 5, 15, 4)
squirtle = Pokemon("Squirtle", "Water", 5, 20, 7)

pikachu.pokeStats()
bulbasaur.pokeStats()
charmander.pokeStats()
squirtle.pokeStats