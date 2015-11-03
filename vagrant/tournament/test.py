
import random

testset = []

def getRandPos(testset):
    goodToInsert = False
    while goodToInsert != True:
        pos = random.randrange(1, len(testset))
        testItem = testset[pos]
        if testItem[2] == False:
            goodToInsert = True
            newTup = (testItem[0], testItem[1], True)
            oldTup = testset[pos]
            testset.remove(oldTup)
            testset.insert(pos, newTup)
            print pos
        else:
            print "Looping again"
    return

if __name__ == '__main__':

    for x in xrange(0, 5):
        myBool = False
        testset.append((x, x*2, myBool))

    # print len(testset)

    insertLoc = random.randrange(1, len(testset))
    for x in xrange(0,3):
        getRandPos(testset)



    #print insertLoc
