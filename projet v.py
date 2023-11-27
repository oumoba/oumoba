import numpy as np
import scipy.linalg as lg
from time import time
import matplotlib.pyplot as plt

def remontee(A,b):
    # resout le systeme triangulaire superieur Ax=b
    (n,m)=np.shape(A)
    B=np.copy(b) # pour eviter de modifier b
    for i in range (n-1,-1,-1):# attention au pas et aux extremites. On part de i=n-1 et on arrete à i=0
        B[i]=B[i]-np.dot(A[i,i+1:n],B[i+1:n]) # attention, on ne change rien quand i=n-1
        B[i]=B[i]/A[i,i]
    return(B)
def MatriceA(n,tau):
   #tau=d/r0
   A=np.eye(n)
   for i in range(n):
       for j in range(n):
           A[i, j] = 1 / (1 + tau**2 * (i - j)**2) # V(d)=1/(1+tau^2) la formule (1)
   return A
n,tau=4,1           
A=MatriceA(n,tau);A
Phi=np.reshape(np.ones(n),(n,1));Phi

def descente(A,b):
    n,m=np.shape(A)
    n=len(b)
    x=b.copy()
    for i in range(0,n):
        for k in range(0,i):
            x[i]=x[i]-(np.dot(A[i,k],x[k]))
        x[i]=x[i]/A[i,i]
    return x

def LU1(A):
    n,n=np.shape(A)
    L=np.eye(n)
    B=np.copy(A)
    for k in range(0,n-1):
       for i in range(k+1,n):
           coef=-(B[i,k]/B[k,k])
           B[i,:]=B[i,:]+coef*B[k,:]
           L[i,k]=-coef
           U=B
    return U,L
LU1(A)
lg.lu(A)
def solutionLU(A,b):
    U,L=LU1(A)
    y=remontee(L, b)
    x=descente(U, y)
    return x
solutionLU(A,Phi)
