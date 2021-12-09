# -*- coding: utf-8 -*-
"""
Να γραφεί πρόγραμμα που να διάβαζει το πλήθος θετικών
ακεραίων που θα διαβαστούν. Το πρόγραμμα να υπολογίζει
τον μέσο όρο αυτών των αριθμών και να πραγματοποιεί
έλεγχο εισόδου για αρνητικές τιμές

"""
n=int(input("dose plithos arithmon:"))
s=0
for i in range(1,n+1):
    x=int(input("dose thetiko akeraio:"))
    while not(x>=0):
        print("lathos eisagogi")
        x=int(input("dose thetiko akeraio:"))
    s=s+x
average=s/n



