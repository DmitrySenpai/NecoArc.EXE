import pygame
import time
import os
import random
import sys

def select_audio():
    sound_files = os.listdir(resource_path("sound"))
    sound_files = [os.path.join(resource_path("sound"), file) for file in sound_files]
    return random.choice(sound_files)

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pygame.init()
screen_size = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)

image = pygame.image.load(resource_path("images.jpg"))
pygame.display.set_icon(image)
image = pygame.transform.scale(image, screen_size)
image_rect = image.get_rect()
if image_rect.width < screen_size[0]:
    black_strip = pygame.Surface((screen_size[0]-image_rect.width, image_rect.height))
    black_strip.fill((0, 0, 0))
    screen.blit(black_strip, (image_rect.right, image_rect.top))
    screen.blit(black_strip, (0, image_rect.top))
if image_rect.height < screen_size[1]:
    black_strip = pygame.Surface((screen_size[0], screen_size[1]-image_rect.height))
    black_strip.fill((0, 0, 0))
    screen.blit(black_strip, (0, image_rect.bottom))
    screen.blit(black_strip, (0, 0))
screen.blit(image, (0, 0))
pygame.display.flip()
time.sleep(1)
sound = pygame.mixer.Sound(select_audio())
sound.play()

while pygame.mixer.get_busy():
    time.sleep(0.1)
time.sleep(0.5)
pygame.quit()