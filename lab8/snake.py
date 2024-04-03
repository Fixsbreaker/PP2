import random
import time
import pygame

pygame.init()
WIDTH, HEIGHT = 760, 760
HEAD_COLOR = (19, 213, 213)
BOARD_COLOR = (246, 197, 124)
BLACK = (0, 0, 0)
POISON_COLOR = (255, 0, 0)
FOOD_COLOR = (78, 229, 73)
SNAKE_COLOR = (19, 26, 215)
BG_SOUND = 'sounds/background.mp3'
FOOD_SOUND = pygame.mixer.Sound('sounds/food.mp3')
GAME_OVER_SOUND = 'sounds/game_over.mp3'
POISON_SOUND = pygame.mixer.Sound('sounds/poison.mp3')

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
pygame.display.set_caption('Snake v0')

# Класс для точки
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс для объектов, которые можно съесть
class EatebleObjects:
    def __init__(self, x, y, color):
        self.location = Point(x, y)
        self.color = color

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            self.color,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

# Класс для еды
class Food(EatebleObjects):
    pass

# Класс для яда
class Poison(EatebleObjects):
    pass

# Класс для змейки
class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
        ]

    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            HEAD_COLOR,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                SNAKE_COLOR,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        head = self.points[0]
        if head.x >= WIDTH // BLOCK_SIZE or head.x < 0:
            return False
        elif head.y >= HEIGHT // BLOCK_SIZE or head.y < 0:
            return False
        else:
            return True

    def check_collision(self, eateble):
        if self.points[0].x != eateble.x:
            return False
        if self.points[0].y != eateble.y:
            return False
        return True

    def touch_snake(self):
        head = self.points[0]
        for item in self.points[1:]:
            if item.x == head.x and item.y == head.y:
                return False
        return True

# Функция для отрисовки сетки
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (0, y), (WIDTH, y), width=1)

# Функция для отображения счета и уровня
def show_score(score, level):
    my_font = pygame.font.SysFont('times new roman', 25)
    score_surface = my_font.render(f'Score: {score} | Уровень: {level}', True, BLACK)
    SCREEN.blit(score_surface, (0, 0))

# Функция окончания игры
def game_over(score):
    pygame.mixer.music.load(GAME_OVER_SOUND)
    pygame.mixer.music.play()
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Ваш счет: {score}', True, BLACK)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 2)
    SCREEN.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()

# Основная функция игры
def main():
    running = True
    snake = Snake()
    food = Food(5, 5, FOOD_COLOR)
    poison = Poison(6, 8, POISON_COLOR)
    dx, dy = 0, 0
    fps = 5
    score = 0
    level = 1
    direction = 'UP'
    change_to = direction
    pygame.mixer.music.load(BG_SOUND)
    pygame.mixer.music.play(-1)

    while running:
        SCREEN.fill(BOARD_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            dx, dy = 0, -1
        if direction == 'DOWN':
            dx, dy = 0, +1
        if direction == 'LEFT':
            dx, dy = -1, 0
        if direction == 'RIGHT':
            dx, dy = +1, 0

        if snake.move(dx, dy):
            pass
        else:
            game_over(score)

        if snake.touch_snake():
            pass
        else:
            game_over(score)

        if len(snake.points) == 1 and snake.check_collision(poison):
            game_over(score)

        if snake.check_collision(food):
            FOOD_SOUND.play()
            snake.points.append(Point(food.x, food.y))
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            score += 10

        if snake.check_collision(poison):
            POISON_SOUND.play()
            snake.points.pop(-1)
            poison.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            poison.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        food.update()
        poison.update()
        snake.update()
        draw_grid()
        show_score(score, level)
        pygame.display.flip()

        if score >= level * 30:  # Увеличение уровня каждые 30 очков
            level += 1
            fps += 2  # Увеличение скорости с каждым уровнем

        clock.tick(fps)

if __name__ == '__main__':
    main()
