import random
import time
import pygame
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

pygame.init()
WIDTH, HEIGHT = 760, 760
HEAD_COLOR = (19, 213, 213)
BOARD_COLOR = (246, 197, 124)
BLACK = (0, 0, 0)
POISON_COLOR = (255, 0, 0)
FOOD_FOR_FIVE_COLOR = (78, 229, 73)
FOOD_FOR_TEN_COLOR = (83, 253, 202)
FOOD_FOR_FIFTEEN_COLOR = (243, 7, 243)
SNAKE_COLOR = (19, 26, 215)
BG_SOUND = 'sounds/background.mp3'
FOOD_SOUND = pygame.mixer.Sound('sounds/food.mp3')
GAME_OVER_SOUND = 'sounds/game_over.mp3'
POISON_SOUND = pygame.mixer.Sound('sounds/poison.mp3')

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
pygame.display.set_caption('Snake v0')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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


class FoodForFive(EatebleObjects):
    score_add = 5


class FoodForTen(EatebleObjects):
    score_add = 10


class FoodForFifteen(EatebleObjects):
    score_add = 15


class Poison(EatebleObjects):
    score_add = -10


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


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (0, y), (WIDTH, y), width=1)


def show_score(score):
    my_font = pygame.font.SysFont('times new roman', 25)
    game_over_surface = my_font.render(f'Your Score is : {score}', True, BLACK)
    SCREEN.blit(game_over_surface, (0, 0))


def game_over(score):
    pygame.mixer.music.load(GAME_OVER_SOUND)
    pygame.mixer.music.play()
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your Score is : {score}', True, BLACK)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 2)
    SCREEN.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    time.sleep(2)
    adding_user(name, score, level)
    pygame.quit()
    


def adding_user(name):
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password=os.getenv("PASSWORD"),
            database='snake'
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Проверяем, существует ли уже пользователь с таким именем
        cursor.execute("SELECT user_id FROM users WHERE name = %s", (name,))
        existing_user = cursor.fetchone()

        if existing_user:
            user_id = existing_user[0]
            # Получаем текущий уровень пользователя
            cursor.execute("SELECT current_level_id FROM users WHERE user_id = %s", (user_id,))
            current_level_id = cursor.fetchone()[0]
            print("Ваш текущий уровень:", current_level_id)
        else:
            # Если пользователь не существует, добавляем его
            cursor.execute("INSERT INTO users (name) VALUES (%s) RETURNING user_id", (name,))
            user_id = cursor.fetchone()[0]
            current_level_id = 1  # Новый пользователь начинает с уровня 1
            # Устанавливаем начальный уровень для нового пользователя
            cursor.execute("UPDATE users SET current_level_id = %s WHERE user_id = %s", (current_level_id, user_id))

        cursor.close()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при добавлении пользователя:", error)



def load_user_level(name, score):
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password=os.getenv("PASSWORD"),
            database='snake'
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Получаем идентификатор пользователя
        cursor.execute("SELECT user_id FROM users WHERE name = %s", (name,))
        user_id = cursor.fetchone()
        if user_id is None:
            return None  # Если пользователь не найден, возвращаем None

        # Получаем уровень пользователя в зависимости от набранных очков
        cursor.execute("SELECT level FROM users JOIN users_score USING (user_id) WHERE user_id = %s AND score >= %s ORDER BY level DESC", (user_id[0], score))
        level = cursor.fetchone()

        cursor.close()
        conn.close()

        return level[0] if level else 1  # Если уровень не найден, возвращаем 1
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при загрузке уровня игрока:", error)


    

def user_exists(name):
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password=os.getenv("PASSWORD"),
            database='snake'
        )
        cursor = conn.cursor()

        cursor.execute("SELECT user_id FROM users WHERE name = %s", (name,))
        existing_user = cursor.fetchone()

        cursor.close()
        conn.close()

        return existing_user is not None
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при проверке существования пользователя:", error)
        return False


def pause_game():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Нажата клавиша "p" для продолжения игры
                    paused = False
                    return
            

def save_game_state(name, score, level):
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password=os.getenv("PASSWORD"),
            database='snake'
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Получение идентификатора пользователя
        cursor.execute("SELECT user_id FROM users WHERE name = %s", (name,))
        user_id = cursor.fetchone()[0]

        # Обновление данных пользователя
        cursor.execute("UPDATE users SET level = %s WHERE user_id = %s", (level, user_id))
        cursor.execute("INSERT INTO users_score (user_id, score) VALUES (%s, %s)", (user_id, score))
        
        cursor.close()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при сохранении состояния игры:", error)




def main(level):
    running = True
    if level:
        print("Ваш текущий уровень:", level)
    else:
        print("Добро пожаловать, новый игрок!")
    snake = Snake()
    foods = [
        FoodForFive(5, 5, FOOD_FOR_FIVE_COLOR),
        FoodForTen(5, 5, FOOD_FOR_TEN_COLOR),
        FoodForFifteen(5, 5, FOOD_FOR_FIFTEEN_COLOR)
    ]
    food = random.choices(foods, weights=[10, 5, 1])[0]
    poison = Poison(6, 8, POISON_COLOR)
    dx, dy = 0, 0
    fps = 5
    score = 0
    direction = 'UP'
    change_to = direction
    pygame.mixer.music.load(BG_SOUND)
    pygame.mixer.music.play(-1)

    last_food = 0
    food_timer = 15000

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
                if event.key == pygame.K_SPACE:
                    pause_game()
                    continue

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
            if food.location.x == poison.location.x and food.location.y == poison.location.y:
                food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            score = score + food.score_add
            food = random.choices(foods, weights=[10, 5, 1])[0]

        if snake.check_collision(poison):
            POISON_SOUND.play()
            snake.points.pop(-1)
            poison.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            poison.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        now = pygame.time.get_ticks()

        if now - last_food >= food_timer:
            food = random.choices(foods, weights=[10, 5, 1])[0]
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            last_food = now

        food.update()
        poison.update()
        snake.update()
        draw_grid()
        show_score(score)
        pygame.display.flip()

        if score == 50:
            fps = 7
        elif score == 100:
            fps = 9
        elif score == 150:
            fps = 11
        elif score == 200:
            fps = 13
        elif score == 250:
            fps = 15

        clock.tick(fps)

if __name__ == '__main__':
    name = input("Введите ваше имя: ")
    if name:
        score = 0
        if user_exists(name):  # Проверяем, существует ли пользователь в базе данных
            level = load_user_level(name, score)
            print("Ваш текущий уровень:", level)
        else:
            print("Добро пожаловать, новый игрок!")
            level = 1  # Новый пользователь начинает с уровня 1
            adding_user(name, level)  # Добавление нового пользователя в базу данных
        time.sleep(2)
        main(level)
