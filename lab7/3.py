import pygame

pygame.init()
clock = pygame.time.Clock()

HEIGHT, WEIGHT = 600, 600
screen = pygame.display.set_mode((HEIGHT, WEIGHT))
pygame.display.set_caption("My first game")

x, y = HEIGHT / 2, WEIGHT / 2
radius = 25
step = 20
fps = 30

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if y - radius > 0:
        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            if y - radius == 0:
                pass
            else:
                y -= step
    if y + radius < HEIGHT:
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            if y + radius == HEIGHT:
                pass
            else:
                y += step
    if x - radius > 0:
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            if x - radius == 0:
                pass
            else:
                x -= step
    if x + radius < WEIGHT:
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            if x + radius == WEIGHT:
                pass
            else:
                x += step
    if pressed[pygame.K_q]:
        running = False

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()

    clock.tick(fps)