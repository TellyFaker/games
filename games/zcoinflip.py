import pygame
import random

# Initialisierung
pygame.init()

# Farben und Einstellungen
WIDTH, HEIGHT = 500, 400
WHITE = (240, 240, 240)
DARK_GREY = (40, 40, 40)
GOLD = (255, 215, 0)
GREEN = (46, 204, 113)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Flip HUD")
font = pygame.font.SysFont("Arial", 24, bold=True)

# Spielvariablen (Das HUD-System)
stats = {"Win": 0, "Loss": 0, "Total": 0}
last_result = "Ready?"
is_animating = False

def draw_hud():
    # Hintergrund für das HUD (Obere Leiste)
    pygame.draw.rect(screen, DARK_GREY, (0, 0, WIDTH, 60))
    
    # Statistiken rendern
    win_text = font.render(f"Wins: {stats['Win']}", True, GREEN)
    loss_text = font.render(f"Losses: {stats['Loss']}", True, (231, 76, 60))
    total_text = font.render(f"Total: {stats['Total']}", True, WHITE)
    
    screen.blit(win_text, (20, 15))
    screen.blit(loss_text, (180, 15))
    screen.blit(total_text, (350, 15))

def flip_coin():
    stats["Total"] += 1
    result = random.choice(["HEADS", "TAILS"])
    # Hier simulieren wir eine 50/50 Chance für das HUD
    if result == "HEADS":
        stats["Win"] += 1
    else:
        stats["Loss"] += 1
    return result

# Main Loop
running = True
button_rect = pygame.Rect(175, 250, 150, 50)

while running:
    screen.fill((60, 60, 60)) # Hintergrundfarbe
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                last_result = flip_coin()

    # HUD zeichnen
    draw_hud()

    # Die Münze (HUD-Zentrum)
    pygame.draw.circle(screen, GOLD, (WIDTH // 2, 160), 60)
    res_text = font.render(last_result, True, DARK_GREY)
    screen.blit(res_text, (WIDTH // 2 - res_text.get_width() // 2, 145))

    # Button zeichnen
    pygame.draw.rect(screen, GREEN, button_rect, border_radius=10)
    btn_text = font.render("FLIP!", True, WHITE)
    screen.blit(btn_text, (button_rect.centerx - btn_text.get_width() // 2, button_rect.centery - 12))

    pygame.display.flip()

pygame.quit()
