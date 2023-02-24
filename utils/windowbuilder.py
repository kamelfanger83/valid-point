import os
import pygame

class Button:
    def __init__(self, id, text, textsize, textcolor, location, height, width, backgroundcolor, screen):
        self.rect = pygame.Rect(location[0]*screen.get_width(), location[1]*screen.get_height(), width*screen.get_width(), height*screen.get_height())

        font = pygame.font.SysFont("Arial", textsize)
        self.text = font.render(text, True, textcolor)

        self.id = id
        self.backgroundcolor = backgroundcolor
        self.location = location

    def draw(self, screen):
        pygame.draw.rect(screen, self.backgroundcolor, self.rect)
        # draw text centered
        screen.blit(self.text, (self.rect.centerx - self.text.get_width() / 2, self.rect.centery - self.text.get_height() / 2))

    def is_clicked(self, mousepos):
        if self.rect.collidepoint(mousepos):
            return True
        else:
            return False

class WindowBuilder:
    def __init__(self, screen):
        self.screen = screen
        self.background = None
        self.text_list = []
        self.image_list = []
        self.button_list = []

    def setBackground(self, background):
        self.background = pygame.image.load("./data/img/"+background).convert()
        self.background = pygame.transform.scale(self.background, self.screen.get_size())

    def addText(self, text, location, size, color):
        font = pygame.font.SysFont("Arial", size)
        text = font.render(text, True, color)

        location = (location[0]*self.screen.get_width(), location[1]*self.screen.get_height())

        self.text_list.append([text, location])

    def removeText(self, text, location):
        if ([text, location]) in self.text_list:
            self.text_list.remove([text, location])

    def addImage(self, image, location):
        location = (location[0]*self.screen.get_width(), location[1]*self.screen.get_height())
        self.image_list.append([image, location])

    def addButton(self, id, text, textsize, textcolor, location, width, height, backgroundcolor):
        self.button_list.append(Button(id, text, textsize, textcolor, location, height, width, backgroundcolor, self.screen))

    def draw(self):
        if self.background != None:
            self.screen.blit(self.background, (0, 0))

        for text in self.text_list:
            self.screen.blit(text[0], text[1])

        for button in self.button_list:
            button.draw(self.screen)

        for image in self.image_list:
            self.screen.blit(image[0], image[1])

    def getEvents(self):
        events = []

        for button in self.button_list:
            if button.is_clicked(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    events.append(["left_click", button.id])
                if pygame.mouse.get_pressed()[2]:
                    events.append(["right_click", button.id])
                if pygame.mouse.get_pressed()[1]:
                    events.append(["middle_click", button.id])

        return events