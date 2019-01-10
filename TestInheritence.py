#!/usr/bin/python

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print counter._JustCounter__secretCount


print "JustCounter.__doc__:", JustCounter.__doc__
print "JustCounter.__name__:", JustCounter.__name__
print "JustCounter.__module__:", JustCounter.__module__
print "JustCounter.__bases__:", JustCounter.__bases__
print "JustCounter.__dict__:", JustCounter.__dict__