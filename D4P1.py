


def main():
    import re

    array = []
    
    #elfOne.append([])
    
    #elfTwo.append([])
    
    
   #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D4.txt","r") as f:
        for val in f.read().splitlines():
            valClean = re.split(r',|-',val)
            array.append((valClean))  

    print(array)

    elfOne = [[] for i in range(len(array))]
    elfTwo = [[] for i in range(len(array))]


    for i in range(0,len(array),1):
        elfOne[i]= array[i][:-2]
        elfTwo[i]=array[i][2:]


    count = 0

    #need to fix the having to convert int at time of compare, later
    for j in range(0,len(elfOne),1):
        print(elfOne[j],elfTwo[j])
        if int(elfOne[j][0]) <= int(elfTwo[j][0]) and int(elfOne[j][1]) >= int(elfTwo[j][1]):
            print('two in one')
            count += 1
        elif int(elfTwo[j][0]) <= int(elfOne[j][0])  and int(elfTwo[j][1])>= int(elfOne[j][1]):
            print('one in two')
            count += 1

    print(count)

if __name__ == "__main__":
    main() 

