

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
    maxView = 0
    
    for curCol in range(0,col,1):
        for curRow in range(0,row,1):
            
            tempView = 0
            houseCol = curCol
            houseRow = curRow
            print('testing position','row:',houseRow,'col',houseCol)
            
            #check up
            if curRow == 0:
                tempUp = 0
            else:               
                nextCol = curCol
                nextRow = curRow - 1
                tempUp = 0
                while nextRow > -1:   
                    tempUp += 1
                    if array[houseRow][houseCol] <= array[nextRow][nextCol]:
                        break
                        
                    nextRow -= 1
            #check down
            if curRow == row-1:
                tempDown = 0
            else:               
                nextCol = curCol
                nextRow = curRow + 1
                tempDown = 0
                while nextRow < row:
                    tempDown += 1
                    if array[houseRow][houseCol] <= array[nextRow][nextCol]:
                        break
                    nextRow += 1

            #check left
            if curCol == 0:
                tempLeft = 0
            else:               
                nextCol = curCol + 1
                nextRow = curRow
                tempLeft = 0
                while nextCol < col:    
                    tempLeft += 1
                    if array[houseRow][houseCol] <= array[nextRow][nextCol]:
                        break
                    nextCol += 1

            #check Right
            if curCol == col-1:
                tempRight = 1
            else:               
                nextCol = curCol - 1
                nextRow = curRow
                tempRight = 0
                while nextCol > -1:   
                    tempRight += 1
                    if array[houseRow][houseCol] <= array[nextRow][nextCol]:
                        break                       
                    nextCol -= 1

            tempView = tempUp * tempDown * tempLeft * tempRight
            print(tempUp,tempDown,tempLeft,tempRight,tempView)

            if tempView > maxView:
                maxView = tempView
                
            tempUp = 0
            tempDown = 0
            tempLeft = 0
            tempRight = 0
            tempView = 0

    print(maxView)

if __name__ == "__main__":
    main() 

