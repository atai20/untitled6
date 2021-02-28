import pygame
import time
import math

pygame.init()

clock = pygame.time.Clock()

win = pygame.display.set_mode((600, 600))
run = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
#всю часть выше этого коммента делал я
class Vector(list):
    def __init__(self, *n):
        for i in n:
            self.append(i)

    def __add__(self, other):
        res = Vector()
        if type(other) is Vector:
            assert len(self) == len(other), "Error 0"
            for i in range(len(self)):
                res.append(self[i] + other[i])
            return res
        elif type(other) == int:
            for i in self:
                res.append(i + other)
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
            self.speed = Vector(*[0 for i in range(1)])
        else:
            self.speed = speed
        self.acc = Vector(*[0 for i in range(1)])
        self.mass = mass


    def move(self):
        self.coords = self.coords + self.speed
        return self.coords

    def accelerate(self, dt):
        self.speed = self.speed + self.acc * dt

    def accinc(self, force):  # Зная сообщаемую силу мы получаем нужное ускорение
        self.acc = self.acc + force / self.mass

    def clean_acc(self):
        self.acc = self.acc * 0
#вот эта функция мной сделана которая драв
    def draw(self):
        return pygame.draw.circle(win, PINK,
                           (int(self.coords[0]), int(self.coords[1])), 50, 10)



class InteractionField:
    def __init__(self):  # F - это кастомное взаимодействие, F(p1, p2, r), p1, p2 - точки, r - расстояние между ними
        self.points = []


    def append(self, *args):
        for i in list(args):
            self.points.append(i)
#вся эта всратая функция написана мной которая F
    def F(self, p1, p2):
        if p1.coords[0] > p2.coords[0]:
            p_e_x = p1.coords[0] - p2.coords[0]
        if p1.coords[0] < p2.coords[0]:
            p_e_x = p2.coords[0] - p1.coords[0]
        if p1.coords[1] > p2.coords[1]:
            p_e_y = p1.coords[1] - p2.coords[1]
        if p1.coords[1] < p2.coords[1]:
            p_e_y = p2.coords[1] - p1.coords[1]
        if p1.coords[1] == p2.coords[1]:
            p_e_y = p1.coords[1]
        if p1.coords[0] == p2.coords[0]:
            p_e_x = p1.coords[0]
        p_e_l = math.sqrt(p_e_y**2+p_e_x**2)
        if p_e_l<100:

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
            if p1 == self.points[1]:

                p1.speed[0] = int4_3-int4_2

                p2.speed[0] = -int2_3+p1.speed[0]

                p1.speed[0] = (p_e_x / 100) * p1.speed[0]
                p1.speed[1] = (p_e_y / 100) * p1.speed[0]

                if (p2.coords[1] > p1.coords[1]):
                    p1.speed[1] = -p1.speed[1]
            elif p1 == self.points[0]:
                p1.speed[0] = int4_3 - int4_2

                p2.speed[0] = -int2_3 + p1.speed[0]

                p2.speed[0] = (p_e_x / 100) * p2.speed[0]
                p2.speed[1] = (p_e_y / 100) * p2.speed[0]
                if(p1.coords[1]>p2.coords[1]):
                    p2.speed[1] = -p2.speed[1]
                print(p_e_x)

            # я тут тупил




    def step(self, dt):
        for p in self.points:
            p.clean_acc()
            p.accelerate(dt)
            p.move(dt)

#все ниже написано мной
Ball1 = Point(Vector(100, 290), 2,  speed=Vector(0.1, 0))
Ball2 = Point(Vector(400, 340), 1,  speed=Vector(-0.1, 0))

Space = InteractionField()
Space.append(Ball1, Ball2)

datetime = 0

while run:


    datetime += 1
    Space.F(Ball1, Ball2)
    win.fill(BLACK)
    Space.points[0].draw()
    Space.points[1].draw()
    Space.points[0].move()
    Space.points[1].move()


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



