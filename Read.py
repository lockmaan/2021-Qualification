from re import X
from classes import *


def Readata(file_path):
    streets = {}
    intersections = []
    cars = []
    lines = open(file_path).readlines()
    problem = Problem(*list(map(int, lines[0].split())))

    for i in range(problem.I):
        intersections.append(Intersection(i))
        # giving the intersections thier ID , which happens to be a number

    for i in lines[1: problem.S + 1]:
        L = i.split()
        streets[L[2]] = Street(*L)
        # constructing a list of all the streets
        intersections[int(L[1])].incoming(L[2])
        # adding the street to the list of the incoming streets(intersection object)

    for i in lines[problem.S + 1:]:
        L = i.split()
        cars.append(
            # perfect fit for pop
            # pops first element which is the number of streets the car passes through
            # the rest of the elements are the streets the car goes through
            Car(L.pop(0), L)
        )

    return streets, intersections, cars, lines, problem
