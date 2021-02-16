import cv2
import numpy as np
import os
import sys
from os.path import isfile, join

 
def main(pathIn,pathOut,fps):
    # pathOut = "/home/ubuntu/detectron/tools/detectronManager/processing/frames.mp4"  ### modified
    print("line9__frames2video_modified____: pathIn: {0},pathOut: {1},fps: {2}".format(pathIn,pathOut,fps))  
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))] 

    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename= join(pathIn, files[i])
        #reading each files
        img = cv2.imread(filename)
        print('filename:',filename)
        height, width, layers = img.shape
        size = (width,height)        
        #inserting the frames into an image array
        frame_array.append(img)  
    # cv2.imwrite('messigray.jpg',img)    # Javi, is this line necessary?
    print('pathOut:',pathOut,'fps:',fps,'size:',size)   
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)  # mp4v  DIVX
    # mpeg4    mp4v    
    for i in range(len(frame_array)):
        # writing to an image array
        out.write(frame_array[i])    
    out.release()
    

if __name__=="__main__":
    pathIn = "/home/ubuntu/detectron/tools/detectronManager/processing/example6-client-20190605_100237.43_frames"
    pathOut = "/home/ubuntu/detectron/tools/detectronManager/processing/vid2.mp4"
    main(pathIn, pathOut, 30)