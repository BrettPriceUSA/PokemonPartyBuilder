class PokeDex:

    def __init__(self):
        
        self.DexList = []

    def addToDex(self, *pokemon):
        for individualPokemon in pokemon:
            self.DexList.append(individualPokemon)

    def pokemonList(self):
        for pokemon in self.DexList:
            print(pokemon.name)
    
    def searchPokemon(self, pokemon_name):
        for mons in self.DexList:
            if pokemon_name == mons.name:
                mons.pokeStats()
                break
        else:
            print("This Pokemon has not been discovered yet!")

    def removePokemon(self, pokemon_name):
        name_found = False
        for mons in self.DexList:
            if pokemon_name == mons.name:
                self.DexLists.remove(mons)
                print(f"{pokemon_name} has been removed from your dex")
                name_found = True
                break
        if name_found == False:
            print(f"{pokemon_name} was not found in your pokedex")


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