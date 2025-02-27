def roll_call_dwarves(dwarves):
    if dwarves:
        for dwarf in dwarves:
            print(f"{dwarves.index(dwarf)+1}. {dwarf}")

def summon_captain_planet(planets):
    new_planets = []
    if planets:
        for planet in planets:
            new_planets.append(f"{planet.capitalize()}!")
    print(new_planets)
    return new_planets

def long_planeteer_calls(list):
    if list:
        print(len(list) == 4)
    return len(list) == 4


def find_the_cheese():
    pass
