# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 14:17:00 2016

@author: hihi
"""

A = [[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]]
B = [[0.5,0.5],[0.4,0.6],[0.7,0.3]]
pai = [0.2,0.4,0.4]
O = [0,1,0]
#Delte = []

N  =  len(pai)
T   = len(O)

tmp = [0 for i in range(N)]
#Psi = [tmp for i in range(N)]
#Delte =  [tmp for i in range(T)] 
#use this format Delte[t][i] will change in the following step
#        Delte[t][i] = max_val*B[i][O[t]]
#        Psi[t][i] = max_idx
#Psi = [[0] * N] * T#low copy
#Delte =  [[0] * N] * T
Delte = [[]]
Psi=[[]]
for i in range(N):
    Delte[0].append(pai[i]*B[i][O[0]])
    Psi[0].append(-1)
#print Delte[0]
#Delte[0][2]=0
#print Delte
#print "------------------------------"
for t in range(1,T):
    #print t
    delte = []
    psi = []
    for i in range(N):
        #print tmp
#        print Delte[t-1]
#        for  j in  range(N):
#            print A[j][i],
#        print ''
        for j in range(N):
            tmp[j] = Delte[t-1][j]*A[j][i]
        #print Delte[t-1]
        max_idx = 0
        max_val = tmp[0]
        
        for j in range(1,N):
            if max_val < tmp[j]:
                max_val = tmp[j]
                max_idx = j
        #print tmp,max_val,max_idx
        delte.append(max_val*B[i][O[t]])
        psi.append(max_idx)
    Delte.append(delte)
    Psi.append(psi)
        #Psi[t][i] = max_idx
        #print Delte
        #print "------------------------------"
max_idx = 0      
max_val = Delte[T-1][0]
for i in range(1,N):
    if max_val < Delte[T-1][i]:
        max_val = Delte[T-1][i]
        max_idx = i
path = [0 for i in range(N)]
path[N-1] = max_idx
for i in range(T-1,0,-1):
    path[i-1] = Psi[i][path[i]]
print path
delte= Delte
psi =  Psi 
