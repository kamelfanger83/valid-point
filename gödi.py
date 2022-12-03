import pygame

gödi_list = []

class Gödi:
    def __init__(self, x = 10, y = 1, r = 0.5):
        self.x = x
        self.y = y
        self.r = r

        self.vert = 1 # 0 = right, 1 = left
        self.speed = 0.1
        self.ang = 0
        self.ang_speed = 10

        gödi_list.append(self)

    def step(self, grid):
        # check if there is a block in front of the gödi
        # if yes, go up
        # if it wants to go up but there is a block, turn around
        # if no, go ahead
        if self.vert == 1:
            if(self.x - self.speed < 0):
                gödil.remove(self)
            self.ang += self.ang_speed
            if grid[int(self.x-self.speed)][int(self.y+self.speed)] == 1:
                if grid[int(self.x)][int(self.y + self.speed)+1] == 1:
                    self.vert = 0
                else:
                    self.y += self.speed
            elif grid[int(self.x-self.speed)][int(self.y)] == 1 or grid[int(self.x-self.speed)+1][int(self.y)] == 1:
                self.x -= self.speed
            else:
                self.y -= self.speed
                if grid[int(self.x)][int(self.y)] == 1:
                    self.y = int(self.y) + 0.99999
        else:
            if(self.x + self.speed > grid.width-2):
                gödi_list.remove(self)
            self.ang -= self.ang_speed
            if grid[int(self.x+self.r*2+self.speed)][int(self.y+self.speed)] == 1:
                if grid[int(self.x+1)][int(self.y + self.speed)+1] == 1:
                    self.vert = 1
                else:
                    self.y += self.speed
            elif grid[int(self.x+self.speed)][int(self.y)] == 1 or grid[int(self.x+self.speed)+1][int(self.y)] == 1:
                self.x += self.speed
            else:
                self.y -= self.speed
                if grid[int(self.x+1)][int(self.y)] == 1:
                    self.y = int(self.y) + 0.99999

    def draw(self, surface, camera, sprite):
        #   rotate gödi image by self.ang then draw that image
        #   rotate around the center of the image

        #   get the rotated image
        rotated_image = pygame.transform.rotate(sprite.image, self.ang)

        #   get the rectangle of the rotated image
        rect = rotated_image.get_rect()

        #   set the center of the rectangle to the center of the image
        rect.center = camera.coords_to_screen(self.x + 1/2, self.y + 1/2, surface)

        #   draw the rotated image
        surface.blit(rotated_image, rect)