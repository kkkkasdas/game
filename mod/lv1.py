import pygame
import sys

# 초기화
pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 설정
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# 사각형 객체 설정
rect_width = 50
rect_height = 50
velocity = 25
move_direction = None

# 벽 객체 설정
levels = [
    {
        "walls": [
            {"rect" : pygame.Rect(350, 250, rect_width, rect_height), "name" : "1"},
            {"rect" : pygame.Rect(325, 100, rect_width, rect_height), "name" : "2"},
            {"rect" : pygame.Rect(150, 125, rect_width, rect_height), "name" : "3"},
            {"rect" : pygame.Rect(175, 350, rect_width, rect_height), "name" : "4"},
            {"rect" : pygame.Rect(475, 325, rect_width, rect_height), "name" : "5"},
        ],
        "triangles": [  # 직각삼각형 추가
            {"points": [(100, 100), (150, 100), (100, 150)], "direction_change": "right"},
        ],
        "rotated_squares": [  # 회전한 정사각형 추가
            {"points": [(200, 200), (250, 250), (200, 300), (150, 250)], "direction_change": "down"},
        ],
        "goal": pygame.Rect(450,150,rect_width,rect_height),
        "player_start": (250,250),
    },
]

# 직각삼각형 빗면 충돌 검사 및 진행 방향 변경 로직
def check_slope_collision(player_rect, triangles, direction):
    for triangle in triangles:
        # 각 삼각형에 대한 충돌 검사 로직이 필요
        # 여기서는 단순화된 예시로, 실제 구현은 더 복잡한 충돌 검사가 필요
        slope = triangle["points"][0], triangle["points"][2]  # 빗면 좌표 추출
        dx = slope[1][0] - slope[0][0]
        dy = slope[1][1] - slope[0][1]
        slope_direction = 'up' if dy > 0 else 'down'
        
        # 충돌 검사 로직 (여기서는 간단화하여 진행 방향만 확인)
        if direction == 'right':  # 실제로는 player_rect와 slope가 충돌하는지 검사해야 함
            if slope_direction == 'up':
                return 'up'
            else:
                return 'down'
    return direction

def check_collision(rect, walls):
    for wall in walls:
        if rect.colliderect(wall["rect"]):
            return True
    return False

# 게임 루프
game_running = True
current_level = 0

while game_running:
    level=levels[current_level]
    walls = level["walls"]
    goal = level["goal"]
    triangles = level["triangles"]
    player_x, player_y = level["player_start"]
    def_x, def_y = player_x, player_y
    player_rect = pygame.Rect(player_x, player_y, rect_width, rect_height)
    round_running = True

    while round_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                round_running = False
                game_running = False

            # 키 입력 처리
            if event.type == pygame.KEYDOWN and move_direction is None:
                if event.key == pygame.K_LEFT:
                    move_direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    move_direction = 'right'
                elif event.key == pygame.K_UP:
                    move_direction = 'up'
                elif event.key == pygame.K_DOWN:
                    move_direction = 'down'

        old_x, old_y = player_x, player_y

        # 이동 처리
        if move_direction == 'left':
            player_x -= velocity
        elif move_direction == 'right':
            player_x += velocity
        elif move_direction == 'up':
            player_y -= velocity
        elif move_direction == 'down':
            player_y += velocity

        player_rect.update(player_x, player_y, rect_width, rect_height)

        # 경계 처리
        if player_x < 0 or player_x > screen_width - rect_width or player_y < 0 or player_y > screen_height - rect_height:
            player_x, player_y = old_x, old_y  # 원래 위치로 복구

        # 빗면 충돌 검사 및 진행 방향 변경
        if move_direction == 'right':  # 오른쪽으로 이동 중일 때만 빗면 충돌 검사
            move_direction = check_slope_collision(player_rect, triangles, move_direction)

        # 충돌 처리
        if check_collision(player_rect, walls):
            player_x, player_y = old_x, old_y  # 충돌 시 원래 위치로 복구
            move_direction = None  # 이동 방향 초기화

        # 목표 지점 도달 확인
        if player_rect.colliderect(goal):
            print("목표 지점에 도달했습니다!")
            round_running = False
            break

        # 화면 그리기
        screen.fill(white)
        for wall in walls:
            pygame.draw.rect(screen, red, wall["rect"])
        for triangle in triangles:
            pygame.draw.polygon(screen, red, triangle["points"])
        pygame.draw.rect(screen, green, goal)
        pygame.draw.rect(screen, blue, player_rect)

        pygame.display.update()
        pygame.time.Clock().tick(60)

pygame.quit()
