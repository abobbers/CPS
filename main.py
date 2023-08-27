import pygame
import sys
import time

width = 500
height = 500
button = pygame.Rect(0,0,200,200)
count = 0
start = time.time()

screen = pygame.display.set_mode([width, height])

while True:
    current = time.time()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONUP:
            if button.collidepoint(pygame.mouse.get_pos()):
                count += 1
    
    if current - start >= 5:
        print(f"{count/(current-start)}cps")
    
    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (0,0,255), button)
    
    pygame.display.flip()
    
    
