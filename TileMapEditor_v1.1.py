import pygame
import winsound
import time as t
import os
import sys
import json
from random import randint
from tkinter import messagebox, filedialog
from pygame import *
from pygame.locals import *

"v 1.1"

pygame.init()
monitorSize = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(monitorSize, FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Level Editor")


def writetext(text, pos, size=30, color=(255, 255, 255), font="Candara"):
    font = pygame.font.SysFont(font, size)
    text = font.render(text, True, color)
    screen.blit(text, pos)
    return text


def main(new):
    running = True
    if not new:
        pass
    while running:
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # display
        screen.fill((20, 20, 20))
        pygame.draw.rect(screen, (120, 120, 120), (0, 0, monitorSize[0], 40))
        writetext("Tilemap Editor",
                  (20, 5), 30, (180, 0, 0), "Bauhaus 93")
        writetext("version 1.1", (monitorSize[0] - 100, 14), 18, (0, 0, 0))

        "Add dropdown menus to the below"
        writetext("Palette", (monitorSize[0] /
                  2 - 120, 12), 18, (0, 0, 0), "Georgia")
        writetext("Edit", (monitorSize[0]/2, 12), 18, (0, 0, 0), "Georgia")
        writetext("About", (monitorSize[0]/2 +
                  100, 12), 18, (0, 0, 0), "Georgia")


def del_dialog():
    t.sleep(0.25)
    running = True
    rect1 = Rect(400, 500, 600, 50)
    rect2 = Rect(400, 600, 600, 50)
    x1 = monitorSize[0]/4 + 30
    x2 = monitorSize[0]/4 + 30
    while running:
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos(), pygame.mouse.get_pressed()

        if rect1.collidepoint(mouse[0]):
            if mouse[1][0]:
                running = False
                t.sleep(0.25)
            if x1 < monitorSize[0]/4 + 60:
                x1 += 10
                if x1 == monitorSize[0]/4 + 40:
                    winsound.Beep(1000, 50)
            else:
                x1 = monitorSize[0]/4 + 60
        else:
            if x1 > monitorSize[0]/4 + 30:
                x1 -= 6
            else:
                x1 = monitorSize[0]/4 + 30

        if rect2.collidepoint(mouse[0]):
            if mouse[1][0]:
                running = False
                pygame.quit()
                sys.exit()
            if x2 < monitorSize[0]/4 + 60:
                x2 += 10
                if x2 == monitorSize[0]/4 + 40:
                    winsound.Beep(1000, 50)
            else:
                x2 = monitorSize[0]/4 + 60
        else:
            if x2 > monitorSize[0]/4 + 30:
                x2 -= 6
            else:
                x2 = monitorSize[0]/4 + 30

        # display
        screen.fill((20, 0, 60))
        for x in range(0, int(monitorSize[0]/50)):
            pygame.draw.line(screen, (40, 0, 120), (x*50, 0),
                             (x*50, monitorSize[1]))
        for y in range(0, int(monitorSize[1]/50)):
            pygame.draw.line(screen, (40, 0, 120), (0, y*50),
                             (monitorSize[0], y*50))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 20, monitorSize[1]))
        pygame.draw.rect(screen, (0, 0, 0),
                         (monitorSize[0] - 20, 0, 20, monitorSize[1]))
        writetext("Tilemap Editor",
                  (monitorSize[0]/4 - 60, 120), 140, (180, 0, 0), "Bauhaus 93")
        writetext("v1.1", (monitorSize[0]*3/4 + 80, 225), 30)
        writetext("Do you really want to quit?",
                  (monitorSize[0]/4 - 40, 350), 80)
        writetext("No", (x1, 500), 60)
        writetext("Yes", (x2, 600), 60)
        if x1 > monitorSize[0]/4 + 50:
            pygame.draw.circle(screen, (255, 255, 255),
                               (rect1.x + 20, rect1.centery), 8)
        if x2 > monitorSize[0]/4 + 50:
            pygame.draw.circle(screen, (255, 255, 255),
                               (rect2.x + 20, rect2.centery), 8)


def main_menu():
    running = True
    bordercolor = [0, 0, 0]
    b_color_dir = ["increasing", "increasing", "increasing"]
    rect1 = Rect(400, 400, 600, 50)
    rect2 = Rect(400, 500, 600, 50)
    rect3 = Rect(400, 600, 600, 50)
    x1 = monitorSize[0]/4 + 30
    x2 = monitorSize[0]/4 + 30
    x3 = monitorSize[0]/4 + 30
    while running:
        pygame.display.flip()
        clock.tick(30)
        for i in range(len(bordercolor)):
            if bordercolor[i] <= 10:
                b_color_dir[i] = "increasing"
            elif bordercolor[i] >= 245:
                b_color_dir[i] = "decreasing"
        for i in range(len(bordercolor)):
            if b_color_dir[i] == "increasing":
                bordercolor[i] += randint(0, 10)
            if b_color_dir[i] == "decreasing":
                bordercolor[i] -= randint(0, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         print(pygame.mouse.get_pos())
        mouse = pygame.mouse.get_pos(), pygame.mouse.get_pressed()

        if rect1.collidepoint(mouse[0]):
            if mouse[1][0]:
                main(True)
            if x1 < monitorSize[0]/4 + 60:
                x1 += 10
                if x1 == monitorSize[0]/4 + 40:
                    winsound.Beep(1000, 50)
            else:
                x1 = monitorSize[0]/4 + 60
        else:
            if x1 > monitorSize[0]/4 + 30:
                x1 -= 6
            else:
                x1 = monitorSize[0]/4 + 30

        if rect2.collidepoint(mouse[0]):
            if x2 < monitorSize[0]/4 + 60:
                x2 += 10
                if x2 == monitorSize[0]/4 + 40:
                    winsound.Beep(1000, 50)
            else:
                x2 = monitorSize[0]/4 + 60
        else:
            if x2 > monitorSize[0]/4 + 30:
                x2 -= 6
            else:
                x2 = monitorSize[0]/4 + 30

        if rect3.collidepoint(mouse[0]):
            if mouse[1][0]:
                del_dialog()
            if x3 < monitorSize[0]/4 + 60:
                x3 += 10
                if x3 == monitorSize[0]/4 + 40:
                    winsound.Beep(800, 50)
            else:
                x3 = monitorSize[0]/4 + 60
        else:
            if x3 > monitorSize[0]/4 + 30:
                x3 -= 6
            else:
                x3 = monitorSize[0]/4 + 30

        # display
        screen.fill((20, 0, 60))
        for x in range(0, int(monitorSize[0]/50)):
            pygame.draw.line(screen, (40, 0, 120), (x*50, 0),
                             (x*50, monitorSize[1]))
        for y in range(0, int(monitorSize[1]/50)):
            pygame.draw.line(screen, (40, 0, 120), (0, y*50),
                             (monitorSize[0], y*50))
        pygame.draw.rect(screen, bordercolor, (0, 0, monitorSize[0], 30))
        pygame.draw.rect(screen, bordercolor, (0, 0, 60, monitorSize[1]))
        pygame.draw.rect(screen, bordercolor,
                         (monitorSize[0] - 60, 0, 60, monitorSize[1]))
        pygame.draw.rect(screen, bordercolor,
                         (0, monitorSize[1] - 30, monitorSize[0], 30))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 20, monitorSize[1]))
        pygame.draw.rect(screen, (0, 0, 0),
                         (monitorSize[0] - 20, 0, 20, monitorSize[1]))
        writetext("Tilemap Editor",
                  (monitorSize[0]/4 - 60, 120), 140, (180, 0, 0), "Bauhaus 93")
        writetext("v1.1", (monitorSize[0]*3/4 + 80, 225), 30)
        writetext("Start New Project", (x1, 400), 60)
        writetext("Open Existing Project", (x2, 500), 60)
        writetext("Exit Application", (x3, 600), 60)
        if x1 > monitorSize[0]/4 + 50:
            pygame.draw.circle(screen, (255, 255, 255),
                               (rect1.x + 20, rect1.centery), 8)
        if x2 > monitorSize[0]/4 + 50:
            pygame.draw.circle(screen, (255, 255, 255),
                               (rect2.x + 20, rect2.centery), 8)
        if x3 > monitorSize[0]/4 + 50:
            pygame.draw.circle(screen, (255, 255, 255),
                               (rect3.x + 20, rect3.centery), 8)


if __name__ == "__main__":
    # main_menu()
    main(True)
