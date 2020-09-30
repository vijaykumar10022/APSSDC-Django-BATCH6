class Arithmatic:
         def __init__(self,a,b):
                  self.a=a ## class varaibles
                  self.b=b
         def add(self):
                  print("Addition of {} and {} is {}".format(self.a,self.b,self.a+self.b))
         def myfun(self,myname):
                  self.myname=myname
                  #myname is local variable
                  print("my name is {}".format(myname))
         def ref(self):
                  print("Reference{}".format(self.myname))
                  
