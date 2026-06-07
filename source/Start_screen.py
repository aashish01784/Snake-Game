import pygame
import sys
import random
import Display

from Display import Screen as screen
from Display import WIDTH as width
from Display import HEIGHT as height

pygame.init()        
pygame.font.init()


# Start screen background image
start_bg = pygame.image.load("start_bg.jpg")
start_bg = pygame.transform.scale(start_bg, (width, height))

font = pygame.font.SysFont("Segoe UI Emoji", 20)


def show_start_screen():
    screen.blit(start_bg, (0, 0))
    font_big = pygame.font.SysFont("Arial", 45)
    title = font_big.render("SNAKE GAME", True, (0, 0, 0))
    instr1 = font.render("Press SPACE to Start", True, (255, 255, 255))
    instr2 = font.render("Arrow keys to move | P to pause | R to resume", True, (255, 255, 255))
    instr3 = font.render("Eat food 🍎. Avoid crashing to walls and to yourself !", True, (255, 255, 0))
    screen.blit(title, title.get_rect(center=(width // 2, height // 3)))
    screen.blit(instr1, instr1.get_rect(center=(width // 2 - 10, height // 2)))
    screen.blit(instr2, instr2.get_rect(center=(width // 2 - 10, height // 2 + 40)))
    screen.blit(instr3, instr3.get_rect(center=(width // 2 - 10, height // 2 + 80)))
    pygame.display.update()