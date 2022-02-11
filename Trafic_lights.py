from Read import Readata


streets, intersections, cars, lines, problem = Readata('data/a.txt')

"""[most basic solution]
for i in intersections:
    i.cycle[i.incoming] = 1 

# implimenting the most basic solution ie. 1 tempo for each street """

"""[our function except oversimplified]
    count the occurences of each street in the path of the cars and then give it a coeficient 
    relatively to the number of occurances and then you give it a value in the cycle depending on that
"""

# the implimentation of the function except for 1 concideration all across the simulation


def trafic_lights_1(streets, intersections, cars):
    for car in cars:
        for i in range(1, car.n-1):
            streets[car.path[i]].coefi()

    cycles = []
    for i in intersections:
        for street in i.istrts:
            i.cycle[street] = streets[street].coef
        cycles.append(i.cycle)
    return cycles


print(trafic_lights_1(streets, intersections, cars))
