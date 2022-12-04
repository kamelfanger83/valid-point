class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[0 for x in range(height)] for y in range(width)]

    def __getitem__(self, column):
        return self.data[column]

    def __setitem__(self, column, value):
        self.data[column] = value

    def store(self, path):
        with open(path, "w") as f:
            f.write(str(self.width) + " " + str(self.height) + "\n")
            for y in range(self.height):
                for x in range(self.width):
                    f.write(str(self.data[x][y]))
                f.write("\n")

    def load(self, path):
        with open(path, "r") as f:
            self.width, self.height = [int(x) for x in f.readline().split()]
            self.data = [[0 for x in range(self.height)] for y in range(self.width)]
            for y in range(self.height):
                line = f.readline()
                for x in range(self.width):
                    self.data[x][y] = int(line[x])