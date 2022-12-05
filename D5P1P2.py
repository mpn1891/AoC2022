
def main():
    import re

    stacks = []
    stacks.append('FTNZMGHJ')
    stacks.append('JWV')
    stacks.append('HTBJLVG')
    stacks.append('LVDCNJPB')
    stacks.append('GRPMSWF')
    stacks.append('MVNBFCHG')
    stacks.append('RMGHD')
    stacks.append('DZVMNH')
    stacks.append('HFNG')
      
    array = []
    #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D5_lower.txt","r") as f:
        for val in f.read().splitlines():
            valClean = re.split(r'move | from | to ',val)
            array.append((valClean))  

    #im dumb and made them backwards too lazy to redo
    orgStacks = [i[::-1] for i in stacks]
    #creates copy for P2, doing both P1 and P2 here
    orgStacksP2 = orgStacks.copy()

    #cleans a first empty string not sure why thats showing up
    for x in array:
        x.pop(0)

    #Part 1
    for command in array:
        #gets commands
        numToMove = int(command[0])
        sourceStack = int(command[1])-1
        tarStack = int(command[2])-1

        #start and end for string slice
        start = len(orgStacks[sourceStack]) - numToMove
        end = len(orgStacks[sourceStack])

        #gets string
        stringToMove = orgStacks[sourceStack][start:end]

        #Skips the Reverse for P2
        stringToMove = stringToMove[::-1]

        #adds to target
        orgStacks[tarStack] += stringToMove

        #removes from source
        orgStacks[sourceStack] = orgStacks[sourceStack][:-numToMove]
    print(orgStacks)

    #Part 2
    for command in array:
        #gets commands
        numToMove = int(command[0])
        sourceStack = int(command[1])-1
        tarStack = int(command[2])-1

        #start and end for string slice
        start = len(orgStacksP2[sourceStack]) - numToMove
        end = len(orgStacksP2[sourceStack])

        #gets string
        stringToMove = orgStacksP2[sourceStack][start:end]

        #Skips the Reverse for P2

        #adds to target
        orgStacksP2[tarStack] += stringToMove

        #removes from source
        orgStacksP2[sourceStack] = orgStacksP2[sourceStack][:-numToMove]
             
        
    print(orgStacksP2)

if __name__ == "__main__":
    main() 