myList =  [1, 0, 5, 6, 0, 2]
x = 0 

count = 0

for i in myList:
    if(i==x):
        count=count+1

print("{} has occured {} times".format(x,count))