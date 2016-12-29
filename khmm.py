# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 14:17:00 2016

@author: hihi
"""

def viterbi(A,B,pai,O):
#Delte = []

    N  =  len(pai)
    T   = len(O)
    
    tmp = [0 for i in range(N)]
    
    Delte = []
    Psi=[]
    delte = []
    psi = []
    #initialization
    for i in range(N):
        delte.append(pai[i]*B[i][O[0]])
        psi.append(-1)
    Delte.append(delte)
    Psi.append(psi)
    # recurrence
    for t in range(1,T):
        delte = []
        psi = []
        for i in range(N):
            for j in range(N):
                tmp[j] = Delte[t-1][j]*A[j][i]
    
            max_idx = 0
            max_val = tmp[0]        
            for j in range(1,N):
                if max_val < tmp[j]:
                    max_val = tmp[j]
                    max_idx = j
    
            delte.append(max_val*B[i][O[t]])
            psi.append(max_idx)
        Delte.append(delte)
        Psi.append(psi)
    #finish
    max_idx = 0      
    max_val = Delte[T-1][0]
    for i in range(1,N):
        if max_val < Delte[T-1][i]:
            max_val = Delte[T-1][i]
            max_idx = i
    #backtrack
    path = [-1 for i in range(N)]
    path[N-1] = max_idx
    for i in range(T-2,-1,-1):
        path[i] = Psi[i+1][path[i+1]]
    #print path
    return path,max_val
