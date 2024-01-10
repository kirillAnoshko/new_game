import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Моя игра")
        self.clock = pygame.time.Clock()
        self.is_running = True

    def render(self):
        self.rect = pygame.Rect(300, 200, 50, 50)
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rect.y -= 15
                if event.key == pygame.K_DOWN:
                    self.rect.y += 15
                if event.key == pygame.K_LEFT:
                    self.rect.x -= 15
                if event.key == pygame.K_RIGHT:
                    self.rect.x += 15    

    def update(self):
       pygame.display.update()
    
    def run(self):
        while self.is_running:
            self.handle_events()
            self.render()
            self.move()
            self.update()
            
            self.screen.fill((0, 0, 0))

            # Установка частоты кадров
            self.clock.tick(60)
        pygame.quit()    
    
# Создание экземпляра игры и запуск игрового цикла
game = Game()
game.run()