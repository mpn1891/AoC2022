


def main():
    
    array = []
    #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D8_test.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  

    print(array)

    width = len(array[0])
    height = len(array)

    #builds 2d list for worst case amount of overlaps
    alreadyCounted = [[] for i in range(height*2 + width*2)]

    #check from Top
    curTree = 0
    nextTree = 0
    treeCount = 0

    #x is horizontal y is vertical (reversed) from normal coords
    for x in range(0,width,1):
        for y in range(0,height,1):
            curTree = array[y][x]
            nextTree = array[y+1][x]
            print(curTree)
            print(nextTree)
            if nextTree < curTree:
                continue
            elif y == 0:
                break
            else:
                treeCount += 1
                coordPair = str(x)+str(y)
                alreadyCounted.append(coordPair)


    print(alreadyCounted)








if __name__ == "__main__":
    main() 

