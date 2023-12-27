import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 900))
        pygame.display.set_caption("Моя игра")
        self.clock = pygame.time.Clock()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()

            pygame.draw.rect(self.screen, (255, 0, 0), (300, 200, 50, 50))
            pygame.display.flip()

            # Очистка экрана
            self.screen.fill((0, 0, 0))

            # Установка частоты кадров
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):  # Обновление экрана
        pygame.display.flip()


# Создание экземпляра игры и запуск игрового цикла
game = Game()
game.run()