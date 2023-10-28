class Point:
    def __init__(self, x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color
line = [[i, i] for i in range(1, 2000, 2)]
points = [f'point_{j}' for j in range(1, 1001)]
for _ in range(1000):
    points[_] = Point(line[_][0], line[_][1])
points[1].color = 'yellow'
print([points[i].__dict__ for i in range(1000)])