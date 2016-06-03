#---------------------------------------------------------------------------
# Backware Equation for Region 2:
#   IAPWS-IF97-Rev : (P,S)->T (P,H)->T
#       pstoTreg2(p,s)
#       phtoTreg2(p,h)
#   Supp-PHS12-2014: (H,S)->P
#      hstopreg2(h,s) 
#---------------------------------------------------------------------------
import math
I=0
J=1
N=2
IJN=[[0,0,0.10898952318288E+04]
    ,[0,1,0.84951654495535E+03]
    ,[0,2,-0.10781748091826E+03]
    ,[0,3,0.33153654801263E+02]
    ,[0,7,-0.74232016790248E+01]
    ,[0,20,0.11765048724356E+02]
    ,[1,0,0.18445749355790E+01]
    ,[1,1,-0.41792700549624E+01]
    ,[1,2,0.62478196935812E+01]
    ,[1,3,-0.17344563108114E+02]
    ,[1,7,-0.20058176862096E+03]
    ,[1,9,0.27196065473796E+03]
    ,[1,11,-0.45511318285818E+03]
    ,[1,18,0.30919688604755E+04]
    ,[1,44,0.25226640357872E+06]
    ,[2,0,-0.61707422868339E-02] 
    ,[2,2,-0.31078046629583E+00]
    ,[2,7,0.11670873077107E+02]
    ,[2,36,0.12812798404046E+09]
    ,[2,38,-0.98554909623276E+09]
    ,[2,40,0.28224546973002E+10]
    ,[2,42,-0.35948971410703E+10]
    ,[2,44,0.17227349913197E+10]
    ,[3,24,-0.13551334240775E+05]
    ,[3,44,0.12848734664650E+08]
    ,[4,12,0.13865724283226E+01]
    ,[4,32,0.23598832556514E+06]
    ,[4,44,-0.13105236545054E+08]
    ,[5,32,0.73999835474766E+04]
    ,[5,36,-0.55196697030060E+06]
    ,[5,42,0.37154085996233E+07]
    ,[6,34,0.19127729239660E+05] 
    ,[6,44,-0.41535164835634E+06]
    ,[7,28,-0.62459855192507E+02]
    ]
def thetaPHreg2(pi,  eta):
     eta=eta-2.1
     theta=0
     for k in range(34):
         theta += IJN[k][2]*pow(pi,IJN[k][0])*pow(eta,IJN[k][1])
     return theta

def phtoTreg2(p,h):
      pi=p/1.0
      eta=h/2000.0
      return (1.0*thetaPHreg2(pi,eta))
   

IJN=[[-1.5,-24,-0.39235983861984E+06]
    ,[-1.5,-23,0.51526573827270E+06]
    ,[-1.5,-19,0.40482443161048E+05]
    ,[-1.5,-13,-0.32193790923902E+03]
    ,[-1.5,-11,0.96961424218694E+02]
    ,[-1.5,-10,-0.22867846371773E+02]
    ,[-1.25,-19,-0.44942914124357E+06]
    ,[-1.25,-15,-0.50118336020166E+04]
    ,[-1.25,-6,0.35684463560015E+00]
    ,[-1.0,-26,0.44235335848190E+05]
    ,[-1.0,-21,-0.13673388811708E+05]
    ,[-1.0,-17,0.42163260207864E+06]
    ,[-1.0,-16,0.22516925837475E+05]
    ,[-1.0,-9,0.47442144865646E+03]
    ,[-1.0,-8,-0.14931130797647E+03]
    ,[-0.75,-15,-0.19781126320452E+06]
    ,[-0.75,-14,-0.23554399470760E+05]
    ,[-0.5,-26,-0.19070616302076E+05]
    ,[-0.5,-13,0.55375669883164E+05]
    ,[-0.5,-9,0.38293691437363E+04]
    ,[-0.5,-7,-0.60391860580567E+03]
    ,[-0.25,-27,0.19363102620331E+04]
    ,[-0.25,-25,0.42660643698610E+04]
    ,[-0.25,-11,-0.59780638872718E+04]
    ,[-0.25,-6,-0.70401463926862E+03]
    ,[0.25,1,0.33836784107553E+03]
    ,[0.25,4,0.20862786635187E+02]
    ,[0.25,8,0.33834172656196E-01]
    ,[0.25,11,-0.43124428414893E-04]
    ,[0.5,0,0.16653791356412E+03]
    ,[0.5,1,-0.13986292055898E+03]
    ,[0.5,5,-0.78849547999872E+00]
    ,[0.5,6,0.72132411753872E-01]
    ,[0.5,10,-0.59754839398283E-02]
    ,[0.5,14,-0.12141358953904E-04]
    ,[0.5,16,0.23227096733871E-06]
    ,[0.75,0,-0.10538463566194E+02]
    ,[0.75,4,0.20718925496502E+01]
    ,[0.75,9,-0.72193155260427E-01]
    ,[0.75,17,0.20749887081120E-06]
    ,[1.0,7,-0.18340657911379E-01]
    ,[1.0,18,0.29036272348696E-06]
    ,[1.25,3,0.21037527893619E+00]
    ,[1.25,15,0.2581239729999E-03]
    ,[1.5,5,-0.1279900293381E-01]
    ,[1.5,18,-0.82198102652018E-05]
    ]

def thetaPStoT(pi,sigma):
      sigma=sigma-2.0
      theta=0.0
      for k in range(46):
        theta += IJN[k][2]*pow(pi,IJN[k][0])*pow(sigma,IJN[k][1])
      return theta

def pstoTreg2(p,s):
    pi=p/1.0
    sigma=s/2.0
    return (1.0*thetaPStoT(pi,sigma))

     
