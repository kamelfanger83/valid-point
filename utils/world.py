import random

import spawner
import gödi
import respawnpoint
import winblock
import sand
import pygame

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[0 for x in range(height)] for y in range(width)]
        self.metadata = {}

    def __getitem__(self, column):
        return self.data[column]

    def __setitem__(self, column, value):
        self.data[column] = value

    def __len__(self):
        return len(self.data)


    def load(self, path, tile_size, ud_list):
        with open(path, "r") as file:
            lines = file.readlines()

            self.width = int(lines[1].split(" ")[0])
            self.height = int(lines[1].split(" ")[1])

            self.metadata = {
                "respawn_point": ["9", "1"],
                "speed": "0.1",
                "respawn": "0",
                "crouch_speed": "0.2",
                "hitbox": ["0.2", "0.85"],
                "creative": "0",
                "invincible": "0",
                "music": "./ data / music / jumpandgian.wav"
            }

            i = 2
            while lines[i] != "\n":
                splitline = lines[i].split(" ")
                if len(splitline) == 2:
                    self.metadata[splitline[0][:-1]] = str(splitline[1])[:-1]
                else:
                    self.metadata[splitline[0][:-1]] = [str(k) for k in splitline[1:]]
                    self.metadata[splitline[0][:-1]][-1] = self.metadata[splitline[0][:-1]][-1][:-1]
                i += 1

            self.data = [[0 for x in range(self.height)] for y in range(self.width)]

            for i_line in range(i+1, len(lines)):
                line = lines[i_line]
                x = float(line.split(" ")[0])
                y = float(line.split(" ")[1])

                type = int(line.split(" ")[2])

                if type == 3:
                    print(line)
                    spawner.Spawner(int(x), int(y), int(line.split(" ")[3]), int(line.split(" ")[4]), tile_size, self, ud_list)
                elif type == 4:
                    gödi.Gödi(x, y, "./data/img/gödi.png", ud_list)
                elif type == 5:
                    respawnpoint.Respawnpoint(x, y, "./data/img/respawnpoint.jpg", ud_list)
                elif type == 6:
                    winblock.Winblock(x, y, "./data/img/winblock.jpg", ud_list)
                else:
                    self.data[int(x)][int(y)] = type
    def store(self, name):
        # write out the grid to a file
        with open("./data/maps/" + name + ".gr", "w") as file:
            file.write(name)
            file.write(str(self.width) + " " + str(self.height) + "\n")
            file.write("respawn_point:" + input("Respawn x: ") + " " + input("Respawn y: ") + "\n")
            file.write("speed:" + input("Player speed: ") + "\n")
            file.write("crouch_speed:" + input("Player crouch speed: ") + "\n")
            file.write("hitbox:" + str(self.metadata["hitbox"][0]) + " " + str(self.metadata["hitbox"][1]) + "\n")
            file.write("0\n")

            for y in range(self.height):
                for x in range(self.width):
                    if self[x][y] != 0 and self[x][y] != 3:
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

        # set pygame window back to fullscreen
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)