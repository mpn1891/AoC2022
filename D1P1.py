
array = []
answer = 0
with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D1.txt","r") as f:
    for val in f.read().split():
        array.append(int(val))  
        
print(array)

for i in range(len(array)-1):
    if array[i+1] > array[i]:
        answer =+ answer + 1
        continue
    else:
        continue

print (answer)