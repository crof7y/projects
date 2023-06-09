import numpy as np
p=np.array([[1,0],[0,1]])
q=np.array([[1,2],[3,4]])
m=p*q
a=p+q
print('Matrix Muliplication:\n', m)
print('\n')
print('Matrix Addition:\n', a)
print('\n')
d=np.dot(p,q)
print('Dot Product:\n', d)
print('Yes, the dot product is different than the matrix multiplication.')
print('\n\n----------------------------------------------------------------\n')
print('Same tasks without numpy')
print('\n----------------------------------------------------------------\n')
P=[1,0,0,1]
Q=[1,2,3,4]
M1=P[0]*Q[0]
M2=P[1]*Q[1]
M3=P[2]*Q[2]
M4=P[3]*Q[3]
print('Matrix Multiplication:')
print('[',M1,M2,']\n[',M3,M4,']')
A1=P[0]+Q[0]
A2=P[1]+Q[1]
A3=P[2]+Q[2]
A4=P[3]+Q[3]
print('\nMatrix Addition:')
print('[',A1,A2,']\n[',A3,A4,']')
D1=(P[0]*Q[0])+(P[2]*Q[2])
D2=(P[0]*Q[1])+(P[1]*Q[3])
D3=(P[2]*Q[0])+(P[0]*Q[2])
D4=(P[2]*Q[1])+(P[3]*Q[3])
print('\nDot Product:')
print('[',D1,D2,']\n[',D3,D4,']')
print('\nThis is achieved much easier by using numpy')