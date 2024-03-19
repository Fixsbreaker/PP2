import pygame
import datetime


def rotate_for_second(img_sec, center_image_sec, angle_for_sec):
    w, h = img_sec.get_size()
    img2 = pygame.Surface((w * 2, h * 2), pygame.SRCALPHA)
    img2.blit(img_sec, (w - center_image_sec[0], h - center_image_sec[1]))
    return pygame.transform.rotate(img2, angle_for_sec * -1)


def rotate_for_minutes(img_min, center_image_min, angle_for_min):
    w, h = img_min.get_size()
    img2 = pygame.Surface((w * 2, h * 2), pygame.SRCALPHA)
    img2.blit(img_min, (w - center_image_min[0], h - center_image_min[1]))
    return pygame.transform.rotate(img2, angle_for_min * -1)


pygame.init()
screen = pygame.display.set_mode([829, 836])
screen.fill((255, 255, 255))
pygame.display.set_caption("Вращение")
clock_img = pygame.image.load(r'/Users/alnurkunbolov/PP2_id/PP2/lab7/src/main-clock.png')
screen.blit(clock_img, (0, 0))


image_sec = pygame.image.load(r"/Users/alnurkunbolov/PP2_id/PP2/lab7/src/left-hand.png").convert_alpha()
image_sec = pygame.transform.rotate(image_sec, 90)
image_min = pygame.image.load(r"/Users/alnurkunbolov/PP2_id/PP2/lab7/src/right-hand.png").convert_alpha()
image_min = pygame.transform.rotate(image_min, 90)
center_window = (414.5, 418)
angle_for_sec = datetime.datetime.now().second * 6
angle_for_min = datetime.datetime.now().minute * 6
center_image_min = (90, 205)
center_image_sec = (70, 273)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    now = datetime.datetime.now()
    image_for_sec = rotate_for_second(image_sec, center_image_sec, angle_for_sec)
    image_for_min = rotate_for_minutes(image_min, center_image_min, angle_for_min)
    rect_sec = image_for_sec.get_rect()
    rect_min = image_for_min.get_rect()
    rect_sec.center = center_window
    rect_min.center = center_window
    screen.blit(clock_img, (0, 0))
    screen.blit(image_for_sec, rect_sec)
    screen.blit(image_for_min, rect_min)
    angle_for_sec = now.second * 6
    angle_for_min = now.minute * 6

    pygame.display.update()

pygame.quit()