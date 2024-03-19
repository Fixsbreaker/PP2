import pygame
import os


def play_song(ind):
    pygame.mixer.music.load(songs[ind])
    pygame.mixer.music.play()


pygame.init()


HEIGHT, WEIGHT = 600, 600
screen = pygame.display.set_mode((HEIGHT, WEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption("My first game")


f = pygame.font.Font(None, 36)
text1 = f.render('PLAY - F', True, (0, 0, 0))
text2 = f.render('STOP - G', True, (0, 0, 0))
text3 = f.render('NEXT - H', True, (0, 0, 0))
text4 = f.render('PREVIOUS - J', True, (0, 0, 0))


screen.blit(text1, (10, 50))
screen.blit(text2, (10, 100))
screen.blit(text3, (10, 150))
screen.blit(text4, (10, 200))

pygame.display.update()
songs = []
ind = 0
directory = r"file_name"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.mp3'):
        songs.append(f)
print(songs)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            play_song(ind)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            pygame.mixer.music.stop()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            if ind < len(songs) - 1:
                ind += 1
                play_song(ind)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            if ind > 0:
                ind -= 1
                play_song(ind)


