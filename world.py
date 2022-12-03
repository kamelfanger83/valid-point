class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[0 for x in range(height)] for y in range(width)]

    def __getitem__(self, column):
        return self.data[column]

    def __setitem__(self, column, value):
        self.data[column] = value