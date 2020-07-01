import random


start_list = ['Bulbasaur','Charmander','Squirtle','Pikachu']

all_pokemon = ['Bulbasaur','Charmander','Squirtle','Pikachu','Arbok','Raichu','Spearow','Raticate','Kakuna','Butterfree','Metapod']

partner = input("Which type of pokemon you want to choose to be your initial partner? [G]Grass, [F]Fire or [W]Water?")
your_pokemon = []

if partner.lower() == 'g':
    print("You got a Bulbasaur as your partner!")
    your_pokemon.append(start_list[0])
elif partner.lower() == 'f':
    print("You got a Charmander as your partner!")
    your_pokemon.append(start_list[1])
elif partner.lower() == 'w':
    print("You got a Squirtle as your partner!")
    your_pokemon.append(start_list[2])
else:
    print("It seems that you don't like those three pokemons, it doesn't matter, you will get a pikachu!")
    your_pokemon.append(start_list[3])

print("Let's start our adventure! Our goal is to get SEVEN pokemons!")
print("-------------------------------------------------------------")

egg = 0

while len(your_pokemon) < 7:
    if egg > 3:
        print("You find a meow-two, this is the egg of this game. You win!")
        break
    else:
        enemy = all_pokemon[random.randint(0, len(all_pokemon)-1)]
        print("You find a", enemy)
        x = input("[F]ight, [E]scape or [Q]uit the game:")
        if x.lower() == 'f':
            user = random.randint(1, 6)
            ene = random.randint(1, 6)
            print("your value is", user, "and enemy value is ", ene)
            if user >= ene:
                print("You win! ", enemy, "has joined your team!")
                your_pokemon.append(enemy)
                egg += 1
            else:
                print("You are defeated, ", enemy, "has escaped.")
                egg = 0
        elif x.lower() == "q":
            break
        else:
            print("you successfully escaped!")
            egg = 0
        print("now you have ", len(your_pokemon), "pokemons. They are: ", your_pokemon)
        print("-------------------------------------------------------------------------")

print("Game is ended, hope you enjoy it!")



