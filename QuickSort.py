import pygame
import random

# Инициализируем библиотеку Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Определение размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Функция для отображения массива
def display_array(arr):
    screen.fill(WHITE)
    for i in range(len(arr)):
        color = BLACK
        if arr[i] == pivot:
            color = RED
        elif i in sub_array:
            color = BLUE
        elif i in sorted_indices:
            color = GREEN
        pygame.draw.rect(screen, color, [(i*10)+10, WINDOW_HEIGHT-arr[i], 5, arr[i]])
    pygame.display.update()
    pygame.time.wait(100) # задержка в 100 миллисекунд

# Функция быстрой сортировки
def quick_sort(arr, start, end):
    global sub_array, sorted_indices, pivot
    if start >= end:
        return
    pivot = arr[end]
    pivot_index = start
    sub_array = set()
    sorted_indices = set()
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
            sub_array.add(i)
            display_array(arr)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    sorted_indices.add(pivot_index)
    display_array(arr)
    quick_sort(arr, start, pivot_index-1)
    quick_sort(arr, pivot_index+1, end)

# Создание случайного массива
arr = [random.randint(50, WINDOW_HEIGHT-10) for i in range(WINDOW_WIDTH//10-2)]

# Запуск быстрой сортировки
quick_sort(arr, 0, len(arr)-1)

# Ожидание закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
