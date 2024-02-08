import numpy as np


def simplexe(A,b,c, permut):
    m,n = A.shape
    if m>=n or c.shape[0] != n or b.shape[0] != m:
        print("dimensões incompatíveis")
        
    if min(b) < 0 :
        print("o vetor b deve ser >=0")
        
    while True:
        Ap = np.column_stack((A[:permut[i]] for i in range(n)))
        cp = np.array([c[permut[i]]for i in range(n)])
        
        if np.linalg.det(Ap[:,n]) == 0:
            print("Matriz não inversível")
        
        invAp = np.linalg.inv(Ap[:,:n])
        Chb = np.dot(invAp, Ap[:,m:])
        bhbase = np.dot(invAp, b)
        
        cbase = np.dot(cp[:m], Chb) + cp[m:]
        cmax = max(cbase)
        
        if cmax<=0:
            break
        ihb = np.argmax(cbase) + m
        xrmax = np.array([bhbase[i]/Chb[i][ihb-m] for i in range(n)])
        vmax = max(xrmax)
        
        for i in range(m):
            if xrmax[i] <= 0:
                xrmax[i] = vmax+1
            
        ib = np.argmin(xrmax)
        print("out=", permut[ib], "in=", permut[ihb])
        
        permut[ib], permut[ihb] = permut[ihb] , permut[ib]
        
        xp = np.hstack((bhbase, np.zeros(n,m)))
        x = np.empty(n)
        for i in range(n):
            x[permut[i]] = xp[i]
        return x,np.dot(c,x)
    
A = np.array([[1,2,1,0,0],[1,0,0,1,0],[0,1,0,0,1]])
b= np.array([9,3,4])
c = np.array([5,2,0,0,0])

permut= np.array([3,2,1,0])

print(simplexe(A,b,c,permut))