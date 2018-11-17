from math import sin, cos, tan, acos, asin, atan
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2
from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

                                            #This is where the user inputs the function and intervals. 
function=input("What function would you like to analyze? ")
print("If you choose a log function, make sure your interval is within the domain :)")
x1=int(input("Where do you want your interval to start (x value)? "))
x2=int(input("Where do you want your interval to end (x value)? "))

        
#print(function)

xcoordlist=[]                               #This prints a list of the x values. 
for i in range(x1,x2+1):
    if i == x2:
        xcoordlist.append(i+.0)
    else:
        for m in [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            #print(i+m)
            xcoordlist.append(i+m)
#print(xcoordlist)


    
a=False
ycoordlist=[]                               #This prints a list of the y values. 
for r in xcoordlist:
    x=r
    Locfunction=function.lower()
    try:
        y=eval(Locfunction)
        ycoordlist.append(y)
    except: 
        a=True
        asymptote=r
        print("There is a vertical asymptote at x=", asymptote, " in this function!")
#print(ycoordlist)


                                             #This will find the y+.001 value for the symmetric difference quotient.
ycoordlist1=[]                              
for r in xcoordlist:
    x=r+0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist1.append(y)
#print(ycoordlist1)


ycoordlist2=[]                              #This will find the y-.001 value for the symmetric differnce quotient. 
for r in xcoordlist:
    x=r-0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist2.append(y)
#print(ycoordlist2)


intervalnum=len(ycoordlist1)                #This tells us how long our cordinate lists are 
#print(intervalnum)                            #so we know how long to run the loop. 


derivlist=[]                                #This makes a list of the derivatives, and a rounded list
derivlist1=[]                                   #of the derivatives. 
for s in range(intervalnum):
    deriv  = ((ycoordlist1[s])-(ycoordlist2[s]))/(2*0.001)
    derivlist1.append(round(deriv,2))
    derivlist.append(deriv)
#print (derivlist1)
#print (derivlist)
derivlista=[]                                #This makes a list of the derivatives, and a rounded list
derivlista1=[]                                   #of the derivatives. 
for s in range(intervalnum):
    deriva  = ((ycoordlist1[s]+0.001)-(ycoordlist1[s]-0.001))/(2*0.001)
    #derivlista1.append(round(deriva,2))
    derivlista.append(deriva)
#print (derivlista1)
print (derivlista)

derivlistb=[]                                #This makes a list of the derivatives, and a rounded list
derivlistb1=[]                                   #of the derivatives. 
for s in range(intervalnum):
    derivb  = ((ycoordlist2[s]+0.001)-(ycoordlist2[s]-0.001))/(2*0.001)
    #derivlistb1.append(round(derivb,2))
    derivlistb.append(derivb)
#print (derivlistb1)
print (derivlistb)
    
deriv2list=[]
deriv2list1=[]
for s in range(intervalnum):
    deriv2  = ((derivlista[s])-(derivlistb[s]))/(2*0.001)
    #deriv2list1.append(round(deriv2,2))
    deriv2list.append(deriv2)
#print(deriv2list1)
print (deriv2list)
