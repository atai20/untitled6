import pygame
class Vector(list):
    def __init__(self, *n):
        for i in n:
            self.append(i)

    def __add__(self, other):
        res = Vector()
        if type(other) is Vector:
            assert len(self) == len(other), "Error 0"
            for i in range(len(self)):
                res.append(self[i] - other[i])
            return res
        elif type(other) == int:
            for i in self:
                res.append(i - other)
        return res

    def __sub__(self, other):
        res = Vector()
        if type(other) is Vector:
            assert len(self) == len(other), "Error 0"
            for i in range(len(self)):
                res.append(self[i] - other[i])
            return res
        elif type(other) == int:
            for i in self:
                res.append(i - other)
        return res

    def __pow__(self, other):
        res = Vector()
        if type(other) is Vector:
            assert len(self) == len(other), "Error 0"
            for i in range(len(self)):
                res.append(self[i] ** other[i])
            return res
        elif type(other) == int:
            for i in self:
                res.append(i ** other)
        return res

    def __mod__(self, other):
        return sum((self - other) ** 2) ** 0.5

    def __mul__(self, other):
        res = Vector()
        if type(other) is Vector:
            assert len(self) == len(other), "Error 0"
            for i in range(len(self)):
                res.append(self[i] * other[i])
            return res
        elif type(other) == int:
            for i in self:
                res.append(other*i)
        return res

class Point():
    def __init__(self, coords, mass = 1.0, speed=None):
        self.coords = coords
        if speed is None:
            self.speed = Vector(*[0 for i in range(len(coords))])
        else:
            self.speed = speed
        self.acc = Vector(*[0 for i in range(len(coords))])
        self.mass = mass

    def move(self, dt):
        self.coords =  self.speed*dt
        return self.coords

    def accelerate(self, dt):
        self.speed = self.speed + self.acc * dt

    def accinc(self, force):  # Зная сообщаемую силу мы получаем нужное ускорение
        self.acc = self.acc + force / self.mass

    def clean_acc(self):
        self.acc = self.acc * 0



class InteractionField:
    def __init__(self):  # F - это кастомное взаимодействие, F(p1, p2, r), p1, p2 - точки, r - расстояние между ними
        self.points = []


    def append(self, *args, **kwargs):
        self.points.append(Point(*args, **kwargs))

    def F(self, p1, p2, r):
        if r == 0:
            int1_1 = p1.mass
            int1_2 = p2.mass
            int1_3 = p1.mass*p1.speed[0] + p2.mass*p2.speed[0]
            int2_1 = 1
            int2_2 = -1
            int2_3 = p2.speed[0]-p1.speed[0]
            int3_1 = int1_1+int2_1
            int3_2 = int1_2+int2_2
            int3_3 = int1_3+int2_3
            int4_1 = int3_1/int3_1
            int4_2 = int3_2/int3_1
            int4_3 = int3_3/int3_1

            p1.speed[0] = int4_3-int4_2
            p1.speed[1] = -int2_3+p1.speed[0]

            # я тут тупил




    def step(self, dt):
        for p in self.points:
            p.clean_acc()
            p.accelerate(dt)
            p.move(dt)

Ball1 = Point(Vector(100, 300), 2,  speed=Vector(1, 5))
Ball2 = Point(Vector(100, 300), 1,  speed=Vector(-1, 5))

Space = InteractionField()
Space.F(Ball1, Ball2, 0)




