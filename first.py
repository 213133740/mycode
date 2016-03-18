from __future__ import division
import math
D=2
v=0.0098
Re=2000
rho=998
V=Re*v/10000/(D/100)
L=(math.pi/4)*((D/100)**2)*V
print ("The required Largest Discharge",round(L*1000*60,3),"L/min")
f=64/Re
u=V*(math.sqrt(f/8))
tou=rho*(u**2)
print("tou=",round(tou,4),"Pa")
    
    
