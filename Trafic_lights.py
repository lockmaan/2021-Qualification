from Read import Readata
from Simulation import simulation

streets, intersections, cars, lines, problem = Readata('data/d.txt')

"""[most basic solution]
for i in intersections:
    i.cycle[i.incoming] = 1 

# implimenting the most basic solution ie. 1 tempo for each street """

"""[our function except oversimplified]
    count the occurences of each street in the path of the cars and then give it a coeficient 
    relatively to the number of occurances and then you give it a value in the cycle depending on that
"""

# the implimentation of the function except for 1 concideration all across the simulation


def trafic_lights_simplified(streets, intersections, cars):
    for car in cars:
        for i in range(1, car.n-1):
            streets[car.path[i]].coefi()

    cycles = []
    for i in intersections:
        for street in i.istrts:
            i.cycle[street] = streets[street].coef
        cycles.append(i.cycle)
    return cycles


def trafic_lights_c(car, l, e):
    global streets
    x = l*e
    if x+l <= len(car.path):
        for i in range(x, x+l):
            streets[car.path[i]].coefi()
        for street in streets.values():
            street.ecoef[e].append(
                street.coef
            )
            street.coef = 0
    else:
        pass


def trafic_lights_e(cars, n, e):
    global streets
    for street in streets.values():
        street.ecoef[e] = []

    for car in cars:
        l = car.n//n or 1
        trafic_lights_c(car, l, e)

    for street in streets.values():
        street.ecoef[e] = sum(street.ecoef[e])


def trafic_lights(cars, n):
    global streets
    global intersections
    for e in range(n):
        trafic_lights_e(cars, n, e)

    for street in streets.values():
        street.coef = max(street.ecoef.values())

    cycles = []
    for i in intersections:
        for street in i.istrts:
            i.cycle[street] = streets[street].coef
        cycles.append(i.cycle)
    return cycles


trafic_lights(cars, 10)
print(simulation(streets, intersections, cars, problem))
