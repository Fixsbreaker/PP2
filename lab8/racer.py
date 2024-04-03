import random
import pygame

# основные параметры игры в виде размеров окна, цвета и тд.
pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SCORE = 0
COINS = 0

clock = pygame.time.Clock()
background = pygame.image.load('./sprites/AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 15)


# класс монетки с тремя функциями (инициализация, рисования не экране и изменение положения)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./sprites/coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(20, 380),
            550,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.center = (
            random.randint(20, 380),
            550,
        )


# класс врага с тремя функциями (инициализация, рисования не экране и изменение положения)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('./sprites/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(WIDTH // 2, HEIGHT - self.rect.height // 2 - 20),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 0.5
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )


# класс игрока с тремя функциями (инициализация, рисования не экране и изменение положения за счет движения)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('./sprites/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)


# главная функция с игровым циклом
def main():
    COINS = 0
    running = True
    player = Player()
    enemy = Enemy()
    coin = Coin()
    coins = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)
    coins.add(coin)

    while running:
        # SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        coin_text = score_font.render(f"Your coins: {COINS}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(coin_text, (290, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coin.draw(SCREEN)
# проверка обЬектов на столкновение
        if pygame.sprite.spritecollideany(player, enemies):
            running = False
        if pygame.sprite.spritecollideany(player, coins):
            COINS += 1
            coin.update()
            coin.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()