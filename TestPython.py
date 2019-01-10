list = [1,2,3,4]
tup = ('Rahul','Chakraborty','New Jersy')
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print tinydict.keys()
print tinydict.values()

def printInfo(arg, *varargs):
    print arg
    for var in varargs:
        print var

    return

printInfo(10)
printInfo(20,30,40)

#Python Lambda

sum = lambda arg1,arg2 : arg1+arg2
print(sum(1,2))

for key, value in tinydict.iteritems():
    print key
    print value