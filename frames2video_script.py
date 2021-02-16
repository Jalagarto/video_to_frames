import cv2
import numpy as np
import os
import sys
import argparse
from os.path import isfile, join


def frames2video(parameters):  # pathIn,pathOut,fps):
    frame_array = []
    path = parameters['im_or_folder'] + '/'
    pathout = parameters['video']
    files = [f for f in os.listdir(path) if isfile(join(path, f))]
    if files:
        img = None
        size = (0,0)
        fps = parameters['fps']
        # for sorting the file names properly
        files.sort(key = lambda x: int(x[5:-4]))
        #append the images
        for i in range(len(files)):
            filename = path + files[i]
            # reading each files
            img = cv2.imread(filename)
            print('filename:', filename)
            height, width, layers = img.shape
            size = (width, height)
            # inserting the frames into an image array
            frame_array.append(img)
        # cv2.imwrite('messigray.jpg', img)
        print('pathOut:', path, 'fps:', fps, 'size:', size)
        try:
            out = cv2.VideoWriter(pathout, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)  # mp4v  DIVX
            for i in range(len(frame_array)):
                # writing to an image array
                out.write(frame_array[i])
            out.release()
        except:
            print('corrupt frames')
            raise
    else:
        print('There were no files to create a video')
        
        


