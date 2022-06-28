import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 8, HEIGHT // 2)
        self.is_now_jump = False
        self.y_speed = 0
        self.JUMP_POWER = 16

    def jump(self):
        if not self.is_now_jump:
            self.y_speed = -self.JUMP_POWER
            self.is_now_jump = True

    def update(self):
        if self.is_now_jump:
            if self.y_speed == self.JUMP_POWER:
                self.is_now_jump = False
            self.rect.y += self.y_speed
            self.y_speed += 1


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH + randint(50, 1000), HEIGHT // 2)
        self.x_speed = randint(7, 15)

    def update(self):
        if self.rect.left + 50 < 0:
            self.kill()
        global running
        self.rect.left -= self.x_speed
        if pygame.sprite.collide_rect(self, player):
            running = False


WIDTH = 800
HEIGHT = 600
FPS = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.jump()
    if len(all_sprites) < 3:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
    all_sprites.update()
    screen.fill((220, 220, 220))
    screen.fill((20, 20, 20), rect=(0, 0, WIDTH, HEIGHT // 2 + 20))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

