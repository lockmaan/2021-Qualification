from Read import Readata


streets, intersections, cars, lines, problem = Readata('data/a.txt')

for car in cars:
    car.car_inter(streets)
# creates a list of the intersections that the car goes through


# implimenting the most basic solution
