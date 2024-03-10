import pygame
from setting import screen_width, screen_height, rect_width, rect_height, white, blue, red, green

def check_collision(rect, walls):
    for wall in walls:
        if rect.colliderect(wall["rect"]):
            return True
    return False

def draw_game(screen, walls, player_rect, goal):
    # 화면 그리기
    screen.fill(white)
    pygame.draw.rect(screen, blue, player_rect)
    pygame.draw.rect(screen, green, goal)
    font = pygame.font.Font(None, 20)

    for wall in walls:
        pygame.draw.rect(screen, red, wall["rect"])
        wall_name_surface = font.render(wall["name"], True, white)
        screen.blit(wall_name_surface, (wall["rect"].x + rect_width // 2 - wall_name_surface.get_width() // 2, wall["rect"].y + rect_height // 2 - wall_name_surface.get_height() // 2))
