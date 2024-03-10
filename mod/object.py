import pygame
from setting import *

# 폴리곤 포인트 정의
triangle_points = [(300, 400), (400, 300), (500, 400)]  # 직각삼각형의 세 꼭짓점
square_points = [(550, 250), (650, 250), (650, 350), (550, 350)]  # 정사각형의 네 꼭짓점

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
        "goal": pygame.Rect(450,150,rect_width,rect_height),
        "player_start": (250,250),
        "triangle_points": triangle_points,
        "square_points": square_points
    },
]
