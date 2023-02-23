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
    spritesheetimport = False
    scroll = [0, 0]
    addrowbool = False
    addcolumnbool = False
    tile_selection = 0
    while running:
        pygame.display.flip(); clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if addcolumnbool:
                        for i in range(len(blocks)):
                            blocks[i].append(0)
                        addcolumnbool = False
                    elif addrowbool:
                        prevlen = len(blocks[0])
                        blocks.append([])
                        for i in range(prevlen):
                            blocks[-1].append(0)
                        addrowbool = False
        mouse = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        mousepos = [mouse[0][0] + scroll[0], mouse[0][1] + scroll[1]]
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and scroll[0] > 0:
            scroll[0] -= 2
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            scroll[0] += 2
        if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and scroll[1] > 0:
            scroll[1] -= 2
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            scroll[1] += 2
        if keys_pressed[K_LCTRL]:
            if keys_pressed[K_s]:
                global screen
                screen = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
                path = filedialog.asksaveasfilename(initialdir = "./", title = "Save Tilemap", filetypes = (("json file", "*.json"), ("all files", "*.*")))
                with open(f"{path}.json", "w") as outfile:
                    json.dump(blocks, outfile)
                screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
            if keys_pressed[K_n]:
                blocks = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        toolbar_rect = Rect(scroll[0], scroll[1], 300, monitor_size[1])
                
        #display
        screen.fill((60, 60, 60))
        rects = []
        for i in range(len(blocks)):
            rects.append([])
            for j in range(len(blocks[i])):
                rects[i].append(Rect(j*64 + 300 - scroll[0], i*64 - scroll[1], 64, 64))
                if blocks[i][j] != 0:
                    if blocks[i][j] == 1:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (0, 0, 64, 64))
                    elif blocks[i][j] == 2:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (64, 0, 64, 64))
                    elif blocks[i][j] == 3:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (128, 0, 64, 64))
                    elif blocks[i][j] == 4:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (0, 64, 64, 64))
                    elif blocks[i][j] == 5:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (64, 64, 64, 64))
                    elif blocks[i][j] == 6:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (128, 64, 64, 64))
                    elif blocks[i][j] == 7:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (0, 128, 64, 64))
                    elif blocks[i][j] == 8:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (64, 128, 64, 64))
                    elif blocks[i][j] == 9:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (128, 128, 64, 64))
                if rects[i][j].collidepoint((mousepos)) and not toolbar_rect.collidepoint((mousepos)):
                    pygame.draw.rect(screen, (255, 255, 0), (rects[i][j].x - scroll[0], rects[i][j].y - scroll[1], rects[i][j].w, rects[i][j].h), 1)
                    if mouse[1][0]:
                        blocks[i][j] = tile_selection
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (rects[i][j].x - scroll[0], rects[i][j].y - scroll[1], rects[i][j].w, rects[i][j].h), 1)
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 300, monitor_size[1]))
        columnrect = Rect(30, monitor_size[1] - 160, 240, 60)
        rowrect = Rect(30, monitor_size[1] - 80, 240, 60)
        eraserrect = Rect(30, 60, 240, 60)

        if tile_selection != 0:
            pygame.draw.rect(screen, (255, 100, 60), eraserrect)
        else:
            pygame.draw.rect(screen, (255, 255, 255), eraserrect)

        if columnrect.collidepoint((mouse[0])):
            pygame.draw.rect(screen, (255, 0, 0), columnrect)
            addcolumnbool = True
            addrowbool = False
        else:
            pygame.draw.rect(screen, (255, 255, 0), columnrect)

        if rowrect.collidepoint((mouse[0])):
            pygame.draw.rect(screen, (255, 0, 0), rowrect)
            addrowbool = True
            addcolumnbool = False
        else:
            pygame.draw.rect(screen, (255, 255, 0), rowrect)
        
        if eraserrect.collidepoint((mouse[0])) and mouse[1][0]:
            tile_selection = 0

        writetext("Add Column", (70, monitor_size[1] - 140), 32, (0, 0, 0))
        writetext("Add Row", (90, monitor_size[1] - 60), 32, (0, 0, 0))
        writetext("Eraser", (90, 64), 42, (0, 0, 0))
        if spritesheetimport:
            screen.blit(pygame.transform.scale(ssimage, (192, 192)), (50, 180))
            for i in range(len(tilerects)):
                if tilerects[i].collidepoint(mouse[0]):
                    pygame.draw.rect(screen, (255, 255, 0), tilerects[i], 1)
                    if mouse[1][0]:
                        tile_selection = i + 1
        if not spritesheetimport:
            screen = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
            ss = filedialog.askopenfile(initialdir = "./", title = "Import Sprite Sheet", filetypes = (("png file", "*.png"), ("all files", "*.*")))
            ssimage = pygame.image.load(str(ss.name))
            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
            tilerects = []
            for j in range(int(ssimage.get_height()/32)):
                for i in range(int(ssimage.get_width()/32)):
                    tilerects.append(Rect(i*64 + 50, j*64 + 180, 64, 64))
            
            spritesheetimport = True

def openproj():
    running = True
    blocks = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    spritesheetimport = False
    scroll = [0, 0]
    addrowbool = False
    addcolumnbool = False
    tile_selection = 0
    while running:
        pygame.display.flip(); clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if addcolumnbool:
                        for i in range(len(blocks)):
                            blocks[i].append(0)
                        addcolumnbool = False
                    elif addrowbool:
                        prevlen = len(blocks[0])
                        blocks.append([])
                        for i in range(prevlen):
                            blocks[-1].append(0)
                        addrowbool = False
        mouse = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        mousepos = [mouse[0][0] + scroll[0], mouse[0][1] + scroll[1]]
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and scroll[0] > 0:
            scroll[0] -= 2
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            scroll[0] += 2
        if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and scroll[1] > 0:
            scroll[1] -= 2
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            scroll[1] += 2
        if keys_pressed[K_LCTRL]:
            if keys_pressed[K_s]:
                global screen
                screen = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
                path = filedialog.asksaveasfilename(initialdir = "./", title = "Save Tilemap", filetypes = (("json file", "*.json"), ("all files", "*.*")))
                with open(path, "w") as outfile:
                    json.dump(blocks, outfile)
                screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
            if keys_pressed[K_n]:
                blocks = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        toolbar_rect = Rect(scroll[0], scroll[1], 300, monitor_size[1])

        #display
        screen.fill((60, 60, 60))
        rects = []
        for i in range(len(blocks)):
            rects.append([])
            for j in range(len(blocks[i])):
                rects[i].append(Rect(j*64 + 300 - scroll[0], i*64 - scroll[1], 64, 64))
                if blocks[i][j] != 0:
                    if blocks[i][j] == 1:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (0, 0, 64, 64))
                    elif blocks[i][j] == 2:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (64, 0, 64, 64))
                    elif blocks[i][j] == 3:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (128, 0, 64, 64))
                    elif blocks[i][j] == 4:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (0, 64, 64, 64))
                    elif blocks[i][j] == 5:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (64, 64, 64, 64))
                    elif blocks[i][j] == 6:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (128, 64, 64, 64))
                    elif blocks[i][j] == 7:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (0, 128, 64, 64))
                    elif blocks[i][j] == 8:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (64, 128, 64, 64))
                    elif blocks[i][j] == 9:
                        screen.blit(pygame.transform.scale(ssimage, (192, 192)), (j*64 + 300 - scroll[0]*2, i*64 - scroll[1]*2), (128, 128, 64, 64))
                if rects[i][j].collidepoint((mousepos)) and not toolbar_rect.collidepoint((mousepos)):
                    pygame.draw.rect(screen, (255, 255, 0), (rects[i][j].x - scroll[0], rects[i][j].y - scroll[1], rects[i][j].w, rects[i][j].h), 1)
                    if mouse[1][0]:
                        blocks[i][j] = tile_selection
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (rects[i][j].x - scroll[0], rects[i][j].y - scroll[1], rects[i][j].w, rects[i][j].h), 1)
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 300, monitor_size[1]))
        columnrect = Rect(30, monitor_size[1] - 160, 240, 60)
        rowrect = Rect(30, monitor_size[1] - 80, 240, 60)
        eraserrect = Rect(30, 60, 240, 60)

        if tile_selection != 0:
            pygame.draw.rect(screen, (255, 100, 60), eraserrect)
        else:
            pygame.draw.rect(screen, (255, 255, 255), eraserrect)

        if columnrect.collidepoint((mouse[0])):
            pygame.draw.rect(screen, (255, 0, 0), columnrect)
            addcolumnbool = True
            addrowbool = False
        else:
            pygame.draw.rect(screen, (255, 255, 0), columnrect)

        if rowrect.collidepoint((mouse[0])):
            pygame.draw.rect(screen, (255, 0, 0), rowrect)
            addrowbool = True
            addcolumnbool = False
        else:
            pygame.draw.rect(screen, (255, 255, 0), rowrect)
        
        if eraserrect.collidepoint((mouse[0])) and mouse[1][0]:
            tile_selection = 0

        writetext("Add Column", (70, monitor_size[1] - 140), 32, (0, 0, 0))
        writetext("Add Row", (90, monitor_size[1] - 60), 32, (0, 0, 0))
        writetext("Eraser", (90, 64), 42, (0, 0, 0))
        if spritesheetimport:
            screen.blit(pygame.transform.scale(ssimage, (192, 192)), (50, 180))
            for i in range(len(tilerects)):
                if tilerects[i].collidepoint(mouse[0]):
                    pygame.draw.rect(screen, (255, 255, 0), tilerects[i], 1)
                    if mouse[1][0]:
                        tile_selection = i + 1
        if not spritesheetimport:
            screen = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
            ss = filedialog.askopenfile(initialdir = "./", title = "Import Sprite Sheet", filetypes = (("png file", "*.png"), ("all files", "*.*")))
            ssimage = pygame.image.load(str(ss.name))
            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
            tilerects = []
            for j in range(int(ssimage.get_height()/32)):
                for i in range(int(ssimage.get_width()/32)):
                    tilerects.append(Rect(i*64 + 50, j*64 + 180, 64, 64))
            blocks_path = filedialog.askopenfile(initialdir = "./", title = "Import Tile Map", filetypes = (("json file", "*.json"), ("all files", "*.*")))
            if blocks_path != None:
                blocks = json.load(blocks_path)
            else:
                blocks = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            spritesheetimport = True

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
            if text1x < monitor_size[0]/4 + 90:
                text1x += 15
            if text1y < 340:
                text1y += 4
            if text1g > 0:
                text1g -= 20
        else:
            if text1size < 80:
                text1size += 4
            if text1x > monitor_size[0]/4 + 30:
                text1x -= 15
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
            if mouse[1][0]:
                openproj()

        # display
        screen.fill((0, 80, 180))
        writetext("Tilemap Editor", (monitor_size[0]/4 - 120, 60), 140, (80, 0, 0), "Bauhaus 93")
        writetext("Start New Project", (text1x, text1y), int(text1size), (text1g, text1g, text1g))
        writetext("Open Existing Project", (text2x, text2y), int(text2size), (text2g, text2g, text2g))
        writetext("Press Esc To Exit", (monitor_size[0]/2 - 120, monitor_size[1] - 60), color=(0, 0, 0))

if __name__ == "__main__":
    main()
