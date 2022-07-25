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
        self.x_speed = 0
        self.JUMP_POWER = 16
        self.player_speed = 10

    def jump(self):
        if not self.is_now_jump:
            self.y_speed = -self.JUMP_POWER
            self.is_now_jump = True

    def step_right(self):
        self.x_speed += self.player_speed
        self.rect.x += self.x_speed
        self.x_speed += 1

    def step_left(self):
        self.x_speed -= self.player_speed
        self.rect.x -= self.x_speed
        self.x_speed += 1

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
        self.x_speed = 15

    def update(self):
        if self.rect.left + 50 < 0:
            self.kill()
        global running
        self.rect.left -= self.x_speed
        if pygame.sprite.collide_rect(self, player):
            running = False


WIDTH = 800
HEIGHT = 600
FPS = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")
pygame.display.set_icon(pygame.image.load("Alien.png"))
clock = pygame.time.Clock()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
# основной игровой цикл
while running:
    clock.tick(FPS)
    # обработка нажатия клавиш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.jump()
        # поправить класс player неправильное отображение движений
        # при зажатой клавише должен двигаться влево или вправо
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.step_left()
        elif keys[pygame.K_RIGHT]:
            player.step_right()
    # отрисовка обьектов препятствий
    if len(all_sprites) < 3:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
    # отрисовка экрана и спрайтов
    all_sprites.update()
    screen.fill((220, 220, 220))
    screen.fill((20, 20, 20), rect=(0, 0, WIDTH, HEIGHT // 2 + 20))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

