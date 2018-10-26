

"""
Created on Sat Aug 01 11:56:10 2015

@author: Zombie.Soc // Similarities
"""

import numpy as np

print ('Z/A to element and charge collector')
print ('.........................by J. Braenzel')
print ('...............................2016... ')
print ('valid for elements within the 4. period')

print("search Z/A?")
ZA= input("Z/A:") # mass number of ion


print ("deviation of Z/A?")
accuracy = input("uncertainty in Z/A value: ")


# Zmax is -1 smaller by index system below, in real: 36
Zmax=35
#print charge
#table of elements within 4.period
names1=("H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu",'Zn',"Ga",'Ge',"As","Se","Br","Kr")
Mass1=(1.0079,4.0026,6.941,9.0122,10.811,12.011,14.007,15.999,18.988,20.18,22.990,24.305,26.982,29.086,30.974,32.065,35.453,39.948,39.098,40.078,
      44.956,47.867,51.996,51.996,54.938,55.845,58.933,58.693,63.546,65.38,69.723,72.64,74.922,78.96,79.904,83.789)
charge1=range(0,37) 
# charge=(0,1,2,3,)

     #some isotopes of C,N,O life time is >ms
names2=('C11','C13','C14','C15','C16','N13','N15','N16','N17','015','O17','O18','O19')
Mass2=(11.0114,13.0034,14.0032,15.0106,16.0147,13.0057,15.0001,16.0061,17.0085,15.0031,16.9991,17.9992,19.0036)    
# due to loop boarders the charge list is here -1
charge2=(0,5,5,5,5,5,6,6,6,6,7,7,7,7)
#count elements+1
ZmaxIso=(12)

namesAu=("Au")
chargeAu=(0,78)
ZmaxAu=1
MassAu=(0,196.96657)

names3=("artificial C12-C12")
charge3=(0,12)
Zmaxart=1
Mass3=(0,24.022)

# artificial elements
#names3=('C12-H','C12-H(2)','C12-C12')
#Mass3=(13.0189,14.0268,24.022)
#charge3=(0,5,6,11)
#Zmaxart=(2)


print ''
print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
print ''
if accuracy < 0:
	print "....search absolute match"
elif accuracy == 1:
	print "honestly???"


def listen(lab,N,Massx):
    mass=Massx[lab] 
#    print mass
#    print N
#    print mass,names[N] 
    iterable = (x+1 for x in range(N+1))
    rr=np.fromiter(iterable, np.float)
    for i in range (0,N):
#        print mass
#        print i
    # here the xx is due to a loop stop if same result
    #calculated can be returned.
        rr2=rr/mass
        xx=rr2
    return xx


# here in a wonderful double-for-loop now the election
# of matching Z/A values
# note: argument 'N' serves in 'listen' as election of specific element
# and maximum charge
def result(Zmaxx,ZA,namesx,accuracy,Massx,chargex):
#    print listen(1,Mass)
    print Zmaxx
    delta=accuracy
    for i in range(1,Zmaxx+1):
#        print i
#        print i,'i number of elment +1'
        laufzahl=chargex[i]
#        print laufzahl
        lab=i        
#        print laufzahl,"laufzahl"
        g=listen(lab,laufzahl,Massx)
#        print g

#        print listen(laufzahl,Mass),names[i],'Z/A'
        for j in range(0,laufzahl+1):
 #           print j,'in list of Z/A at place'
             x=g[j]
 #            print x
#            print j,'iteration charge'
#            print namesx[i]
             if (ZA-delta)<=x<=(ZA+delta):
                print ':D !!!'
                print x,'element:',namesx[i],j+1,'+','mass:',Massx[i]
                d=x/ZA
                print '1=100%, matches within:',d
             else:
                 continue 
    
print result(Zmax,ZA,names1,accuracy,Mass1,charge1)
print 'ISOTOPES OF C,N,O from A-1 to A+4'
print result(ZmaxIso,ZA,names2,accuracy,Mass2,charge2)
print 'artificial elements'
print result(Zmaxart,ZA,names3,accuracy,Mass3,charge3)
print 'gold'
print result(ZmaxAu,ZA,namesAu,accuracy,MassAu,chargeAu)



raw_input('press Return>')


