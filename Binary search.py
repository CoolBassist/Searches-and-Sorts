#the data to be searched
data = [3,4,5,5,6,7,10,10,11,34,43]

def Search(dataToFind, start = 0, end = 10):
    #if the data cannot be found
    if start > end:
        print(dataToFind,"not found")
        return
    
    middlePoint = int((start + end) / 2)

    if data[middlePoint] == dataToFind:
        print(dataToFind, "found at position", middlePoint, "\b!")
        return

    #recursively narrow the list down
    if(data[middlePoint] > dataToFind):
        Search(dataToFind, start, middlePoint-1)
    else:
        Search(dataToFind, middlePoint+1, end)


Search(int(input("Please enter data you want to find: ")))