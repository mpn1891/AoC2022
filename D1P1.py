

def main():
    array = []
    total = 0
    answer = 0
    with open(r"C:\Users\mpn42\source\repos\AoC2022\AoC2022\AoC2022\Input Files\D1.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  
        
    print(array)

    for i in array:
        if i != '':
            total = total + int(i)
            #print(total)
        
        else:       
            if total > answer:
                answer = total
            total = 0

    print (answer)

if __name__ == "__main__":
    main()