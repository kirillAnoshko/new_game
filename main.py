import pygame
from random import randint

GREEN = (0, 255, 0)
ROWS = 50
COLS = 50
CELL_SIZE = 5


class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.content = None
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.image.fill((r, g, b))


cells = [
    [Cell(y=row, x=col) for col in range(COLS)]
    for row in range(ROWS)
]


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Моя игра")
        self.clock = pygame.time.Clock()
        self.is_running = True

    def render(self):
        self.screen.fill((255, 255, 255))
        for row in cells:
            for cell in row:
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                cell.image.fill((r, g, b))
                self.screen.blit(cell.image, (cell.x * CELL_SIZE, cell.y * CELL_SIZE))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pygame.display.update()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.render()
            self.update()

            self.screen.fill((0, 0, 0))

            # Установка частоты кадров
            self.clock.tick(60)
        pygame.quit()      

# Создание экземпляра игры и запуск игрового цикла
game = Game()
game.run()
