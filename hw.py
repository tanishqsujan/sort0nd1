def intersect(A1, A2, A3, m, n, o):
    i,j,k = 0,0,0
    while i < m and j < n and k < o:
        if A1[i] < A2[j]:
            i += 1
        elif A2[j] < A3[k]:
            j += 1
        elif A3[k] < A1[i]:
            k += 1
        else:
            print(A1[i], end= " ")
            i += 1
            j += 1
            k += 1
            
A1= [1,2,3,6,7]
A2= [2,3,4,5,7]
A3= [3,4,6,7,8]

m= len(A1)
n= len(A2)
o= len(A3)

intersect(A1, A2, A3, m, n, o)