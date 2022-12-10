
def main():
    
    array = []
    #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D9_test.txt","r") as f:
        for val in f.read().split():
            array.append((val))  

    print(array)

    headPos = [0,0]
    tailPos = [0,0]

    print(headPos)
    while len(array)>0:
        dir = array[0]
        dist = int(array[1])
        array.pop(0)
        array.pop(0)

        print(dir,dist)

        if dir == 'R':
            headPos[0] += dist
        elif dir == 'L':
            headPos[0] -= dist
        elif dir == 'U':
            headPos[1] += dist
        elif dir == 'D':
            headPos[1] -= dist

        print(headPos)

        if headPos == tailPos:
            #same position do nothing
            continue
        elif headPos[0] == tailPos[0]:
            #they are one the same vertical
        elif headPos[1] == tailPos[1]:
            #they are on the same row



    




if __name__ == "__main__":
    main() 



