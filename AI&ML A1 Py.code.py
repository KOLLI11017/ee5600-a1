import numpy as np
import sympy as sp
from sympy import Eq,solve,symbols

[a1,b1,c1,d1]=[1,2,3,4]
[a2,b2,c2,d2]=[2,1,-1,-5]
[a3,b3,c3,d3]=[5,3,-6,-8]
x,y,z=symbols('x,y,z')
a4=1
[b4,c4,d4]=symbols('b4,c4,d4')
q1=np.dot([a1,b1,c1],[x,y,z])
q2=np.dot([a2,b2,c2],[x,y,z])
q3=np.dot([a3,b3,c3],[x,y,z])

Pp1=Eq(q1,d1)
Pp2=Eq(q2,d2)
Pp3=Eq(q3,d3)

POI=solve([Pp1,Pp2,Pp3],[x,y,z])

print('POINT on PLANE (x0,y0,z0) = (',POI[x],',',POI[y],',',POI[z],')')


N1=np.dot([a3,b3,c3],[a4,b4,c4])

N2=np.dot(np.cross([a1,b1,c1],[a2,b2,c2]),[a4,b4,c4])

Np1=Eq(N1,0)
Np2=Eq(N2,0)

Norcoeff=solve([N1,N2],[b4,c4])

d4= np.dot([POI[x],POI[y],POI[z]],[a4, Norcoeff[b4],Norcoeff[c4]])
print('Coefficients of PLANE (a4,b4,c4,d4) = ' '(', a4,',', Norcoeff[b4],',', Norcoeff[c4],',', d4,')')
