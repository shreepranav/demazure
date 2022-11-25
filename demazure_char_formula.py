import sys
import time

#Pick the suitable Cartan matrix A
#NOTE: We use Bourbaki notation, but indexing of nodes in a Dynkin diagram always starts with 0. For example, in G_2, the long simple root is indexed 0 and short simple root is indexed 1.
# For E_6, the 5 element chain is indexed 0,2,3,4,5 and the node indexed 1 is connected to node 3 (This is Bourbaki notation, but shifted down by 1 to start indexing from 0).

# For E_6
#A = [[2,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,0,-1],[0,0,-1,2,-1,0],[0,0,0,-1,2,0],[0,0,-1,0,0,2]]

# For E_7
#A = [[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]]

# For E_7^(1)
#A = [[2,-1,0,0,0,0,0,0],[-1,2,0,-1,0,0,0,0],[0,0,2,0,-1,0,0,0],[0,-1,0,2,-1,0,0,0],[0,0,-1,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,-1],[0,0,0,0,0,0,-1,2]]

# For E_8
#A = [[2,0,-1,0,0,0,0,0],[0,2,0,-1,0,0,0,0],[-1,0,2,-1,0,0,0,0],[0,-1,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,-1],[0,0,0,0,0,0,-1,2]]

# For E_8^(1)
A = [[2,0,0,0,0,0,0,0,-1],[0,2,0,-1,0,0,0,0,0],[0,0,2,0,-1,0,0,0,0],[0,-1,0,2,-1,0,0,0,0],[0,0,-1,-1,2,-1,0,0,0],[0,0,0,0,-1,2,-1,0,0],[0,0,0,0,0,-1,2,-1,0],[0,0,0,0,0,0,-1,2,-1],[-1,0,0,0,0,0,0,-1,2]]


# For F_4
#A = [[2,-1,0,0],[-1,2,-2,0],[0,-1,2,-1],[0,0,-1,2]]

# For G_2
#A = [[2, -3], [-1, 2]]

rank = len(A)



def r2s(r):
    return ' '.join(map(str, r))

def s2r(r):
    return [int(i) for i in r.split()]


# Calculates the scalar product <\lambda_k - r, \alpha_i^{\check}>
def prod(r, i, k):
    s = -sum([r[j]*A[j][i] for j in range(rank)])
    if i==k:
        s += 1
    return s

# Calculates D_w(e^(\lambda_k))
def demazure(w, k):
    zero = [0 for i in range(rank)]    
    D = {}
    D[r2s(zero)] = 1
    temp_D = {}
    temp_D[r2s(zero)] = 1
    for i in w:
#        print(i)
#        print(D)
        for text in D:
            coeff = D[text]
            r = s2r(text)
            m = prod(r, i, k)
#            print(r, m, coeff)
            if m >= 0:
                for j in range(m):
                    r[i] += 1 
                    t = r2s(r)
                    if t in temp_D:
                        temp_D[t] += coeff
                    else:
                        temp_D[t] = coeff
            elif m == -1:
                if text not in temp_D:
                    print("Tried to delete a root not in the list!")
                    sys.exit(1)
                if temp_D[text] == coeff:
                    del temp_D[text]
                else:
                   temp_D[text] -= coeff 
            else:
                for j in range(-m):                    
                    t = r2s(r)
                    if temp_D[t] == coeff:
                        del temp_D[t]
                    else:
                        temp_D[t] -= coeff 
                    r[i] -= 1
#            print(temp_D)
#        print()
                        
        D.clear()
        D = temp_D.copy()
#        print(temp_D)
#        print()
#        print()
    return D       
        
    
    
    
    
    
    
    

################################################


#Enter Weyl group element here

w = [5, 6, 7, 8, 0, 1, 2, 3, 1, 4, 2, 3, 1, 4, 5, 4, 2, 3, 1, 4, 3, 5, 4, 6, 5, 4, 2, 3, 1, 4, 3, 5, 4, 2, 6, 5, 4, 3, 7, 6, 5, 4, 2, 3, 1, 4, 3, 5, 4, 2, 6, 5, 4, 3, 1, 7, 6, 5, 4, 2, 3, 4, 5, 6, 8, 7, 6, 5, 4, 2, 3, 1, 4, 3, 5, 4, 2, 6, 5, 4, 3, 1, 7, 6, 5, 4, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 2, 3, 1, 4, 3, 5, 4, 2, 6, 5, 4, 3, 1, 7, 6, 5, 4, 2, 3, 4, 5, 6, 7]


#root = [1,0]
#print(s2r(r2s(root)))

# L will store the values D_w(\lambda_i)
L = [0 for i in range(rank)]

for k in range(rank):
    t0 = time.time()
    D = demazure(w,k)
    t1 = time.time()
    s = sum(D.values())
    l = len(D)
    L[k] = s
    print(k, ": ",s, l, 100.0*l/s, 1.0*s/l, t1-t0)

#print("Input: ")
#dummy = input()
#print(L)

    
