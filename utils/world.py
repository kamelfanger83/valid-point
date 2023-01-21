import spawner
import gödi
import respawnpoint
import winblock
import sand

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[0 for x in range(height)] for y in range(width)]
        self.metadata = []

    def __getitem__(self, column):
        return self.data[column]

    def __setitem__(self, column, value):
        self.data[column] = value

    def __len__(self):
        return len(self.data)


    def load(self, path, tile_size, ud_list):
        with open(path, "r") as file:
            lines = file.readlines()

            self.width = int(lines[0].split(" ")[0])
            self.height = int(lines[0].split(" ")[1])
            for k in range(1, 5):
                self.metadata.append([float(n) for n in lines[k].split(" ")[0]])

            self.data = [[0 for x in range(self.height)] for y in range(self.width)]

            for line in lines:
                if line != lines[0]:
                    x = float(line.split(" ")[0])
                    y = float(line.split(" ")[1])

                    type = int(line.split(" ")[2])

                    if type == 3:
                        spawner.Spawner(x, y, 100, tile_size, self, ud_list)
                    elif type == 4:
                        gödi.Gödi(x, y, "./data/img/gödi.png", ud_list)
                    elif type == 5:
                        respawnpoint.Respawnpoint(x, y, "./data/img/respawnpoint.jpg", ud_list)
                    elif type == 6:
                        winblock.Winblock(x, y, "./data/img/winblock.jpg", ud_list)
                    else:
                        self.data[int(x)][int(y)] = type
    def store(self, path):
        print("storing")
        # write out the grid to a file
        with open(path, "w") as file:
            file.write(str(self.width) + " " + str(self.height) + "\n")
            for y in range(self.height):
                for x in range(self.width):
                    if self[x][y] != 0:
                        file.write(str(x)+" "+str(y)+" "+str(self[x][y])+"\n")
            for spawnero in spawner.spawner_list:
                file.write(str(spawnero.x)+" "+str(spawnero.y)+" 3\n")
            for gödio in gödi.gödi_list:
                #write location with 3 decimal places
                file.write(str(round(gödio.x, 3))+" "+str(round(gödio.y, 3))+" 4\n")
            for respawnpointo in respawnpoint.respawnpoint_list:
                file.write(str(respawnpointo.x)+" "+str(respawnpointo.y)+" 5\n")
            for winblocko in winblock.winblock_list:
                file.write(str(winblocko.x)+" "+str(winblocko.y)+" 6\n")
