import math
import numpy as np
import cv2
from copy import copy, deepcopy
import time



def loadVideo(file):
    cap = cv2.VideoCapture(file)
    return cap

start_time = time.time()

W = 320
H = 240

B = list()
G = list()
R = list()

b = 0
g = 0
r = 0

prog = 1
print('Reading master R...∫∆∆∆∆')
with open('MASTER_R.txt', 'r') as f : 
    for i in f : 
        print(str(prog) + ' ' + str(format(prog / (H * W) * 100, '0.2f')) + '%' ,end = '\r')
        line = i.split()
        temp = list()
        for j in line : 
            R.append(int(j))
            r += 1
        prog += 1
        #B.append(temp)

prog = 1
print('Reading master G...')
with open('MASTER_G.txt', 'r') as f : 
    for i in f : 
        print(str(prog) + ' ' + str(format(prog / (H * W) * 100, '0.2f')) + '%' ,end = '\r')
        line = i.split()
        temp = list()
        for j in line : 
            G.append(int(j))
            g += 1
        prog += 1
        #G.append(temp)

prog = 1
print('Reading master B...')
with open('MASTER_B.txt', 'r') as f : 
    for i in f : 
        print(str(prog) + ' ' + str(format(prog / (H * W) * 100, '0.2f')) + '%' ,end = '\r')
        line = i.split()
        temp = list()
        for j in line : 
            B.append(int(j))
            b += 1
        prog += 1
        #G.append(temp)


frame_count = max(b,max(g,r)) / (H * W)
frame_count = int(math.ceil(frame_count))

print('New Frame Count :  ' + str(frame_count))

frame = list()
temp = list()
for i in range(320) : 
    temp.append(0)
for i in range (240) : 
    frame.append(temp)




cB = 0
cG = 0
cR = 0
####

W = 320
H = 240
format = ''
fourcc = cv2.VideoWriter_fourcc('H','E','V','C')
vid = None
output = 'bunny_240p5mb_compressed.mp4'
fps = 24


####
#writer = cv2.VideoWriter(output, fourcc, fps, (W, H) , True)
'Writing frames çç∫∫∫∆...'
#©√√√∫˜˜µ≤≤≥≥≥÷ç≈∆∆∆
frameB = deepcopy(frame)
frameG = deepcopy(frame)
frameR = deepcopy(frame)

prog = 1
for k in range(frame_count) : 
    frameB = deepcopy(frame)
    frameG = deepcopy(frame)
    frameR = deepcopy(frame)
    for i in range(H) : 
        for j in range(W) : 
            if(cB < len(B)) : 
                frameB[i][j] = B[cB]
                cB += 1
            if(cG < len(G)) : 
                frameG[i][j] = G[cG]
                cG += 1
            if(cR < len(R)) : 
                frameR[i][j] = R[cR]
                cR += 1
    #print(str(prog) + ' ' + str(format(prog / (H * W) * 100, '0.2f')) + '%' ,end = '\r')
    #prog += 1
    print(prog, end='\r')
    print('Wrote image : ' + str(k) + '.png')
    img = cv2.merge((np.array(frameB),np.array(frameG), np.array(frameR)))
    print(img[200][200])
    cv2.imwrite(str(k) + '.png', img)
    #input()

#input()
frame = []
for i in range(frame_count) :
    name = str(i) + '.png' 
    frame.append(cv2.imread(name))

height , width , layers =  frame[0].shape

print('Height of image : ' + str(height))
print('Width of image : ' + str(width))

writer = cv2.VideoWriter(output, fourcc, fps, (width, height) , True)

#file = open('hello.txt', 'w') 
for i in frame :
    writer.write(i)   

cv2.destroyAllWindows()
writer.release()

cap = loadVideo(output)
#Video Properties
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(str(h) + ' ' + str(w) + ' ' + str(frameCount))

print("--- %s seconds ---" % (time.time() - start_time))
