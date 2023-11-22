import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Размеры кубика
CUBE_SIZE = 50

# Начальная позиция кубика
cube_x = -5
cube_y = -5

# Скорость движения кубика
speed_x = 10
speed_y = 10

# Текущий оттенок цвета
hue = 0

# Список для хранения предыдущих позиций и цветов
trail = []

# Длина хвоста
MAX_TRAIL_LENGTH = 999999999

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Отскакивающий кубик с изменением цвета и хвостом")

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение кубика
    cube_x += speed_x
    cube_y += speed_y

    # Отскок от границ экрана
    if cube_x <= 0 or cube_x >= SCREEN_WIDTH - CUBE_SIZE:
        speed_x = -speed_x
    if cube_y <= 0 or cube_y >= SCREEN_HEIGHT - CUBE_SIZE:
        speed_y = -speed_y

    # Изменение оттенка цвета
    hue = (hue + 1) % 360
    color = pygame.Color(0, 0, 0, 0)
    color.hsla = (hue, 100, 50, 100)

    # Добавление текущей позиции и цвета в хвост
    trail.append((cube_x, cube_y, color))
    if len(trail) > MAX_TRAIL_LENGTH:
        trail.pop(0)

    # Заполнение экрана белым цветом
    screen.fill((255, 255, 255))

    # Рисование хвоста с черной рамкой
    for trail_position in trail:
        pygame.draw.rect(screen, (0, 0, 0), (trail_position[0], trail_position[1], CUBE_SIZE, CUBE_SIZE), 5)
        pygame.draw.rect(screen, trail_position[2], (trail_position[0] + 1, trail_position[1] + 1, CUBE_SIZE - 2, CUBE_SIZE - 2))

    # Рисование кубика
    pygame.draw.rect(screen, color, (cube_x, cube_y, CUBE_SIZE, CUBE_SIZE))

    # Обновление экрана
    pygame.display.flip()

    # Задержка для контроля частоты обновления экрана
    pygame.time.Clock().tick(30)
