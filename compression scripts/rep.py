import time
import numpy as np

def replace(div, color) :

    for I in range(1, div + 1) : 
        SEQ_FILTERED = list()

        print('Replacing file : SPLIT_PLAIN_' + color + '_' + str(I) + '.txt')

        with open('seq_' + color + '_' + str(I) + '.txt' , 'r') as f:
            for i in f : 
                temp = list()
                line = i.split()
                #print(line)
                for j in line : 
                    temp.append(j)

                SEQ_FILTERED.append(temp)

        
        #print(SEQ_FILTERED)

        DATA_PLAIN = list()

        with open('SPLIT_PLAIN_' + color + '_' + str(I) + '.txt', 'r') as f:
            for i in f : 
                temp = list()
                line = i.split()
                for j in line : 
                    temp.append(j)
                DATA_PLAIN.append(temp)

        
        #REPLACE DATA
        SEQ_COUNT = 0
        REPLACE_D = list()

        for i in range(len(DATA_PLAIN)) :
            REPLACE_D.append([])

        SEQ_COUNT = 1

        SEQ_FINAL_256 = list()

        win = 256
        k = 0
        for k in range(len(SEQ_FILTERED)) : 
            if SEQ_COUNT == 256 : 
                break
            L = len(SEQ_FILTERED[k])
            sup = 0
            print(str(SEQ_COUNT) + ' ' + str(SEQ_FILTERED[k]))
            print()
            for i in range(len(DATA_PLAIN)) : 
                #temp = list()
                for j in range(0, len(DATA_PLAIN[i]) - L + 1) :
                    if DATA_PLAIN[i][j:j + L] == SEQ_FILTERED[k] :
                        DATA_PLAIN[i][j : j + L] = [SEQ_COUNT]
                        REPLACE_D[i].append(j+1)
                        sup+=1
            if sup == 0 : 
                win += 1
            else : 
                SEQ_FINAL_256.append(SEQ_FILTERED[k])
                SEQ_COUNT += 1
            #print(SEQ_COUNT)
            print(str(sup) + ' ' + str(win) + ' ' +str(k))
            #REPLACE_D.append(temp)

        file = open('RESULT_' + color + '_' + str(I) + '.txt', 'w')
        for i in range(len(DATA_PLAIN)) : 
            
            for j in DATA_PLAIN[i] : 
                file.write(str(j) + ' ')
            
            file.write('0 ')
            
            for j in REPLACE_D[i] : 
                file.write(str(j) + ' ')
            file.write('0\n')

        '''
        file = open('REPLACE_D_B.txt', 'w')
        for i in REPLACE_D : 
            for j in i :
                file.write(str(j) + ' ')
            file.write('\n')
        ''' 
        file.close()
        file = open('SEQ_FINAL_' + color + '_' + str(I) + '.txt', 'w')
        for i in SEQ_FINAL_256: 
            for j in i :
                file.write(str(j) + ' ')
            file.write('0\n')
        
        file.close()

    return 

def change(div, color) : 
    
    for I in range(1, div + 1) : 
        seq = list()

        with open('seq_' + color + '_' + str(I) + '.txt', 'r') as f:
            for i in f : 
                temp = list()
                tempX = list()
                line = i.split()
                #print(line)
                size = len(line)
                temp.append(int(line[-1]) * int((size - 2) / 2))
                for j in range(0, size - 2, 2):
                    temp.append(int(line[j]))
                
                #print(temp)
                #seq_count.append(tempx)
                seq.append(temp)
                #x = input()

        seq.sort(reverse=True)

        seq_final = seq[0:min(700, len(seq))]
        print(len(seq_final))
        seq_sup_count = list()
        '''
        for i in range(len(seq_final)) : 
            seq_sup_count.append(seq_final[i][0])
            seq_final[i] = seq_final[i][1:len(seq_final[i])]
        '''

        file = open('seq_' + color + '_' + str(I) + '.txt', 'w')

        for i in seq_final : 
            for j in range(1,len(i)): 
                file.write(str(i[j]) + ' ')
            file.write('\n')
        file.close()

    return 


def combine(div, color, H, W) : 

    master = 'MASTER_' + color + '.txt'
    fbase = 'RESULT_' + color + '_'
    sbase = 'SEQ_FINAL_' + color + '_'
    

    frame_count = H * W;

    data = []
    for i in range(frame_count) : 
        data.append('')

    
    for I in range(1, div + 1) :
        print('Merging File : '  + str(I))
        with open(fbase + str(I) + '.txt', 'r') as f : 
            prog = 0
            for line in f :
                line = line[0 : -1] + ' '
                data[I] += line 
                print(str(prog) + ' ' + str(format(prog / frame_count * 100, '0.2f')) + '%' ,end = '\r')
                prog += 1

    file = open(master, 'w')

    prog = 1
    print('Writing Master file ...')
    for I in data : 
        I += '\n'
        file.write(I)
        print(str(prog) + ' ' + str(format(prog / frame_count * 100, '0.2f')) + '%' ,end = '\r')
        prog += 1
    file.close()

    prog = 1

    #code_table = 'CODE_TABLE_' + color + '.'
    #file = open(, 'w')
    code_table = list()
    for I in range(1, div + 1) :
        print('Merging Seq data : '  + str(I))
        with open(sbase + str(I) + '.txt', 'r') as f : 
            prog = 0
            for line in f :
                line = line.split()
                line = list(map(int, line))
                code_table.append(line)
                print(str(prog) + ' ' + str(format(prog / frame_count * 100, '0.2f')) + '%' ,end = '\r')
                prog += 1  
            code_table.append([0,0])

    code_table = np.array(code_table)
    np.save('code_table_' + color + '.npy', )
    return                 

start_time = time.time()
#change(10, 'R')
#replace(10, 'R')

combine(10, 'R', 240, 320)
print("--- %s seconds ---" % (time.time() - start_time))
