

def tree_check(x,y,list,direction):
    coordinates = [x,y]
    print('checking',x,y)
    if coordinates in list:
        print('found and rejected during:',direction,x,y)
    else:
        print('found from:',direction,x,y)
        return list.append(coordinates)



def main():
    

    array = []
    #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D8.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  

    print(array)
    print(array[0])

    col = len(array[0])
    row = len(array)

    print(col,row)

    #builds 2d list for worst case amount of overlaps
    alreadyCounted = [[] for i in range(row*2 + col*2)]
    #alreadyCounted = []


    #x is horizontal y is vertical (reversed) from normal coords
    #check from Left
    for curCol in range(0,col,1):
        print('top')
        largestTree = 0
        for curRow in range(0,row,1):
            #print(array[curRow]curCol)
            #always adds bottom layer of tree since its on the outside
            if curRow == 0 or curCol == 0 or curCol == col - 1 or curRow == row - 1:             
                #tree_check(x,y,alreadyCounted)
                largestTree = int(array[curRow][curCol])
            else:
                if largestTree < int(array[curRow][curCol]):
                    tree_check(curCol,curRow,alreadyCounted,'top')
                    largestTree = int(array[curRow][curCol])

    #check from Bottom

    for curCol in range(0,col,1):
        print('bottom?')
        largestTree = 0
        for curRow in range(row-1,-1,-1):
            #print(array[curRow]curCol)
            #always adds bottom layer of tree since its on the outside
            if curRow == 0 or curCol == 0 or curCol == col - 1 or curRow == row - 1:             
                #tree_check(x,y,alreadyCounted)
                largestTree = int(array[curRow][curCol])
            else:
                if largestTree < int(array[curRow][curCol]):
                    tree_check(curCol,curRow,alreadyCounted,'bottom')
                    largestTree = int(array[curRow][curCol])


    for curRow in range(0,row,1):  
        print('left')  
        largestTree = 0
        for curCol in range(0,col,1):                     
            #print(array[curRow]curCol)
            #always adds bottom layer of tree since its on the outside
            if curRow == 0 or curCol == 0 or curCol == col - 1 or curRow == row - 1:             
                #tree_check(x,y,alreadyCounted)
                largestTree = int(array[curRow][curCol])
            else:
                if largestTree < int(array[curRow][curCol]):
                    tree_check(curCol,curRow,alreadyCounted,'left')
                    largestTree = int(array[curRow][curCol])


    for curRow in range(0,row,1):  
        print('right')  
        largestTree = 0
        for curCol in range(col-1,-1,-1):                     
            #print(array[curRow]curCol)
            #always adds bottom layer of tree since its on the outside
            if curRow == 0 or curCol == 0 or curCol == col - 1 or curRow == row - 1:             
                #tree_check(x,y,alreadyCounted)
                largestTree = int(array[curRow][curCol])
            else:
                if largestTree < int(array[curRow][curCol]):
                    tree_check(curCol,curRow,alreadyCounted,'right')
                    largestTree = int(array[curRow][curCol])


    finalList = list(filter(None, alreadyCounted))
    answer = len(finalList) + row*2+col*2 - 4
    print(answer)

if __name__ == "__main__":
    main() 

