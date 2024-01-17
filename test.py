import pygame
import sys
import random


class Anthill:
    def __init__(self, cell_size, num_cells_x, num_cells_y, existing_positions):
        self.cell_size = cell_size
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.positions = self.generate_random_positions(existing_positions)

    def generate_random_positions(self, existing_positions):
        positions = set()
        num_anthills = random.randint(1, 4)
        while len(positions) < num_anthills:
            x = random.randint(0, self.num_cells_x - 1)
            y = random.randint(0, self.num_cells_y - 1)
            position = (x, y)
            if position not in existing_positions and position not in positions:
                positions.add(position)
        return positions


class Field:
    def __init__(self, screen, cell_size, num_cells_x, num_cells_y):
        self.screen = screen
        self.cell_size = cell_size
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.player = Player(self.cell_size, self.num_cells_x, self.num_cells_y, num_cells_x, num_cells_y)
        self.anthill = Anthill(self.cell_size, self.num_cells_x, self.num_cells_y, {(self.player.x, self.player.y)})
        self.font = pygame.font.Font(None, self.cell_size)

    def render(self, offset_x, offset_y):
        for x in range(self.num_cells_x):
            for y in range(self.num_cells_y):
                cell_surface = pygame.Surface((self.cell_size, self.cell_size))
                cell_surface.fill((255, 255, 255))
                pygame.draw.rect(cell_surface, (0, 0, 0), cell_surface.get_rect(), 2)

                cell_rect = cell_surface.get_rect(
                    topleft=(offset_x + x * self.cell_size, offset_y + y * self.cell_size)
                )

                self.screen.blit(cell_surface, cell_rect.topleft)

        # Отрисовка игрока
        player_text = self.font.render("P", True, (0, 0, 255))
        player_rect = player_text.get_rect(
            center=(offset_x + (self.player.x + 0.5) * self.cell_size,
                    offset_y + (self.player.y + 0.5) * self.cell_size)
        )
        self.screen.blit(player_text, player_rect.topleft)

        # Отрисовка муравейников
        for position in self.anthill.positions:
            anthill_text = self.font.render("A", True, (255, 0, 0))
            anthill_rect = anthill_text.get_rect(
                center=(offset_x + (position[0] + 0.5) * self.cell_size,
                        offset_y + (position[1] + 0.5) * self.cell_size)
            )
            self.screen.blit(anthill_text, anthill_rect.topleft)


class Player:
    def __init__(self, cell_size, num_cells_x, num_cells_y, field_num_cells_x, field_num_cells_y):
        self.cell_size = cell_size
        self.x = random.randint(0, num_cells_x - 1)
        self.y = random.randint(0, num_cells_y - 1)
        self.num_cells_x = field_num_cells_x
        self.num_cells_y = field_num_cells_y

    def move(self, dx, dy, anthill_positions):
        new_x = (self.x + dx) % self.num_cells_x
        new_y = (self.y + dy) % self.num_cells_y

        if (new_x, new_y) not in anthill_positions:
            self.x = new_x
            self.y = new_y


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.cell_size = 50
        self.num_cells_x = 10
        self.num_cells_y = 10
        self.offset_x = 0
        self.offset_y = 0

        self.field = Field(self.screen, self.cell_size, self.num_cells_x, self.num_cells_y)

    def run(self):
        while self.is_running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        anthill_positions = self.field.anthill.positions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
                elif event.key == pygame.K_UP:
                    self.field.player.move(0, -1, anthill_positions)
                elif event.key == pygame.K_DOWN:
                    self.field.player.move(0, 1, anthill_positions)
                elif event.key == pygame.K_LEFT:
                    self.field.player.move(-1, 0, anthill_positions)
                elif event.key == pygame.K_RIGHT:
                    self.field.player.move(1, 0, anthill_positions)

    def update(self):
        pass

    def render(self):
        self.screen.fill((255, 255, 255))
        self.offset_x = (self.screen.get_width() - self.num_cells_x * self.cell_size) // 2
        self.offset_y = (self.screen.get_height() - self.num_cells_y * self.cell_size) // 2

        self.field.render(self.offset_x, self.offset_y)

        pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Window()
    game.run()
    game.quit_game()