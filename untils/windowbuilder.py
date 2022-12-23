import os
import pygame

class WindowBuilder:
    def __init__(self, screen):
        self.screen = screen
        self.background = None
        self.text_list = []
        self.image_list = []
        self.button_list = []

    def setBackground(self, background):
        self.background = pygame.image.load(".\\data\\img\\"+background).convert()
        self.background = pygame.transform.scale(self.background, self.screen.get_size())

    def addText(self, text, location, size, color):
        font = pygame.font.SysFont("Arial", size)
        text = font.render(text, True, color)

        self.text_list.append([text, location])

    def addImage(self, path, location):
        image = pygame.image.load(".\\data\\img\\" + path ).convert()
        self.image_list.append([image, location])

    def addButton(self, id, text, textsize, textcolor, location, height, width, backgroundcolor):
        rect = pygame.Rect(location[0], location[1], width, height)

        font = pygame.font.SysFont("Arial", textsize)
        text = font.render(text, True, textcolor)

        self.button_list.append([id, rect, backgroundcolor, text, textsize, location, height, width])
    def draw(self):
        if self.background != None:
            self.screen.blit(self.background, (0, 0))

        for i in range(len(self.text_list)):
            self.screen.blit(self.text_list[i][0], self.text_list[i][1])

        for i in range(len(self.image_list)):
            self.screen.blit(self.image_list[i][0], self.image_list[i][1])

        for i in range(len(self.button_list)):
            pygame.draw.rect(self.screen, self.button_list[i][2], self.button_list[i][1])
            location = [(self.button_list[i][5][0] + self.button_list[i][4]/2), (self.button_list[i][5][1] + (self.button_list[i][6]-self.button_list[i][4])/3)]
            self.screen.blit(self.button_list[i][3], location)

        pygame.display.update()
        pygame.time.Clock().tick(60)

    def getEvents(self):
        events = []

        for i in range(len(self.button_list)):
            startx = self.button_list[i][5][0]
            starty = self.button_list[i][5][1]
            endx = startx + self.button_list[i][7]
            endy = starty + self.button_list[i][6]

            x, y = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0] and x > startx and x < endx and y > starty and y < endy:
                events.append(["button_right_click", self.button_list[i][0]])
            elif pygame.mouse.get_pressed()[2] and x > startx and x < endx and y > starty and y < endy:
                events.append(["button_left_click", self.button_list[i][0]])
            elif pygame.mouse.get_pressed()[1] and x > startx and x < endx and y > starty and y < endy:
                events.append(["button_middle_click", self.button_list[i][0]])

        return events