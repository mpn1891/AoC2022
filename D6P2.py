
def main():
     
    array = []
    #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D6.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  

    wrkString = ''
    repeatFound = 0
    #loops over each line ended up only being one but didnt realize that
    for x in array:
        #creates a string with the first 13 characters, P1 was only 3
        wrkString = x[:13]
        #for every character in current input starting at 14th char (index 13)
        for i in range(13,len(x),1):
            #adds the next character to the working string
            wrkString += x[i]
            #for every char in the wrkstring
            for j in wrkString:
                #check if the count of that character is greater than one, is so say repeat found and break
                if wrkString.count(j) > 1:
                    repeatFound = 1   
                    break
            #if no repeats are found this is the answer
            if repeatFound == 0:
                print('Found first unique',i+1)

                #reset the string in case multiple inputs were having to be checked, not the case so doesnt matter
                wrkString = ''
                break
            #if a repeat was found, remove first char of wrkString in prep for next round and reset the repeat found
            else:
                wrkString = wrkString[1:]
                repeatFound = 0
                continue

if __name__ == "__main__":
    main() 
