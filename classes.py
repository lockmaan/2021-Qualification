class Problem:
    def __init__(self, D, I, S, V, F):
        self.D = D
        # the duration of the simulation
        self.I = I
        #  the number of intersections
        self.S = S
        # the number of streets
        self.V = V
        # the number of cars
        self.F = F
        # the bonus points for each car that reaches
        # its destination before time D


class Street:
    def __init__(self, a, b, ID, l):
        self.a = a
        # the starting intersection
        self.b = b
        # the ending
        self.ID = ID
        # the ID
        self.l = int(l)
        # length
        self.occur = 0

    def occurences(self):
        self.occur += 1


class Intersection:

    def __init__(self, ID):
        self.ID = ID
        self.istrts = []
        # incoming streets
        # (counciously not taking outgoing streets in concideration)

    def incoming(self, street):
        self.istrts.append(street)

    def asigncycle(self, L):
        self.cycle = {
            "{self.istrts}"
        }


class Car:
    def __init__(self, n, L):
        self.n = int(n)
        self.path = []

        for i in L:
            self.path.append(i)


# loop throught all of the streets cheking for thier ID , and then after that we can increment the occurance
