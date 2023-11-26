class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"

    def swap(self):
        temp = self.x
        self.x = self.y
        self.y = temp


def swap(p1, p2):
    temp = p1.x
    p1.x = p2.x
    p2.x = temp

    temp = p1.y
    p1.y = p2.y
    p2.y = temp


pair1 = Pair(20, 10)

print(pair1)

pair1.swap()
print(pair1)

pair2 = Pair(30, 40)
print(pair2)


swap(pair1, pair2)
print(pair1)
print(pair2)
