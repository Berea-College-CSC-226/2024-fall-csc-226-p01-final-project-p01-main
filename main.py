import pygame
from game_manager import GameManager
from sound_manager import SoundManager

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fashion Demon")
    clock = pygame.time.Clock()

    game_manager = GameManager()
    sound_manager = SoundManager()
    sound_manager.play_current_track()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_manager.update()

        screen.fill((135, 206, 250))  # Light blue background for sky effect
        game_manager.draw(screen)

        sound_manager.check_music()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()