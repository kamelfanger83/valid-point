# PLATFORMER GAME
# implemented using pygame

import pygame

# initialize pygame
pygame.init()

# create a fullscreen window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# set the window title
pygame.display.set_caption("Platformer Game")

# drid is stored in a 2D list
height = 20
width = 100

# LOWEST ROW IS THE GROUND
# Positive x is right, positive y is up

# the first dimension of the grid represents the x cordinate and thus the left and right on the screen
# the second dimension of the grid represents the y cordinate and thus the up and down on the screen

# create a 2D list
grid = []
for column in range(width):
    grid.append([])
    for row in range(height):
        grid[column].append(0) # append a cell

for row in range(width):
    grid[row][0] = 1

grid[0][1] = 1
grid[0][2] = 1

grid[8][1] = 1
grid[8][2] = 1

grid[1][3] = 1
#grid[7][3] = 1

tile_size = 100

xcen = 0

def map_coords_to_pixels(x, y):
    # convert grid coordinates to pixel coordinates
    return ((x-xcen) * tile_size + screen.get_width()/2, screen.get_height() - y * tile_size)

# load grid images
ground = pygame.image.load(".\sprites\\tile.jpg")
bg = pygame.image.load(".\sprites\\bg.jpg")

#resize images
ground = pygame.transform.scale(ground, (tile_size, tile_size))

# set the player position
# positive x is right and positive y is up
player = [5, 1]

# load player image, left and right
player_left = pygame.image.load(".\sprites\\player_l.png")
player_right = pygame.image.load(".\sprites\\player_r.png")

# load crouch image, left and right
crouch_left = pygame.image.load(".\sprites\\crouch_l.png")
crouch_right = pygame.image.load(".\sprites\\crouch_r.png")

# load jump image, left and right
jump_left = pygame.image.load(".\sprites\\jump_l.png")
jump_right = pygame.image.load(".\sprites\\jump_r.png")

#load walk images, left and right, 1-2
walk_left_1 = pygame.image.load(".\sprites\\walk_l_1.png")
walk_left_2 = pygame.image.load(".\sprites\\walk_l_2.png")
walk_right_1 = pygame.image.load(".\sprites\\walk_r_1.png")
walk_right_2 = pygame.image.load(".\sprites\\walk_r_2.png")

# load crouch walk images, left and right, 1-2
crouch_walk_left_1 = pygame.image.load(".\sprites\\crouch_walk_l_1.png")
crouch_walk_left_2 = pygame.image.load(".\sprites\\crouch_walk_l_2.png")
crouch_walk_right_1 = pygame.image.load(".\sprites\\crouch_walk_r_1.png")
crouch_walk_right_2 = pygame.image.load(".\sprites\\crouch_walk_r_2.png")

# load gödi image
gödi_image = pygame.image.load(".\sprites\\gödi.png")

# resize player image
player_left = pygame.transform.scale(player_left, (tile_size, 2*tile_size))
player_right = pygame.transform.scale(player_right, (tile_size, 2*tile_size))

# resize crouch image
crouch_left = pygame.transform.scale(crouch_left, (tile_size, 2*tile_size))
crouch_right = pygame.transform.scale(crouch_right, (tile_size, 2*tile_size))

# resize jump image
jump_left = pygame.transform.scale(jump_left, (tile_size, 2*tile_size))
jump_right = pygame.transform.scale(jump_right, (tile_size, 2*tile_size))

# resize walk images
walk_left_1 = pygame.transform.scale(walk_left_1, (tile_size, 2*tile_size))
walk_left_2 = pygame.transform.scale(walk_left_2, (tile_size, 2*tile_size))
walk_right_1 = pygame.transform.scale(walk_right_1, (tile_size, 2*tile_size))
walk_right_2 = pygame.transform.scale(walk_right_2, (tile_size, 2*tile_size))

# resize crouch walk images
crouch_walk_left_1 = pygame.transform.scale(crouch_walk_left_1, (tile_size, 2*tile_size))
crouch_walk_left_2 = pygame.transform.scale(crouch_walk_left_2, (tile_size, 2*tile_size))
crouch_walk_right_1 = pygame.transform.scale(crouch_walk_right_1, (tile_size, 2*tile_size))
crouch_walk_right_2 = pygame.transform.scale(crouch_walk_right_2, (tile_size, 2*tile_size))

gödil = []

# resize gödi image
gödi_image = pygame.transform.scale(gödi_image, (tile_size, tile_size))

class gödi:
    def __init__(self, x = 10, y = 1, r = 0.5):
        self.x = x
        self.y = y
        self.r = r

        self.vert = 1 # 0 = right, 1 = left
        self.speed = 0.1
        self.ang = 0
        self.ang_speed = 10

        gödil.append(self)

    def step(self):
        # check if there is a block in front of the gödi
        # if yes, go up
        # if it wants to go up but there is a block, turn around
        # if no, go ahead
        if self.vert == 1:
            if(self.x - self.speed < 0):
                gödil.remove(self)
            self.ang += self.ang_speed
            if grid[int(self.x-self.speed)][int(self.y+self.speed)] == 1:
                if grid[int(self.x)][int(self.y + speed)+1] == 1:
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
            if(self.x + self.speed > width-1):
                gödil.remove(self)
            self.ang -= self.ang_speed
            if grid[int(self.x+self.r*2+self.speed)][int(self.y+self.speed)] == 1:
                if grid[int(self.x+1)][int(self.y + speed)+1] == 1:
                    self.vert = 1
                else:
                    self.y += self.speed
            elif grid[int(self.x+self.speed)][int(self.y)] == 1 or grid[int(self.x+self.speed)+1][int(self.y)] == 1:
                self.x += self.speed
            else:
                self.y -= self.speed
                if grid[int(self.x+1)][int(self.y)] == 1:
                    self.y = int(self.y) + 0.99999

    def draw(self):
        #   rotate gödi image by self.ang then draw that image
        #   rotate around the center of the image

        #   get the rotated image
        rotated_image = pygame.transform.rotate(gödi_image, self.ang)

        #   get the rectangle of the rotated image
        rect = rotated_image.get_rect()

        #   set the center of the rectangle to the center of the image
        rect.center = map_coords_to_pixels(self.x + 1/2, self.y + 1/2)

        #   draw the rotated image
        screen.blit(rotated_image, rect)

gödi()

# set the player direction
direction = "right"

# set the player speed
speed = 0.1
velocity_up = 0
isWalking = False
isCrouching = False

jump_height = 2
gravity = 0.02
jump_speed = 0.35

doubleJumped = True

walkinframe = 1
thisframe = 0
lwpressed = False

hitBoxx = 0.2

gödiTicks = 0

while True:
    #event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            pygame.quit()
            exit(0)

    # get the pressed keys
    pressed_keys = pygame.key.get_pressed()
    # for wasd movement

    isWalking = False
    isCrouching = False

    nlwpressed = False
    if pressed_keys[pygame.K_w]:
        nlwpressed = True
        if lwpressed: pass
        elif not doubleJumped:
            velocity_up = 2/3*jump_speed
            doubleJumped = True
        elif grid[int(player[0])][int(player[1])-1] == 1 and player[1] == int(player[1]):
            velocity_up = jump_speed
            doubleJumped = False

    lwpressed = nlwpressed

    if pressed_keys[pygame.K_s]:
        isCrouching = True
    if pressed_keys[pygame.K_a]:
        # if there is no block to the left
        legal = False
        if isCrouching:
            if grid[int(player[0]-speed-hitBoxx)][int(player[1])] == 0:
                legal = True
        else:
            if grid[int(player[0]-speed-hitBoxx)][int(player[1])] == 0 and grid[int(player[0]-speed-hitBoxx)][int(player[1])+1] == 0:
                legal = True
        if legal:
            player[0] -= speed
            direction = "left"
            isWalking = True
    if pressed_keys[pygame.K_d]:
        # if there is no block to the right
        legal = False
        if isCrouching:
            if grid[int(player[0]+speed+1+hitBoxx)][int(player[1])] == 0:
                legal = True
        else:
            if grid[int(player[0]+speed+hitBoxx)][int(player[1])] == 0 and grid[int(player[0]+speed+hitBoxx)][int(player[1])+1] == 0:
                legal = True
        if legal:
            player[0] += speed
            direction = "right"
            isWalking = True

    velocity_up -= gravity
    if velocity_up > 0:
        if(grid[int(player[0])][int(player[1]+velocity_up)+2] == 0):
            player[1] += velocity_up
    else:
        player[1] += velocity_up

    # check if player is on the ground
    if grid[int(player[0])][int(player[1])] == 1:
        velocity_up = 0
        player[1] = int(player[1])+1
        doubleJumped = True

    if gödiTicks == 1:
        gödiTicks = 0
        for g in gödil:
            g.step()
    gödiTicks += 1

    # draw the background such that height of the image is the height of the screen, repeat the image so whole grid gets covered
    screen.blit(pygame.transform.scale(bg, (screen.get_width(), screen.get_height())), (0, 0))

    # draw the grid
    for row in range(height):
        for column in range(width):
            if grid[column][row] == 1:
                # place tiles so that the bottom left corner of the image is at the bottom left corner of the cell
                # lower left corner of the screen is (0, 0)
                # the first dimension of the grid represents the x cordinate and thus the left and right on the screen
                # the second dimension of the grid represents the y cordinate and thus the up and down on the screen
                screen.blit(ground, map_coords_to_pixels(column, row+1))


    xcen = player[0]

    # draw the player
    if isCrouching:
        if isWalking:
            if walkinframe == 1:
                if direction == "left":
                    screen.blit(crouch_walk_left_1, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
                else:
                    screen.blit(crouch_walk_right_1, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
            else:
                if direction == "left":
                    screen.blit(crouch_walk_left_2, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
                else:
                    screen.blit(crouch_walk_right_2, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
            if thisframe == 10:
                walkinframe = 3 - walkinframe
                thisframe = 0
            thisframe += 1
        else:
            if direction == "left":
                screen.blit(crouch_left, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
            else:
                screen.blit(crouch_right, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
    elif isWalking:
        if direction == "left":
            if walkinframe == 1:
                screen.blit(walk_left_1, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
            else:
                screen.blit(walk_left_2, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
        else:
            if walkinframe == 1:
                screen.blit(walk_right_1, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
            else:
                screen.blit(walk_right_2, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
        if thisframe == 10:
            walkinframe = 3 - walkinframe
            thisframe = 0
        thisframe += 1
    elif velocity_up > 0:
        if direction == "left":
            screen.blit(jump_left, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
        else:
            screen.blit(jump_right, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
    else:
        if direction == "right":
            screen.blit(player_right, map_coords_to_pixels(player[0] - 1/2, player[1]+2))
        else:
            screen.blit(player_left, map_coords_to_pixels(player[0] - 1/2, player[1]+2))

    # draw the gödil
    for g in gödil:
        g.draw()

    # update the screen
    pygame.display.update()

    # set the frame rate
    pygame.time.Clock().tick(60)