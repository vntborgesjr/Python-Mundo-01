# Desafio 021 - Faça um programa em Python que abre e reproduza o audio de um arquivo mp3.

'''
import os
os.startfile('01. Faixa 1.mp3.mp3')
'''

import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
pygame.event.wait()