import pygame
import sys
import os
import random

TILE_WIDTH = 64
TILE_HEIGHT = 32
GRID_SIZE = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Offsets to center the map
OFFSET_X = SCREEN_WIDTH // 2
OFFSET_Y = 50

def grid_to_iso(x, y):
    iso_x = (x - y) * (TILE_WIDTH // 2) + OFFSET_X
    iso_y = (x + y) * (TILE_HEIGHT // 2) + OFFSET_Y
    return iso_x, iso_y

def iso_to_grid(iso_x, iso_y):
    iso_x -= OFFSET_X
    iso_y -= OFFSET_Y
    grid_x = (iso_y / (TILE_HEIGHT / 2) + iso_x / (TILE_WIDTH / 2)) / 2
    grid_y = (iso_y / (TILE_HEIGHT / 2) - iso_x / (TILE_WIDTH / 2)) / 2
    return int(round(grid_x)), int(round(grid_y))

def create_tile(color):
    surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)
    points = [
        (TILE_WIDTH // 2, 0),
        (TILE_WIDTH, TILE_HEIGHT // 2),
        (TILE_WIDTH // 2, TILE_HEIGHT),
        (0, TILE_HEIGHT // 2),
    ]
    pygame.draw.polygon(surface, color, points)
    return surface


class Unit:
    """A simple walking unit."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self) -> None:
        """Move randomly one tile in the four cardinal directions."""
        if random.random() < 0.2:
            dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                self.x = nx
                self.y = ny


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Isometric City")

    clock = pygame.time.Clock()

    sprite_path = os.path.join(os.path.dirname(__file__), "sprites")
    grass_tile = pygame.image.load(os.path.join(sprite_path, "grass.png")).convert_alpha()
    house_tile = pygame.image.load(os.path.join(sprite_path, "building.png")).convert_alpha()

    grid = [["grass" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    units = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                gx, gy = iso_to_grid(mx, my)
                if 0 <= gx < GRID_SIZE and 0 <= gy < GRID_SIZE:
                    if grid[gx][gy] != "house":
                        grid[gx][gy] = "house"
                        units.append(Unit(gx, gy))

        screen.fill((0, 0, 0))

        # Draw grid
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                sx, sy = grid_to_iso(x, y)
                if grid[x][y] == "grass":
                    screen.blit(grass_tile, (sx, sy))
                elif grid[x][y] == "house":
                    screen.blit(house_tile, (sx, sy))

        # Move and draw units
        for unit in units:
            unit.move()
            ux, uy = grid_to_iso(unit.x, unit.y)
            pygame.draw.circle(
                screen,
                (0, 0, 0),
                (ux + TILE_WIDTH // 2, uy + TILE_HEIGHT // 2),
                5,
            )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
