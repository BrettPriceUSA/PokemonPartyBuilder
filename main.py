class PokeDex:

    def __init__(self):
        
        self.DexList = []

    def addToDex(self, pokemon: Pokemon):
        self.DexList.append(pokemon)



class Pokemon:


    def __init__(self, name: str , type: str , id : int):

        self.name = name
        self.type = type
        self.id = id

    def pokeStats(self):
        print(self.name, self.type, self.id)



kantoDex = PokeDex()

pikachu = Pokemon('Pikachu', 'Electric', 25)
bulbasaur = Pokemon("Bulbasaur", "Grass", 1)
charmander = Pokemon("Charmander", "Fire", 4)
squirtle = Pokemon("Squirtle", "Water", 7)

pikachu.pokeStats()
bulbasaur.pokeStats()
charmander.pokeStats()
squirtle.pokeStats()

kantoDex.addToDex(pikachu)