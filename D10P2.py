
def main():
    
    array = []
    #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D10.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  

    #print(array)
    
    cycle = 1
    curCommand = ''
    lastExec = 0
    nextExec = 0
    addOpp = 0
    value = 1
    c2 = 0
    p1Answer = 0

    importantCycles =[20,60,100,140,180,220]

    screenString = ''

    while cycle < 241:
        #print(curCommand)
        #print(nextExec)

        if nextExec == cycle:
            #print('executing')
            if addOpp == 1:
                value += int(c2)
            lastExec = cycle
            nextExec = 0
            addOpp = 0
            curCommand = ''

        #do math at the start of the cycle for the during part

        if curCommand == '':
            curCommand = array[0]
        

        #gets next cycle to execute
        if 'add' in curCommand and nextExec == 0:
            c1,c2 = curCommand.split()
            nextExec = cycle + 2
            addOpp = 1
            array.pop(0)

        elif 'noop' in curCommand and nextExec == 0:
            nextExec = cycle + 1
            array.pop(0)

        print('value during cycle:',cycle,'is',value)

        
        if cycle in importantCycles:
            p1Answer += (cycle*value)
            #print(p1Answer)

        crtDrawPos = cycle % 40 -1
        print(crtDrawPos)
        if crtDrawPos == value or crtDrawPos == value + 1 or crtDrawPos == value - 1:
            screenString += '#'
        else:
            screenString += '.'


        cycle += 1


        desiredLength = 40
        
        #print(screenString)

        

    print([screenString[i:i+desiredLength] for i in range(0, len(screenString), desiredLength)])
           
        


if __name__ == "__main__":
    main() 


