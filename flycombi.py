#encoding: utf-8(para las ñ)
import grafo
import heapq
from collections import deque
import fileinput

'''TENER CUIDADO CON LAS VARIABLES QUE SE REPITEN, NO PASA NADA?'''


def flycombi(archivos):
    for linea in fileinput.input():
        comandos = linea
    return



'''MAIN/APENAS ABRE EL PROGRAMA'''
def main():
    datos = input()
    archivos = datos.split(" ")
    print(datos)

    for s in archivos:
        print (s,len(s))

    flycombi(archivos)