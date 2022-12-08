
#class for directories for name, and parent sets size to 0 when its created and an empty list of children
class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.parent = parent
        self.children = []

    #recursively update size as its expanded
    def update_size(self, sizeToAdd):
        self.size += sizeToAdd
        #this goes back up the tree increasing the size of each parent with the new file that was added until it reaches the root
        if self.parent:
            self.parent.update_size(sizeToAdd)

    #returns the name of the child to update the current directory
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

    #adds dirs
    def add_child(self, name, parent):
        self.children.append(Dir(name, parent))

    #adds files
    def add_file(self, name, size, parent):
        self.children.append(File(name, size, parent))

#class for files for name, size, parent, and a call to update the parent when it gets created
class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        parent.update_size(self.size)


#this function controls eceuting changing the current directory
def exec_command(dir):
    #references the global variable for the directory and root here
    global currentDirectory
    global root

    if dir == '/':
        currentDirectory = root
    elif dir == "..":
        currentDirectory = currentDirectory.parent
    else:
        currentDirectory = currentDirectory.get_child(dir)

def size_check(dir,value,resultsList):
    if dir.size <= value:
        resultsList.append(dir)
    for child in dir.children:
        #checks to see if this is a directory type, if it is call again, if its a file we dont care
        if isinstance(child, Dir):
            resultsList = size_check(child,value,resultsList)
    return resultsList

def size_check_P2(dir,value,resultsList):
    if dir.size >= value:
        resultsList.append(dir)
    for ch in dir.children:
        #checks to see if this is a directory type, if it is call again, if its a file we dont care
        if isinstance(ch, Dir):
            resultsList = size_check_P2(ch,value,resultsList)
    return resultsList

#global variables, could have passed these better
root = Dir('/', None)
currentDirectory = None

def main():
    
    array = []
    #Input processing
    with open(r"C:\repos\AoC2022\AoC2022\Input Files\D7.txt","r") as f:
        for val in f.read().splitlines():
            array.append((val))  

    for x in array:
        #reads input into individual sections in a list
        listCommand = x.split()
        
        if x[0] == '$':
            #we are moving directories with a cd command
            if 'cd' in x:
                exec_command(listCommand[2])
            #ignore the ls line because we dont care
            elif x.startswith('$ ls'): 
                continue
            #if the above fail then we are getting a list of dir or files to add to the current directory
        else:
            #adding directory
            if listCommand[0] == 'dir':
                currentDirectory.add_child(listCommand[1],currentDirectory)
            #adding file
            else:
                currentDirectory.add_file(listCommand[1],int(listCommand[0]),currentDirectory)         

    #PART ONE logic
    sum = 0
    lessThanDirList = []
    for dir in size_check(root,100000,[]):
        lessThanDirList.append(dir.size)

    for x in lessThanDirList:
        sum+=x

    print('P1 answer:',sum)

    #PART TWO logic
    total = 70000000
    need = 30000000
    #calcs what we currently have free
    curFree = total-root.size
    #calcs what we need to free
    minToDelete = need-curFree

    #creates a list of directories that meet that criteria
    largeDirList = []
    for dir2 in size_check_P2(root,minToDelete,[]):
        largeDirList.append(dir2.size)
        continue

    #sorts it so the smallest one is [0]
    largeDirList.sort()
    print('P2 answer:',largeDirList[0])

if __name__ == "__main__":
    main() 



