


def main():
    array = []
   #reads into one array with both mine and their responses
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D2.txt","r") as f:
        for val in f.read().split():
            array.append((val))  

    #changes letters to numbers
    for i, n in enumerate(array):
        if n == 'A' or n == 'X':
            array[i] = 0
        elif n == 'B' or n == 'Y':
            array[i] = 1
        else:
            array[i] = 2

    #print(array)

    roundScore = 0
    total = 0

    for j in range(0,len(array),2):
        #draw
        #if we need a draw, then we just match what the first throw was
        if array[j+1] == 1:
            roundScore = array[j]+1+3
            #print(roundScore)
            #print('draw')

        #win
        #if we need a win, add one to to theirs, and circle back to 0 if we exceed 2 (Rock = 0, Paper = 1,Sciccors = 2)
        if array[j+1] == 2:
            thrown = array[j]+1
            if thrown > 2:
                thrown = 0
            roundScore = thrown+1+6
            #print(roundScore)

        #loss
        #if we need a loss, sub one from theirs, and circle back to 0 if we exceed 2 (Rock = 0, Paper = 1,Sciccors = 2)
        elif array[j+1] == 0:
            thrown = array[j]-1
            if thrown < 0:
                thrown = 2
            roundScore = thrown+1
            #print(roundScore)
 
        total += roundScore
        roundScore = 0
        thrown = 0
        
        

    print(total)

            





if __name__ == "__main__":
    main() 

