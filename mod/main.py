import pygame
import sys
from setting import *
from object import *
from function import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("미니몬의 미로 탈출 (Minimon's Maze Escape)")
    
    game_running = True
    current_level = 0
    move_direction = None

    while game_running:
        level = levels[current_level]
        walls = level["walls"]
        goal = level["goal"]
        triangle_points = level.get("triangle_points", [])  # 안전하게 접근하기 위해 get 사용
        square_points = level.get("square_points", [])
        player_x = level["player_start"][0]
        player_y = level["player_start"][1]
        def_x, def_y = player_x, player_y
        player_rect = pygame.Rect(player_x, player_y, rect_width, rect_height)

        round_running = True
        while round_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    round_running = False
                    game_running = False  # 전체 게임 종료
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        move_direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        move_direction = 'right'
                    elif event.key == pygame.K_UP:
                        move_direction = 'up'
                    elif event.key == pygame.K_DOWN:
                        move_direction = 'down'
                if event.type == pygame.KEYUP:
                    move_direction = None  # 키를 떼면 멈춤

            if move_direction:
                old_x, old_y = player_x, player_y

                if move_direction == 'left':
                    player_x -= velocity
                elif move_direction == 'right':
                    player_x += velocity
                elif move_direction == 'up':
                    player_y -= velocity
                elif move_direction == 'down':
                    player_y += velocity

                # 경계 처리
                if player_x < 0 or player_x > screen_width - rect_width or player_y < 0 or player_y > screen_height - rect_height:
                    player_x, player_y = old_x, old_y  # 이전 위치로 되돌림

            # 화면 그리기 시작
            screen.fill(white)
            
            # 직각삼각형 그리기
            if triangle_points:
                pygame.draw.polygon(screen, red, triangle_points)
            # 정사각형 그리기
            if square_points:
                pygame.draw.polygon(screen, red, square_points)

            # 플레이어, 목표, 벽 그리기
            pygame.draw.rect(screen, blue, player_rect)
            pygame.draw.rect(screen, green, goal)
            
            font = pygame.font.Font(None, 24)  # 폰트 크기 수정

            for wall in walls:
                pygame.draw.rect(screen, red, wall["rect"])
                wall_name_surface = font.render(wall["name"], True, white)
                screen.blit(wall_name_surface, (wall["rect"].x + 5, wall["rect"].y + 5))  # 텍스트 위치 수정

            # 화면 업데이트
            pygame.display.update()
            pygame.time.Clock().tick(60)


            # 충돌 처리
            if check_collision(player_rect, walls) or player_rect.colliderect(goal):
                player_x, player_y = old_x, old_y
                move_direction = None

            # 목표 지점 도달 확인
            if player_rect.colliderect(goal):
                print("목표 지점에 도달했습니다!")
                success_font = pygame.font.Font(None, 40)
                success_message = success_font.render("Great!", True, (0, 0, 0))
                success_rect = success_message.get_rect(center=(screen_width // 2, screen_height // 2))
                screen.blit(success_message, success_rect)
                pygame.display.update()
                pygame.time.delay(2000)  # 알림창이 2초 동안 나타납니다.
                round_running = False
                break

            
        current_level += 1
        if current_level >= len(levels):
            game_running = False
            print("Game Exit.")
    pygame.quit()

if __name__ == "__main__":
    main()
