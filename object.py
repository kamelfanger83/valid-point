def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

class Hitbox:
    def __init__(self):
        self.points = []

class RectangularHitbox(Hitbox):
    def __init__(self, half_width, half_height, distance, x_offset = 0, y_offset = 0):
        self.points = []

        x = -half_width
        while x < half_width:
            self.points.append((x + x_offset, half_height + y_offset))
            self.points.append((x + x_offset, -half_height + y_offset))
            x += distance

        self.points.append((half_width + x_offset, half_height + y_offset))
        self.points.append((half_width + x_offset, -half_height + y_offset))

        y = -half_height
        while y < half_height:
            self.points.append((half_width + x_offset, y + y_offset))
            self.points.append((-half_width + x_offset, y + y_offset))
            y += distance

        self.points.append((half_width + x_offset, half_height + y_offset))
        self.points.append((-half_width + x_offset, half_height + y_offset))

class Object:
    def __init__(self, hitbox):
        self.hitbox = hitbox

    def is_valid_big(self, grid):
        for point in self.hitbox.points:
            if grid[int(self.x + point[0] + 10**-11 * sgn(point[0]))][int(self.y + point[1] + 10**-11 * sgn(point[1]))] != 0:
                return False
        return True

    def is_valid(self, grid):
        for point in self.hitbox.points:
            if grid[int(self.x + point[0])][int(self.y + point[1])] != 0:
                return False
        return True

    def on_ground(self, grid):
        min_y = min([point[1] for point in self.hitbox.points])
        for point in self.hitbox.points:
            if abs(point[1] - min_y) < 10**-11:
                if grid[int(self.x + point[0])][int(self.y + point[1] - 10**-10)] == 1:
                    return True
        return False