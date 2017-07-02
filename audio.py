import pygame

def play_shoot():
    soundwav = pygame.mixer.Sound('audio/shoot.wav')
    soundwav.play()

def play_hit_alien():
    soundwav = pygame.mixer.Sound('audio/hit_alien.wav')
    soundwav.play()
    
def play_dead():
    soundwav = pygame.mixer.Sound('audio/dead.wav')
    soundwav.play()
    
def play_next_level():
    soundwav = pygame.mixer.Sound('audio/next_level.wav')
    soundwav.play()
    
def play_gameover():
    soundwav = pygame.mixer.Sound('audio/gameover.wav')
    soundwav.play()

def play_bg_music():
    soundwav = pygame.mixer.Sound('audio/bg_music.wav')
    soundwav.play(-1)
