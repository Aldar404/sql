import pygame
import os

pygame.init()

#global
SCREEN_HEIGHIT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHIT))

RUNNING = [pygame.image.load(os.path.join("dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("dino", "DinoRun2.png"))]


class Dinosaur:
    X_POS = 80
    Y_POS = 310

    def __int__(self):
        self.run_img = RUNNING

        self.dino_run = True

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_run:
            self.run()

        if self.step_index >= 10:
            self.step_index = 0


    def run(self):
        self.image = self.run_img(self.step_index // 5)
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)


if __name__ == '__main__':
    main()
