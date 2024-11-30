import pygame
import random

SNOWS= 5555
WIND_SPEED = 7
FALL_SPEED = 5
PARALLACS_K = 0.2
START_SPEED = 2
WIDTH = 1024
HEIGHT = 800
WHITE = (240, 255, 255)
BLACK = (10, 2, 10)
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("C новым годом!!!:-)))")
clock = pygame.time.Clock()


class SNOW:

    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.expovariate(lambd = 0.66)
        self.start_speed = random.expovariate(lambd = 11)
        self.color = color


    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x + WIND_SPEED * self.size * PARALLACS_K + self.start_speed
        self.y += self.move_y + FALL_SPEED * self.size * PARALLACS_K + self.start_speed
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = 0



def draw_environment(snow_d):
    game_display.fill(BLACK)
    for _ in snow_d:
        snow = snow_d[_]
        (pygame.draw.circle
         (game_display, snow.color ,
          [snow.x, snow.y], snow.size))
        snow.move()
    pygame.display.update()


def main():
    snow_d = dict(enumerate([SNOW(WHITE) for _ in range(SNOWS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        draw_environment(snow_d)
        clock.tick(60)


if __name__ == '__main__':
    main()