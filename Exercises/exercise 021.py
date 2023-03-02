# Exercício 021 - Faça um programa em Python que abra e reproduza um áudio de um arquivo em MP3

import pygame
pygame.init()
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait()
