# Learnt from https://www.edureka.co/blog/snake-game-with-pygame/ (may be slightly edited)
import pygame

pygame.init()
display = pygame.display.set_mode((400, 400))
pygame.display.update()
pygame.display.set_caption('Snake by rhm-99')

black = (0, 0, 0)
white = (255, 255, 255)

game_over = False
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

        x1 += x1_change
        y1 += y1_change
        display.fill(black)
    pygame.draw.rect(display, white, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit
quit()
