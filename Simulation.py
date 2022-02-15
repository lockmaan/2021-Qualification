from classes import *


def simulation(streets, intersections, cars, problem):
    score = 0
    for car in cars:
        car.destination(streets)

    for T in range(problem.D):
        for intersection in intersections:
            streets = cycling_lights(intersection, T, streets)
        for car in cars:
            car.endstrt(streets)
            if car.at_stop:
                if streets[car.curr].isgreen:
                    car.loc += 1
            else:
                car.loc += 1
            if car.loc == car.dest:
                score += problem.D - T + problem.F

                car.dest = 10000
                # i don't actually know if this will work at all
    return score


def cycling_lights(intersection, T, streets):
    try:
        t = T % sum(list(intersection.cycle.values()))
        streets[list(intersection.cycle.keys())[0]].change()
        i = 0
        while t > 0:

            t -= list(intersection.cycle.values())[i]
            streets[list(intersection.cycle.keys())[i]].change()
            i += 1
            streets[list(intersection.cycle.keys())[i]].change()
    except ZeroDivisionError:
        pass
    except IndexError:
        streets[list(intersection.cycle.keys())[0]].change()
    return streets
