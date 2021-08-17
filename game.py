import game
from player import Player
import pygame

class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = { }
        self.titre=pygame.display.set_caption("comet fall game")
        self.background = pygame.image.load('assets/bg.jpg')
        self.screen = pygame.display.set_mode((1080, 720))

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:

            self.screen.blit(self.background, (0, -200))
            # print(game.pressed)
            self.screen.blit(self.player.image, self.player.rect)

            game.player.all_projectiles.draw(screen)

            if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < self.screen.get_width():
                self.player.move_right()
            elif self.pressed.get(pygame.K_q) and self.player.rect.x > 25:
                self.player.move_left()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print('fermeture')

                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True

                    if event.key == pygame.K_SPACE:
                        game.player.lunch_projectile()

                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False
            clock.tick(60)
