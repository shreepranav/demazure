# Pick the desired Cartan matrix A

# For A_5
#A = [[2,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,0],[0,0,-1,2,-1],[0,0,0,-1,2]]


# For F_4
#A = [[2,-1,0,0],[-1,2,-2,0],[0,-1,2,-1],[0,0,-1,2]]


# For E_6
#A = [[2,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,0,-1],[0,0,-1,2,-1,0],[0,0,0,-1,2,0],[0,0,-1,0,0,2]]

# For E_7
#A = [[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]]

# For D_4
#A = [[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]]

# For E_6^(1)
#A = [[2,-1,0,0,0,0,0],[-1,2,-1,0,0,0,0],[0,-1,2,-1,0,-1,0],[0,0,-1,2,-1,0,0],[0,0,0,-1,2,0,0],[0,0,-1,0,0,2,-1],[0,0,0,0,0,-1,2]]

# For E_8
A = [[2,0,-1,0,0,0,0,0],[0,2,0,-1,0,0,0,0],[-1,0,2,-1,0,0,0,0],[0,-1,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,-1],[0,0,0,0,0,0,-1,2]]

rank = len(A)

def weyl(w, root):
    output = root
    l=len(w)
    for i in range(0,l):
        index = w[l-i-1]
        change = 0
        for j in range(rank):
            change += output[j]*A[j][index]
#            print (i,j, index, output[j],A[j][index])
        output[index] -= change
    return(output)

#print weyl([6],[0,0,1,0,0,0])


# Enter length of the longest Weyl group element
l = 120

# Enter the primer here
longest = [3,4]

#Gives the longest weyl element, starting count from 1 NOT 0

for i in range(l - len(longest)):
    s = -1
    j = 0
    while s < 0:
        j += 1
        root = [0 for k in range(rank)]
        root[j-1]+=1
        root = weyl(longest, root)
#        print root
        s = sum(root)
    longest.append(j-1)

#longest[0]=0
#longest.reverse()

print longest

for i in range(rank):
    root = [0 for j in range(rank)]
    root[i] += 1
    print(weyl(longest,root))
    
#w0 = [2,3,1,2,5,2,3,1,2,0,4,6]
#print w0
#w0 = [i+1 for i in w0]
#print w0
w0 = longest

print(w0)

#print weyl(w0,[1,1,1,1,1,1,0])
        