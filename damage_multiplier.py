import random


def get_damage_multiplier(pokemon_level, pokemon_speed):
    if random.randrange(255) < (pokemon_speed / 2):
        multiplier = (2 * pokemon_level + 5) / (pokemon_level + 5)
        return multiplier
    else:
        return 1


def main():
    """
    Just an example. Feel free to try your own, but note that the auto-grader will only be evaluating the function
    get_damage_multiplier() and will completely ignore the main function!
    """

    pokemon_name = input("What is your Pokémon's name?\n")
    pokemon_move_name = input("What attack should " + pokemon_name + " use?\n")
    pokemon_level = int(input("What level is " + pokemon_name + "?\n"))
    pokemon_speed = int(input("What speed is " + pokemon_name + "?\n"))

    number_of_tests = 20

    for test_number in range(number_of_tests):
        # Testing this several times to get a feel for its behavior. Feel free to change the number of tests!
        damage_multiplier = get_damage_multiplier(pokemon_level, pokemon_speed)

        print("Test #{}: {}'s {}'s damage will be multiplied by {}!".format(test_number + 1, pokemon_name,
                                                                            pokemon_move_name.lower(),
                                                                            damage_multiplier))


# DO NOT WRITE CODE BELOW THIS LINE

if __name__ == '__main__':
    main()
