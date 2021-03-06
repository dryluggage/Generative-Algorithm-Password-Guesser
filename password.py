import random
import sys
import numpy as np

password = "s  a  s  a s  "


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

for i in range(10):
    alphabet.append(str(i))




generation = 1
lettermutationrate = 1
wordlenmutationrate = 1
passwordlen = len(password)
alphabetlen = len(alphabet)



pointsforsameletter = 1
lengthdeductuionmulitplyer = 1
maxstring = len(password) + 10
specimenlist = 80

maxpoints = pointsforsameletter * passwordlen

#lowestnumber=(lengthdeductuionmulitplyer*passwordlen+100)*-1

def randomstring():
    randguess = ""
    for i in range(random.randint(1,maxstring)):
        randguess+=alphabet[random.randint(0,len(alphabet)-1)]

    return randguess




def rate(tried):
    points=0

    lengthdeduction=passwordlen-len(tried)
    if lengthdeduction>0:
        lengthdeduction=lengthdeduction*-1




    points+=lengthdeductuionmulitplyer*lengthdeduction


    for i in range(min(len(tried),passwordlen)):
        
        if password[i]==tried[i]:
            points+=pointsforsameletter

    return points




trylist = []

pointlist = []

for i in range(specimenlist):
    guess=randomstring()
    trylist.append(guess)

    
    pointlist.append(rate(guess))




def switch(even,odd,index):
    if index%2==0:
        return even
    else :
        return odd





def crossstrings(cutvalueslist,firststring,secondstring):


    cutvalueslist=cutvalueslist[:]
    firststring=firststring[:]
    secondstring=secondstring[:]
    crossofstrings=""
    for index,sublist in enumerate(cutvalueslist):

        oldc,newc = sublist
        stringcopy=switch(firststring,secondstring,index)


        crossofstrings+=stringcopy[oldc:newc]


    laststringadd=switch(firststring,secondstring,len(cutvalueslist))

    return crossofstrings+laststringadd[newc:]






def crossbreed(stringlist):

    stringlist = stringlist[:]
    newstringlist = []

    while len(stringlist) != 0 or len(stringlist) != 1:


        if len(stringlist) == 0 or len(stringlist) == 1:
            break


        aindex = random.randint(0,len(stringlist) -1)
        a = stringlist[aindex]
        del stringlist[aindex]

        bindex = random.randint(0,len(stringlist)-1)
        b = stringlist[bindex]
        del stringlist[bindex]



        oldcuttpoint=0


        cutlist=[]




        cuttpoint=0

        #for i in range(min(len(a),len(b) )  ):

        #for i in range(max(len(a),len(b) )  ):
        i=0

        samecutpoint=0
        while True:
            switchab = switch(a,b,i)


            if oldcuttpoint>=len(switchab):
                break

            #print(oldcuttpoint,len(switchab)-1)

            cuttpoint=random.randint(oldcuttpoint,len(switchab))

            if cuttpoint==oldcuttpoint:

                samecutpoint+=1

            else:
                samecutpoint=0

            #print(samecutpoint ,oldcuttpoint,cuttpoint)
            if samecutpoint==2:
                cuttpoint+=1
                samecutpoint=0

            cutlist.append([oldcuttpoint,cuttpoint])
            oldcuttpoint=cuttpoint
            #print(switchcd)

            i+=1


        #print(cutlist)
        c=crossstrings(cutlist,a,b)
        d=crossstrings(cutlist,b,a)

        newstringlist.append(c)

        newstringlist.append(d)



    return newstringlist








def kill(stringlist,numlist,howmany = 70):
    stringlist = stringlist[:]
    numlist = numlist[:]
    
    best = []
    for i in range(specimenlist - howmany):


        if i == 9:
            #print("the best 10 of generation: "+str(generation))


            print()
            print(password)
            print()
            #print("decoding...")
            #print()
            for i in best:
                print(i)
            #print()
            #print()


        bestindex = numlist.index(max(numlist))
        best.append(stringlist[bestindex])
        del stringlist[bestindex]
        del numlist[bestindex]


    for i in range(10):

        randomindex = random.randint(0,len(stringlist) -1)
        best.append(stringlist[randomindex])

        del stringlist[randomindex]



    return best






def mutate(best):
    best = best[:]
    #print(best)
    newlist = []
    for word in best:
        #print(word)
        newword=""
        for letter in word:
            #print(letter)
            newwordlen = len(newword)

            if random.randint(1,10) <= lettermutationrate:
                newword += alphabet[random.randint(0,alphabetlen-1)]

            else:
                newword += letter



            if random.randint(1,10) <= wordlenmutationrate:
                if random.randint(1,10) <= 5 and newwordlen < maxstring:
                    newword += alphabet[random.randint(0,alphabetlen - 1)]
                elif newwordlen > 1:
                    excludeindex = random.randint(0,newwordlen-1)

                    if excludeindex == newwordlen:
                        newword = newword[:excludeindex]
                    elif excludeindex == 0:
                        newword = newword[excludeindex + 1:]
                    else:


                        newword = newword[:excludeindex] + newword[excludeindex + 1:]


        #print("wordadded")
        newlist.append(newword)
    #print("done")
    return newlist+best






while True:
    bestlist = kill(trylist,pointlist)
    print(len(bestlist))
    bestlist = bestlist + crossbreed(bestlist)
    print(len(bestlist))
    
    #trylist=[]
    #bestlist=mutate(bestlist)
    trylist = mutate(bestlist)
    #print(len(trylist))
    #print(len(bestlist))

    pointlist = []
    for i in trylist:
        points = rate(i)
        pointlist.append(points)
        if points == maxpoints:
            print("the password was found after",generation,"generations")
            print()
            print(i)


            


            #input()
            sys.exit()


    generation+=1
