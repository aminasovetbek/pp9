"""
Music Player - Practice 09 Task 3.2
Controls: P=Play  S=Stop  N=Next  B=Back  UP/DOWN=Volume  Q=Quit
"""

import pygame
import sys
from player import MusicPlayer

WIDTH, HEIGHT = 500, 400
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
GRAY   = (60, 60, 60)
PURPLE = (150, 80, 255)
GREEN  = (80, 220, 120)
RED    = (255, 80, 80)


def draw(screen, player, fonts):
    screen.fill((15, 12, 30))

    title = fonts['big'].render("♪ MUSIC PLAYER ♪", True, PURPLE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    status = "▶ PLAYING" if player.is_playing else "■ STOPPED"
    color  = GREEN if player.is_playing else RED
    s = fonts['mid'].render(status, True, color)
    screen.blit(s, (WIDTH // 2 - s.get_width() // 2, 70))

    # Track info
    num = fonts['mid'].render(
        f"Track {player.current_index + 1} / {len(player.playlist)}", True, GRAY)
    screen.blit(num, (WIDTH // 2 - num.get_width() // 2, 110))

    name = fonts['mid'].render(player.get_name(), True, WHITE)
    screen.blit(name, (WIDTH // 2 - name.get_width() // 2, 140))

    pygame.draw.rect(screen, GRAY, (40, 185, WIDTH - 80, 10), border_radius=5)
    pos = min(player.get_position() / 180, 1.0)
    if pos > 0:
        pygame.draw.rect(screen, PURPLE,
                         (40, 185, int((WIDTH - 80) * pos), 10), border_radius=5)

    vol_label = fonts['small'].render(f"Volume: {int(player.get_volume() * 100)}%", True, GRAY)
    screen.blit(vol_label, (40, 210))
    pygame.draw.rect(screen, GRAY, (40, 230, WIDTH - 80, 8), border_radius=4)
    pygame.draw.rect(screen, GREEN,
                     (40, 230, int((WIDTH - 80) * player.get_volume()), 8), border_radius=4)

    controls = [
        ("P", "Play", GREEN),
        ("S", "Stop", RED),
        ("N", "Next", PURPLE),
        ("B", "Back", (255, 210, 60)),
        ("Q", "Quit", GRAY),
    ]
    y = 270
    x_start = 40
    for i, (key, label, color) in enumerate(controls):
        bx = x_start + i * 88
        pygame.draw.circle(screen, color, (bx, y), 20)
        k = fonts['mid'].render(key, True, BLACK)
        screen.blit(k, (bx - k.get_width() // 2, y - k.get_height() // 2))
        lbl = fonts['small'].render(label, True, GRAY)
        screen.blit(lbl, (bx - lbl.get_width() // 2, y + 26))

    hint = fonts['small'].render("↑ / ↓  =  Volume", True, GRAY)
    screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 340))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()

    fonts = {
        'big':   pygame.font.SysFont("Arial", 26, bold=True),
        'mid':   pygame.font.SysFont("Arial", 18),
        'small': pygame.font.SysFont("Arial", 14),
    }

    player = MusicPlayer(music_folder="music")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_p: player.play()
                elif event.key == pygame.K_s: player.stop()
                elif event.key == pygame.K_n: player.next_track()
                elif event.key == pygame.K_b: player.prev_track()
                elif event.key == pygame.K_q: running = False
                elif event.key == pygame.K_UP:   player.set_volume(player.get_volume() + 0.1)
                elif event.key == pygame.K_DOWN: player.set_volume(player.get_volume() - 0.1)

        if player.finished():
            player.next_track()

        draw(screen, player, fonts)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
