def sortzeroone(A,n):
    
    #count the number of zeroes in an array
    count= 0
    
    for i in range(0,n):
        if (A[i]== 0):
            count= count + 1
    
    #filling the A with zero until count        
    for i in range(0,count):
        A[i]= 0
        
    #filling remaining space with one
    for i in range(count,n):
        A[i]= 1
        
A= [0,0,1,1,0,1,0,1]
n= len(A)

sortzeroone(A,n)
print("Sorted Array: ", end= " ")
for i in range(0,n):
    print(A[i], end= " ")