
import os
import sys
import shutil
import cv2

def video2frames(args):
    # convert to vars:
    # args = vars(parser.parse_args())
    video = args['video']
    output_folder = args['im_or_folder']
    # note that im_or_folder is now the output folder of te video2frames, but it will be the input folder when doing inference
    ####################################
    # check if video exists:
    if not os.path.isfile(video):
        sys.exit('Error:    No input video found')

    # set frames output path, ...we want to be sure that not residual images remain there:
    __cwd = os.getcwd() 
    print('_____cwd:',__cwd)
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
        os.makedirs(output_folder)
    else:
        os.makedirs(output_folder)

        # for frame identity
    vid = cv2.VideoCapture(video)
    fps = vid.get(cv2.CAP_PROP_FPS)
    #####
    index = 0
    while (True):
        # Extract images
        ret, frame = vid.read()
        # end of frames
        if not ret:
            break
        # Save images:
        name = output_folder + '/frame' + str(index) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        # next frame
        index += 1
    vid.release()
    return fps


if __name__=='__main__':
    args = {}
    args['video'] = '/home/pi/results/my_video.h264'
    args['im_or_folder'] = '/home/pi/results/frames_from_video'
    video2frames(args)

