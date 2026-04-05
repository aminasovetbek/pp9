import pygame
import sys
import datetime
from clock import MickeysClock

# ── Window settings ──────────────────────────────────────────────────────────
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
FPS = 60
TITLE = "Mickey's Clock"

# ── Colors ────────────────────────────────────────────────────────────────────
BG_COLOR = (15, 10, 30)          # Dark background
BG_STRIPE_COLOR = (20, 15, 40)   # Subtle stripe for texture


def draw_background(surface):
    """Draw a stylized dark background with subtle pattern."""
    surface.fill(BG_COLOR)
    # Subtle diagonal stripes for texture
    for i in range(0, SCREEN_WIDTH + SCREEN_HEIGHT, 30):
        pygame.draw.line(surface, BG_STRIPE_COLOR,
                         (i, 0), (0, i), 1)


def draw_digital_time(surface, font, minutes, seconds):
    """Display digital time (MM:SS) at the bottom of the screen."""
    time_str = f"{minutes:02d}:{seconds:02d}"
    
    # Shadow
    shadow = font.render(time_str, True, (0, 0, 0))
    surface.blit(shadow, (SCREEN_WIDTH // 2 - shadow.get_width() // 2 + 3,
                          SCREEN_HEIGHT - 62))
    
    # Main text
    text = font.render(time_str, True, (255, 230, 80))
    surface.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
                        SCREEN_HEIGHT - 65))


def draw_title(surface, font):
    """Draw the title at the top."""
    title = font.render("⋆ MICKEY'S CLOCK ⋆", True, (255, 200, 50))
    shadow = font.render("⋆ MICKEY'S CLOCK ⋆", True, (100, 60, 0))
    surface.blit(shadow, (SCREEN_WIDTH // 2 - title.get_width() // 2 + 2, 17))
    surface.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 15))


def main():
    pygame.init()

    # Create window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)

    clock_tick = pygame.time.Clock()

    # Fonts
    font_title = pygame.font.SysFont("Arial", 26, bold=True)
    font_digital = pygame.font.SysFont("Courier New", 52, bold=True)

    # Create Mickey's clock object
    mickey_clock = MickeysClock(screen_width=SCREEN_WIDTH,
                                screen_height=SCREEN_HEIGHT - 50)

    print("Mickey's Clock started!")
    print("Press ESC or close window to quit.")

    # ── Main game loop ────────────────────────────────────────────────────────
    running = True
    while running:

        # ── Event handling ────────────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # ── Get current time ──────────────────────────────────────────────────
        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        # ── Drawing ───────────────────────────────────────────────────────────
        # Background
        draw_background(screen)

        # Title
        draw_title(screen, font_title)

        # Clock (centered, slightly below title)
        clock_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - 50), pygame.SRCALPHA)
        clock_surface.fill((0, 0, 0, 0))
        mickey_clock.draw(clock_surface, minutes, seconds)
        screen.blit(clock_surface, (0, 10))

        # Digital time display at bottom
        draw_digital_time(screen, font_digital, minutes, seconds)

        # ── Update display ────────────────────────────────────────────────────
        pygame.display.flip()
        clock_tick.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
