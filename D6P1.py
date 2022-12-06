
def main():
     
    array = []
    #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D6.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  

    print(array)
    wrkString = ''
    repeatFound = 0
    #loops over each line
    for x in array:
        #creates a string with the first 3 characters
        wrkString = x[:3]
        #for every character in current input starting at 4th char (index 3)
        for i in range(3,len(x),1):
            #print(x[i])
            wrkString += x[i]
            for j in wrkString:
                if wrkString.count(j) > 1:
                    print('checking for char',j,wrkString.count(j))
                    repeatFound = 1   
                    break

            
            if repeatFound == 0:
                print('Found first unique',i+1)
                print(wrkString)
                wrkString = ''
                break
            else:
                wrkString = wrkString[1:]
                repeatFound = 0
                continue

if __name__ == "__main__":
    main() 