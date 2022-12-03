

def main():
    array = []
    #build points look up dict
    pointsDict = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,
    'm': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,
    'z': 26,'A': 27,'B': 28,'C': 29,'D': 30,'E': 31,'F': 32,'G': 33,'H': 34,'I': 35,'J': 36,'K': 37,'L': 38,
    'M': 39,'N': 40,'O': 41,'P': 42,'Q': 43,'R': 44,'S': 45,'T': 46,'U': 47,'V': 48,'W': 49,'X': 50,'Y': 51,'Z': 52 }
    
   #reads into one array with both mine and their responses
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D3.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  

    middle = 0
    left = ''
    right = ''
    sum = 0
    #split the word in the middle into two strings, do a search on the first in the second
    for word in array:
        middle = int(len(word)/2)
        left = word[:-middle]
        right = word[middle:]

        for char in left:
            if char in right:
                sum += pointsDict[char]
                break
    print(sum)

if __name__ == "__main__":
    main() 

