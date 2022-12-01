

def main():
    array = []
    total = 0
    total_arr = []
    answer1 = 0
    answer2 = 0
    elfCount = 0
    with open(r"C:\Users\mpn42\source\repos\AoC2022\AoC2022\AoC2022\Input Files\D1.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  
    #checks for number or blank, if blank it knows end of calorie count
    for i in array:
        if i != '':
            total = total + int(i)
            #print(total)  
        else:       
            total_arr.append(total)
            total = 0
    #totals numbers of elves so I can use this after the sort
    elfCount = len(total_arr)
    #definitely a faster way than sort but its fine
    total_arr.sort()
    #after the sort last 3 are the highest
    answer1 = total_arr[elfCount-1]
    answer2 = total_arr[elfCount-1] +total_arr[elfCount-2]+total_arr[elfCount-3]
        
    print (answer1)
    print (answer2)

if __name__ == "__main__":
    main() 
