# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:00:20 2021

@author: leoboeger
"""
# uses cv2 to flip images, all images in one folder if bulk == True
# else only by path specified images are processed
# potenially extenable to a whole lot more processing
# with GUI to ask for which processing should be applied and which folder/path to apply it to

import os
import cv2

bulk = True
filesFound = []
operation = 'flip'

if bulk == True:
    img_dir_in = input('img directory: ')

    for f in os.listdir(img_dir_in):
        if f.__contains__('.png'):
            file = os.path.join(img_dir_in,f)
            filesFound.append(file) 
else:
    img_path_in = input('img path: ')
    filesFound.append(img_path_in)
        
for img_path in filesFound:
    img = cv2.imread(img_path)
    if operation == 'flip':
        img_flipped = cv2.flip(img,1)
        cv2.imwrite(img_path,img_flipped)
