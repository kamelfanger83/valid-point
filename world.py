class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[0 for x in range(height)] for y in range(width)]

    def __getitem__(self, column):
        return self.data[column]

    def __setitem__(self, column, value):
        self.data[column] = value

    def __len__(self):
        return len(self.data)

    def store(self, path):
        with open(path, "w") as f:
            f.write(str(self.width) + " " + str(self.height) + "\n")
            for y in range(self.height):
                for x in range(self.width):
                    f.write(str(self.data[x][y]))
                f.write("\n")

    def load(self, path):
        with open(path, "r") as file:
            lines = file.readlines()
            
            self.width = int(lines[0].split(" ")[0])
            self.height = int(lines[0].split(" ")[1])

            self.data = [[0 for x in range(self.height)] for y in range(self.width)]

            for line in lines:
                if line != lines[0]:
                    x = int(line.split(" ")[0])
                    y = int(line.split(" ")[1])

                    type = int(line.split(" ")[2])

                    self.data[x][y] = type

            for x in range(10):
                self.data[x][0] = 1
