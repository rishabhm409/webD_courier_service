import random

def getref():
    refno='sp'
    for i in range(1,3):
        n=random.randrange(1,5)
        refno+=str(n)
        n=random.randrange(0,7)
        refno+=str(n)
        n=random.randrange(3,9)
        refno+=str(n)

    return refno