class Vector(list):
    def __init__(self, *n):
        for i in n:
            self.append(i)

    def __add__(self, other):
        res = Vector()
        assert len(self) == len(other) and type(other)==type(self), 'error 0'
        for i in range(len(self)):
            res.append(self[i]+other[i])
        return res

    def __sub__(self, other):
        res = Vector()
        assert len(self) == len(other) and type(other)==type(self), 'error 0'
        for i in range(len(self)):
            res.append(self[i]-other[i])
        return res

    def __pow__(self, other):
        res = Vector()
        if type(other) is Vector:
            assert len(self) == len(other), "Error 0"
            for i in range(len(self)):
                res.append(self[i] ** other[i])
            return res
        elif type(other)==int:
            for i in self:
                res.append(i ** other)
        return res

    def __mod__(self, other):
        return sum((self - other) ** 2) ** 0.5

vector = Vector(1, 2)
vector2 = Vector(2, 57)

print(vector % vector2)

