import math as m

def printpower(set , setsize) :

    psetsize = (int) (m.pow(2 , setsize))
    outer = 0
    inner = 0

    for outer in range(0 , psetsize) :

        for inner in range(0,setsize) :

            if outer & (1 << inner) > 0 :

                print(set[inner] , end = " ") 
        print("")

size = int(input("enter n.o of number"))

set = []

for i in range(0 , size) :
    n = int(input("enter a number"))
    set.append(n)

printpower(set , len(set))