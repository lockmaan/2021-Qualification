from numpy import append


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
        self.coef = 0
        # the street's coefficient
        self.ecoef = {}
        # the street's enstance coeficient

    def coefi(self):
        self.coef += 1


class Intersection:

    def __init__(self, ID):
        self.ID = ID
        self.istrts = []
        self.cycle = {}
        # incoming streets
        # (counciously not taking outgoing streets in concideration)

    def incoming(self, street):
        self.istrts.append(street)

    # def asigncycle(self, L):
    #     for i in range(len(L)) :
    #         self.cycle[self.istrts[i]] = L[i]


class Car:
    def __init__(self, n, L):
        self.n = int(n)
        # number of streets the car goes through is n
        self.path = []
        self.car_inter = []

        for i in L:
            self.path.append(i)
    # loop throught all of the streets cheking for thier ID , and then after that we can increment the occurance

    def car_inter(self, L):
        # L here being the dictionnary of the streets
        # the goal here is to give the car path in intersections as well as streets
        self.ipath = []
        for i in self.path:
            self.ipath.append(L.get(i).b)
