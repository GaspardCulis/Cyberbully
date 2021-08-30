#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 21:39:55 2021

@author: anonisouris
"""


#import stockfish
from time import sleep
import numpy as np
import cv2
import pyautogui

plateau = np.full((8,8)," ")


screen_origin = (200,200)
screen_size = (500,500)
piece_size = (int(500/8),int(500/8))

from os import listdir
from os.path import isfile, join
filenames = [f for f in listdir('pieces/') if isfile(join('pieces/', f))]




def filtrer(position):
    max_distance = 20
    out = list()
    adding = True
    for i in position:
        for j in out:
            d = np.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2)
            if d < max_distance:
                adding = False
        if adding:out.append(i)
    return out


def locate_pieces():
    threshold = 0.60

    Screenshot = pyautogui.screenshot()
    Screenshot.save('screen.png')
    
    screen = cv2.imread("screen.png",cv2.IMREAD_UNCHANGED)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2RGBA)
    for p in filenames:
        piece = cv2.imread("pieces/"+p,cv2.IMREAD_UNCHANGED)
        result = cv2.matchTemplate(screen,piece,cv2.TM_CCOEFF_NORMED)
        
        yloc,xloc = np.where(result>threshold)
        positions = list(zip(xloc,yloc))
        #positions = filtrer(positions)
        w,h = piece.shape[1],piece.shape[0]
        
        for i in positions:
            cv2.rectangle(screen,(i[0],i[1]),(i[0]+w,i[1]+h),(255,0,0),2)

        
    cv2.imshow("toto",screen)
    cv2.waitKey()
    cv2.destroyAllWindows()



sleep(5)
"""
posXY = pyautogui.position() 
print(posXY, pyautogui.pixel(posXY[0], posXY[1]))

exit()
"""

locate_pieces()


#search = screen_search.Search("pieces/rb.png")
#print(search.imagesearch())
