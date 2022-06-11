import pygame
from pygame import *
from pygame.locals import *
import sys, datetime, json
from tkinter import messagebox, filedialog

pygame.init()
monitor_size = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
pygame.display.set_caption("Tilemap")
clock = pygame.time.Clock()

def writetext(text, pos, size=30, color=(255, 255, 255), font="Candara"):
    font = pygame.font.SysFont(font, size)
    text = font.render(text, True, color)
    screen.blit(text, pos)
    return text

def newproj():
    running = True
    blocks = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    rects = []
    while running:
        pygame.display.flip(); clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        mouse = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LCTRL]:
            if keys_pressed[K_s]:
                global screen
                screen = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
                path = filedialog.asksaveasfilename(initialdir = "./", title = "Save Tilemap", filetypes = (("json file", "*.json"), ("all files", "*.*")))
                with open(f"{path}.json", "w") as outfile:
                    json.dump(blocks, outfile)
                screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
        #display
        screen.fill((60, 60, 60))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 300, monitor_size[1]))
        for i in range(len(blocks)):
            rects.append([])
            for j in range(len(blocks[i])):
                rects[i].append(Rect(j*32 + 300, i*32, 32, 32))
                if blocks[i][j] != 0:
                    pass
                if rects[i][j].collidepoint((mouse[0])):
                    pygame.draw.rect(screen, (255, 255, 0), rects[i][j], 3)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), rects[i][j], 3)

def main():
    running = True
    text1size = 60
    text1x = monitor_size[0]/4 + 100
    text1y = 340
    text1g = 0
    text2size = 60
    text2x = monitor_size[0]/4 + 50
    text2y = 440
    text2g = 0
    while running:
        pygame.display.flip(); clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         print(pygame.mouse.get_pos())
        mouse = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        rect1 = Rect(420, 340, 440, 80)
        if not rect1.collidepoint((mouse[0])):
            if text1size > 60:
                text1size -= 4
            if text1x < monitor_size[0]/4 + 100:
                text1x += 12
            if text1y < 340:
                text1y += 4
            if text1g > 0:
                text1g -= 20
        else:
            if text1size < 80:
                text1size += 4
            if text1x > monitor_size[0]/4 + 40:
                text1x -= 12
            if text1y > 320:
                text1y -= 4
            if text1g < 200:
                text1g += 20
            if mouse[1][0]:
                newproj()

        rect2 = Rect(360, 440, 530, 80)
        if not rect2.collidepoint((mouse[0])):
            if text2size > 60:
                text2size -= 4
            if text2x < monitor_size[0]/4 + 50:
                text2x += 14
            if text2y < 440:
                text2y += 4
            if text2g > 0:
                text2g -= 20
        else:
            if text2size < 80:
                text2size += 4
            if text2x > monitor_size[0]/4 - 20:
                text2x -= 14
            if text2y > 420:
                text2y -= 4
            if text2g < 200:
                text2g += 20

        # display
        screen.fill((0, 80, 180))
        writetext("Tilemap Editor", (monitor_size[0]/4 - 120, 60), 140, (80, 0, 0), "Bauhaus 93")
        writetext("Start New Project", (text1x, text1y), int(text1size), (text1g, text1g, text1g))
        writetext("Open Existing Project", (text2x, text2y), int(text2size), (text2g, text2g, text2g))
        writetext("Press Esc To Exit", (monitor_size[0]/2 - 120, monitor_size[1] - 60), color=(0, 0, 0))

if __name__ == "__main__":
    main()