class PokeDex:

    def __init__(self):
        
        self.DexList = []

    def addToDex(self, *pokemon):
        for individualPokemon in pokemon:
            self.DexList.append(individualPokemon)

    def pokemonList(self):
        for pokemon in self.DexList:
            print(pokemon.name)
    
    def searchPokemon(self, pokemons):
        for mons in self.DexList:
            if pokemons == mons.name:
                mons.pokeStats()
                break
        else:
            print("This Pokemon has not been discovered yet!")

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

# pikachu.pokeStats()
# bulbasaur.pokeStats()
# charmander.pokeStats()
# squirtle.pokeStats()

kantoDex.addToDex(pikachu, bulbasaur, charmander, squirtle)
#kantoDex.pokemonList()
kantoDex.searchPokemon("Pikachu")