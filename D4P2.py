

def main():
    import re
    array = []  
   #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D4.txt","r") as f:
        for val in f.read().splitlines():
            valClean = re.split(r',|-',val)
            array.append((valClean))  

    #intializes 2d lists of proper size
    elfOne = [[] for i in range(len(array))]
    elfTwo = [[] for i in range(len(array))]

    #reads the base array into each elf's list
    for i in range(0,len(array),1):
        elfOne[i]=array[i][:-2]
        elfTwo[i]=array[i][2:]

    #need to fix the having to convert int at time of compare, later can use list comprehension 
    #+1 on the top ends to allow for the overlaps to show up
    count = 0
    for j in range(0,len(elfOne),1):

        x = range(int(elfOne[j][0]),int(elfOne[j][1])+1) 
        y = range(int(elfTwo[j][0]),int(elfTwo[j][1])+1) 

        z = [i for i in x if i in y]
        #lists return false if they have a length of zero, basically if there is any overlap, z will have a length of at least one
        #not the most efficient probably because we could stop as soon as we find one overlap instead of evaluation all of them above
        if(z):
            count += 1
        
    print(count)

if __name__ == "__main__":
    main() 

