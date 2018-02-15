#Root file
from __future__ import print_function
from collections import defaultdict
import cv2
import os
import numpy as np
import sys
import csv
import time
import _thread
import math
#import split

def recoverFrame(R,G,B,H,W,frameCount,frameNo):

    frameR = [[] for i in range(H)]
    frameG = [[] for i in range(H)]
    frameB = [[] for i in range(H)]
    
    count = 0
    for i in range(0,H):
        for j in range(0,W):
            
            frameR[i].append(R[count][frameNo])
            frameG[i].append(G[count][frameNo])
            frameB[i].append(B[count][frameNo])
            count += 1
    
    print()
    print(frameR[100][100])
    print(frameG[100][100])
    print(frameB[100][100])
        

    frameR = np.array(frameR)
    frameG = np.array(frameG)
    frameB = np.array(frameB)

    img = cv2.merge([frameB,frameG,frameR])
    cv2.imshow("img",img)        
    cv2.waitKey(0);

    return img

def recoverVideo(data):




    return cap

##########################
#load video by VideoCapture
def loadVideo(file):
    cap = cv2.VideoCapture(file)
    return cap


#get data from frame
def getList(cap,H,W,frameCount):
    
    print("Initializing..")
    dataR = list()
    dataG = list()
    dataB = list()
    #Create container
    for j in range (H):
        dataR.append([])
        dataG.append([])
        dataB.append([])
    
    for i in range(H):
        for j in range(W):
            dataR[i].append([])
            dataG[i].append([])
            dataB[i].append([])


    #Transfer values to the container
    print("Capturing frames..")
    #print("in")
    count = 0
    while(cap.isOpened()):
        #print("in1")z
        ret, frame = cap.read()
        count += 1
        #name = "frame%d.jpg"%count
        #cv2.imwrite(name, frame)
        if count > frameCount:
            break;

        for i in range(H):
            for j in range(W):
                if(frame[i][j][2] != 0) : 
                    dataR[i][j].append(frame[i][j][2])
                else : 
                    dataR[i][j].append(1)
                
                if(frame[i][j][1] != 0) : 
                    dataG[i][j].append(frame[i][j][1])
                else : 
                    dataG[i][j].append(1)

                if(frame[i][j][0] != 0) : 
                    dataB[i][j].append(frame[i][j][0])
                else : 
                    dataB[i][j].append(1)
                
                
                #dataG[i][j].append(frame[i][j][1])
                #dataB[i][j].append(frame[i][j][0])
        
    
    print("Writing List...")
    #print(data[100][100][0])
    cap.release()
    mDataR = list()
    mDataG = list()
    mDataB = list()
    for i in range(H):
        for j in range(W):
            tempR = list()
            tempG = list()
            tempB = list() 
            for k in range(frameCount):
                tempR.append(dataR[i][j][k])
                tempG.append(dataG[i][j][k])
                tempB.append(dataB[i][j][k])

            mDataR.append(tempR)
            mDataG.append(tempG)
            mDataB.append(tempB)
    print('Finished Writing List!..')
    return mDataR, mDataG, mDataB

def RLE(C):

    d = list()
    CX = list()
    count = 1
    
    l = len(C[0])
    for i in C:
        temp = list()
        tempd = list()
        count = 1
        k = 0
        for j in range(0, l-1) :
            cutFlag = 0
            if(i[j] == i[j + 1]) :
                if(count == 1):
                    temp.append(i[j])
                    #tempd.append(k);
                if(count > 254) : 
                    temp.append(count)
                    #temp.append(i[j])
                    tempd.append(k)
                    count = 0
                    k +=2
                count += 1
            else : 
                if count > 1:
                    temp.append(count)
                    tempd.append(k)
                    count = 1
                    k +=2
                else:
                    temp.append(i[j])
                    k += 1
                
        #print(count)
        #m = input()
        if count > 1:
            tempd.append(k)
            temp.append(count)
            count = 1
        else:
            temp.append(i[j])

        #print(temp)
        #print(tempd)
        CX.append(temp)
        d.append(tempd)
    #print(CX)
    #print(d)
        
    return CX, d
   

def write_data(X, color, div, frameCount) : 
    print("Writing data to file : "  + color)
    
    base = 'SPLIT_PLAIN_' + color + '_'
    base_mine = 'SPLIT_MINING_' + color + '_'
    files = []
    files_mine =[]
    for i in range(1, math.ceil(frameCount / div) + 1) : 
        file = open(base + str(i), 'w')
        files.append(file)
        file = open(base_mine + str(i), 'w')
        files_mine.append(file)

    #file = open(name,'w')
    #file1 = open(name1,'w')

    #1 2 3 4 5 6 7 8 9 10
    print(len(X[0]))
    for j in X:
        fI = 0
        for i in range(len(j)):
            a = str(j[i])
            #print(fI)
            #print(i)
            files[fI].write(a + ' ')
            files_mine[fI].write(a + ' -1 ')
            
            if((i + 1) % div) == 0 : 
                files[fI].write('\n')
                files_mine[fI].write('-2\n')
                fI += 1
        
        files[-1].write('\n')
        files_mine[-1].write('-2\n')
 
    for i in range(len(files)) : 
        files[i].close()
        files_mine[i].close()

    '''
    print("Writing data to RLE dictionary : "  + dict)
    file = open(dict, 'w')
    for j in DX : 
        for i in j : 
            a = str(i)
            file.write(a + ' ')
        file.write('\n')
    file.close()
    '''
    return 
if __name__ == "__main__":
    start_time = time.time()
    
    video_name='big_buck_bunny_240p_5mb.mp4'
    #video_name = 'bunny.mp4'
    cap = loadVideo(video_name)
    #Video Properties
    H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print("Height : " + str(H))
    print("Width : " + str(W))
    print("Frame Count : " + str(frameCount))
    

    R, G, B = getList(cap, H, W, frameCount)   
     
    #write_data(R, 'DATA_PLAIN_R.txt', 'DATA_MINING_R.txt', 'DRLE_R.txt')
    #del(R)

 
    #write_data(G, 'DATA_PLAIN_G.txt', 'DATA_MINING_G.txt','DRLE_G.txt')
    #del(G)
    
    #write_data(B, 'DATA_PLAIN_B.txt', 'DATA_MINING_B.txt', 'DRLE_B.txt')
    #del(B)

    #split.split('DATA_PLAIN_R.txt', 'DATA_MINING_R.txt', 'R', 2, H, W)
    #split.split('DATA_PLAIN_G.txt', 'DATA_MINING_G.txt', 'G', 2, H, W)
    #split.split('DATA_PLAIN_B.txt', 'DATA_MINING_B.txt', 'B', 2, H, W)
    

    M = [[1,2,3,4,5,6,7,8,9,1],
         [3,6,7,4,7,8,9,2,0,1],
         [2,6,3,5,8,6,8,0,2,1]]
    write_data(R,'R',100,frameCount)
    write_data(G,'G',100,frameCount)
    write_data(B,'B',100,frameCount)
    #write_data(R,'R',100,frameCount)

    print("--- %s seconds ---" % (time.time() - start_time))
    
   
