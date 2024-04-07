import pygame

#inicializa o mixer de audio do pygame
pygame.mixer.init()

#carrega o arquivo de audio mp3
pygame.mixer.music.load('url do video')

#reproduz o arquivo de audio
pygame.mixer.music.play()

#mantem o programa rodando ate que a musica termine
while pygame.mixer.music.get_busy():
    continue