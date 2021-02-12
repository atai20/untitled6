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
    def __init__(self, F):  # F - это кастомное взаимодействие, F(p1, p2, r), p1, p2 - точки, r - расстояние между ними
        self.points = []
        self.F = F

    def append(self, *args, **kwargs):
        self.points.append(Point(*args, **kwargs))
    
    def step(self, dt):
        for p in self.points:
            p.clean_acc()
            p.accelerate(dt)
            p.move(dt)


Space = InteractionField(Vector(1, 0))

Space.step(1)
Ball = Point(Vector(100, 300), speed=Vector(2, 5))

