#Snake Tutorial Python
import os
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("my game")

white = (255, 255, 255)
green = (0, 255, 0)
purple = (150,0,100)
FPS = 60

green_grapes = pygame.image.load(os.path.join('assets','green_grapes.jpeg'))

green_grapes = pygame.transform.scale(green_grapes, (110, 80))
banana = pygame.image.load(os.path.join('assets','banana.jpeg'))
banana = pygame.transform.scale(banana, (110, 80))
monkey_eating_banana = pygame.image.load(os.path.join('assets','monkey_eating_banana.jpeg'))
monkey_eating_banana = pygame.transform.scale(monkey_eating_banana, (110, 80))
monkey_eating = pygame.image.load(os.path.join('assets','monkey_eating.jpeg'))
monkey_eating = pygame.transform.scale(monkey_eating, (110, 150))


def draw_window(colour):
  win.fill(colour)
  win.blit(green_grapes,(200,100))

  win.blit(banana,(450,100))
  win.blit(monkey_eating,(360,300))
  win.blit(monkey_eating_banana,(160,300))

  pygame.display.update()


def main():
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
  
    draw_window(white)
  
  pygame.quit()


if __name__ == "__main__":
  main()