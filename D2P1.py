

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
        #print((array[j+1] -array[j]+3)%3)

        #all results below have their value adjusted by 1 for rounds score since my rock is 0

        #Draw
        #if they are the same we know its a draw
        if array[j] == array[j+1]:
            #print(array[j],array[j+1])
            #print('draw')
            roundScore = array[j+1]+1+3

        #win
        #if the result of the calc below is 1 we know its a win 
        elif ((array[j+1] -array[j]+3)%3 == 1):
            #print(array[j],array[j+1])
            #print('win')
            roundScore = array[j+1]+1+6
        #loss
        #if the other ifs didnt trigger its a loss
        else:
            #print(array[j],array[j+1])
            #print('loss')
            roundScore = array[j+1]+1
        print(roundScore)
        total += roundScore
        roundScore = 0

    print(total)

if __name__ == "__main__":
    main() 

