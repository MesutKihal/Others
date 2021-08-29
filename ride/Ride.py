import pygame
import random
import sys


def MainMenu():
    pygame.init()
    white = (255,255,255)
    black = (0,0,0)
    width = 1024
    height = 400
    fps = 45
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RIDE")
    font = pygame.font.SysFont('rod', 45)
    title_font = pygame.font.SysFont('arialblack', 72, bold=False)
    bg = pygame.image.load('bg_0.jpg')
    start_x = 400
    start_y = 200
    exit_x = 400
    exit_y = 250
    while True:
        clock.tick(fps)
        title_txt = title_font.render('RIDE' , True, black)
        start_txt = font.render('PLAY' , True, white)
        exit_text = font.render('EXIT', True, white)
        window.blit(bg, (0,0))
        pygame.draw.rect(window ,black ,(start_x,start_y, 200, 40))
        pygame.draw.rect(window ,black ,(exit_x,exit_y, 200, 40))
        window.blit(title_txt, (400, 100))
        window.blit(start_txt, (start_x+50, start_y))
        window.blit(exit_text, (exit_x+50, exit_y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if start_x <= mouse[0] <= start_x+200 and start_y <= mouse[1] <= start_y+200:
                Play()
                break
            if exit_x <= mouse[0] <= exit_x+200 and exit_y <= mouse[1] <= exit_y+200:
                sys.exit()
            

def Play():
    pygame.init()

    #Variables
    white = (255,255,255)
    black = (0,0,0)
    light_blue = (153,217,234)
    width = 1024
    height = 400
    fps = 40
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RIDE")
    font = pygame.font.SysFont('platino', 28)
    tip_font = pygame.font.SysFont('courier', 24, bold=True)
    msg_font = pygame.font.SysFont('platino', 40, bold=True)
    replay_btn = pygame.image.load('replay.png')
    bg = [pygame.image.load('bg_0.jpg'),
          pygame.image.load('bg_1.jpg'),
          pygame.image.load('bg_2.jpg'),]
    obstacles = [pygame.image.load('rock.png'),
                 pygame.image.load('rocks_2.png'),
                 pygame.image.load('rocks_3.png'),
                 pygame.image.load('rocks_4.png'),]


    jumpCount = 0
    peak = 120
    ground = 180
    score = 0
    distance = 0
    levels = {range(300):5, range(600,1200):6, range(1200,2100):7, range(2100,3400):9, range(3400,5000):10}
    bg_x = 0
    bg_y = 0
    temp_x = 1024
    temp_y = 230
    vel = 5
    
    #Classes
    class MainChar(object):
        def __init__(self, x, y, w, h, vel):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.vel = vel
            self.index = 0
            self.animation = [pygame.image.load('0.gif'),
                              pygame.image.load('1.gif'),
                              pygame.image.load('2.gif'),
                              pygame.image.load('3.gif'),
                              pygame.image.load('4.gif'),
                              pygame.image.load('5.gif'),]
        def draw(self, screen):
            if not isJump:
                if self.index <= len(self.animation) - 1:
                    screen.blit(self.animation[self.index],(self.x,self.y))
                    self.index += 1
                else:
                    self.index = 0
                    screen.blit(self.animation[self.index],(self.x,self.y))
            else:
                self.index = 5
                screen.blit(self.animation[self.index],(self.x,self.y))

                

    knight = MainChar(330,180,80,90,5)
    temp = random.choice(obstacles)
    def replay_menu():
        while True:
            clock.tick(fps)
            pygame.draw.circle(screen, white, (522, 232), 32)
            screen.blit(replay_btn, (490, 200))
            if gameover and score >= 5000: screen.blit(congrats, (380,130))
            if gameover and score < 5000: screen.blit(itsover, (430,130))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    if 490 < mouse[0] < 554 and 200 < mouse[1] < 264:
                        Play()
                        break
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    Play()
                    break
    
    def drawScreen():
        for i in range(3):
            screen.blit(bg[i], (bg_x+(1024*i),bg_y))
        screen.blit(score_txt, (600, 0))
        if score <= 30:screen.blit(tip_text, (100,100))
        knight.draw(screen)
        screen.blit(temp, (temp_x, temp_y))
        pygame.display.update()

    gameover = False
    isJump = False
    while True:
        clock.tick(fps)
        score_txt = font.render('Score: '+str(score), True, black)
        tip_text = tip_font.render('Jumpover rocks using UP_ARROW or SPACEBAR', True, black)
        congrats = msg_font.render('CONGRATULATIONS!!', True, black)
        itsover = msg_font.render('GAME OVER', True, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                isJump = True
            if keys[pygame.K_DOWN]:
                pass
        #HorseJump
        if isJump == True:
            if jumpCount <= peak:
                jumpCount += knight.vel
                knight.y -= knight.vel
            if jumpCount >= peak and knight.y < ground:
                knight.y += knight.vel
            if knight.y >= ground:
                jumpCount = 0
                isJump = False
        #Obstacles
        if temp_x >= 0:
            temp_x -= vel
        else:
            temp = random.choice(obstacles)
            temp_x = 1024
            
        if knight.x <= temp_x <= knight.x+knight.w and knight.y <= temp_y <= knight.y+knight.h:
            gameover = True
            replay_menu()
            break
        #GroundMotion
        if bg_x + width <= 1024:
            bg_x -= vel
        if bg_x + width*2 <= 1024:
            temp_0 = bg[0]
            temp_1 = bg[1]
            bg.pop(0)
            bg.append(temp_0)
            bg.pop(1)
            bg.append(temp_1)
            bg_x = 0
        #ScoreCount
        if distance % 2 == 0:
            score += 1
        for lvl in levels.keys():
            if score in lvl:
                vel = levels.get(lvl)
                if not vel == 10:
                    knight.vel = vel
                else:
                    knight.vel = 9
                break
        #Gameover
        if score >= 5000:
            gameover = True
        distance += 1
        drawScreen()
        if gameover == True:
            replay_menu()
    pygame.quit()
MainMenu()
